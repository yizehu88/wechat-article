#!/usr/bin/env python3
"""
微信公众号文章自动收录脚本
自动抓取文章内容、生成摘要、更新index.html并提交到Git
"""

import sys
import re
import json
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, List, Any

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("请先安装依赖: pip install requests beautifulsoup4")
    sys.exit(1)

PROJECT_ROOT = Path(__file__).parent.parent
INDEX_HTML = PROJECT_ROOT / "wechat_articles" / "index.html"

PREDEFINED_TAGS = {
    "AI/大模型": ["AI", "大模型", "LLM", "深度学习", "神经网络", "GPT", "ChatGPT", "Agent"],
    "量化框架": ["量化", "回测", "策略", "交易", "框架", "Backtest"],
    "金融数据": ["数据", "行情", "财务", "基本面", "API"],
    "期货CTP": ["期货", "CTP", "SIMNOW", "实盘"],
    "工具": ["工具", "开源", "GitHub", "库", "Library"],
    "LLM": ["LLM", "语言模型", "GPT", "Claude"],
    "智能体": ["智能体", "Agent", "AutoGPT", "多智能体"],
    "技术指标": ["指标", "RSI", "MACD", "K线", "均线"],
    "风险管理": ["风险", "止损", "仓位", "VaR", "回撤"],
    "策略优化": ["优化", "参数", "过拟合", "调参"],
    "形态识别": ["形态", "杯柄", "头肩", "识别"],
    "交易心理": ["心理", "心态", "纪律", "情绪"],
    "开源项目": ["开源", "GitHub", "Star"],
    "IM即时通讯": ["IM", "聊天", "通讯", "消息"],
    "私有部署": ["私有", "部署", "自托管", "本地"],
    "企业级": ["企业", "架构", "系统", "生产"]
}


class ArticleCollector:
    def __init__(self, url: str):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"
        }

    def fetch_content(self) -> Optional[str]:
        try:
            response = requests.get(self.url, headers=self.headers, timeout=15)
            response.encoding = 'utf-8'
            if response.status_code == 200:
                return response.text
            else:
                print(f"HTTP错误: {response.status_code}")
                return None
        except requests.RequestException as e:
            print(f"网络请求失败: {e}")
            return None

    def parse_article(self, html: str) -> Dict[str, Any]:
        soup = BeautifulSoup(html, 'html.parser')

        title = self._extract_title(soup)
        account = self._extract_account(soup)
        content = self._extract_content(soup)
        summary = self._extract_summary(content)
        key_points = self._extract_key_points(content)
        tags = self._extract_tags(content)
        repos = self._extract_repos(content)

        return {
            "title": title,
            "account": account,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "url": self.url,
            "tags": tags,
            "summary": summary,
            "keyPoints": key_points,
            "repos": repos
        }

    def _extract_title(self, soup: BeautifulSoup) -> str:
        for tag in ['h1', '.rich_media_title', '#activity-name', 'title']:
            elem = soup.select_one(tag)
            if elem:
                title = elem.get_text().strip()
                if len(title) > 5:
                    return title[:80]
        return "未获取到标题"

    def _extract_account(self, soup: BeautifulSoup) -> str:
        for tag in ['.account_nickname', '#js_name', '.profile_nickname']:
            elem = soup.select_one(tag)
            if elem:
                return elem.get_text().strip()
        account_match = re.search(r'var biz = "([^"]+)"', str(soup))
        if account_match:
            return f"公众号ID:{account_match.group(1)}"
        return "未获取到公众号"

    def _extract_content(self, soup: BeautifulSoup) -> str:
        for tag in ['.rich_media_content', '#js_content', 'article']:
            elem = soup.select_one(tag)
            if elem:
                return elem.get_text().strip()
        return ""

    def _extract_summary(self, content: str) -> str:
        if not content:
            return "暂无摘要"
        paragraphs = [p.strip() for p in content.split('\n') if len(p.strip()) > 20]
        summary = ' '.join(paragraphs[:2])
        if len(summary) > 150:
            summary = summary[:147] + "..."
        return summary if summary else "暂无摘要"

    def _extract_key_points(self, content: str) -> List[str]:
        if not content:
            return ["暂无核心要点"]

        paragraphs = [p.strip() for p in content.split('\n') if 20 < len(p.strip()) < 200]
        key_points = []
        for p in paragraphs[:8]:
            clean_p = re.sub(r'[^\u4e00-\u9fa5a-zA-Z0-9，。、；：""''（）《》！]', '', p)
            if len(clean_p) > 10:
                key_points.append(clean_p)
            if len(key_points) >= 6:
                break

        return key_points if key_points else ["暂无核心要点"]

    def _extract_tags(self, content: str) -> List[str]:
        matched_tags = []
        for tag, keywords in PREDEFINED_TAGS.items():
            for keyword in keywords:
                if keyword in content:
                    matched_tags.append(tag)
                    break
            if len(matched_tags) >= 4:
                break
        return matched_tags if matched_tags else ["工具"]

    def _extract_repos(self, content: str) -> List[Dict[str, str]]:
        repos = []
        github_pattern = r'https?://github\.com/[a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_./]+'
        matches = re.findall(github_pattern, content)
        seen = set()
        for url in matches[:3]:
            name = url.split('/')[-1].replace('.git', '')
            if name not in seen and len(name) > 2:
                repos.append({
                    "name": name,
                    "github": url,
                    "localPath": "—",
                    "status": "pending",
                    "stars": "—"
                })
                seen.add(name)
        return repos

    def generate_evaluation(self, article: Dict[str, Any]) -> str:
        tags_str = "、".join(article["tags"])
        has_repos = len(article["repos"]) > 0
        repos_info = f"关联仓库：{'、'.join([r['name'] for r in article['repos']])}" if has_repos else "暂无关联仓库"

        return f"本文涵盖{tags_str}领域，{repos_info}。文章提供了实用信息和参考价值，建议结合自身需求深入研究具体实现细节。"


def get_next_id(index_html: Path) -> int:
    if not index_html.exists():
        return 1
    content = index_html.read_text(encoding='utf-8')
    ids = re.findall(r'id:\s*(\d+)', content)
    return max([int(i) for i in ids]) + 1 if ids else 1


def article_to_js(article: Dict[str, Any], article_id: int) -> str:
    repos_json = json.dumps(article["repos"], ensure_ascii=False)
    key_points_json = json.dumps(article["keyPoints"], ensure_ascii=False)
    tags_json = json.dumps(article["tags"], ensure_ascii=False)

    return f"""
      {{
        id: {article_id},
        title: "{article['title']}",
        account: "{article['account']}",
        date: "{article['date']}",
        url: "{article['url']}",
        tags: {tags_json},
        summary: "{article['summary']}",
        keyPoints: {key_points_json},
        repos: {repos_json},
        evaluation: "{article['evaluation']}"
      }}"""


def update_index_html(article: Dict[str, Any]) -> bool:
    if not INDEX_HTML.exists():
        print(f"错误: {INDEX_HTML} 不存在")
        return False

    content = INDEX_HTML.read_text(encoding='utf-8')

    article_id = get_next_id(INDEX_HTML)
    new_article_js = article_to_js(article, article_id)

    new_article_js = new_article_js.strip()

    pattern = r'(\],;)'
    match = re.search(pattern, content)
    if match:
        new_content = content[:match.start()] + ",\n" + new_article_js + "\n    ];"
        INDEX_HTML.write_text(new_content, encoding='utf-8')
        print(f"✅ 文章已添加到 index.html (ID: {article_id})")
        return True
    else:
        print("错误: 无法找到 articles 数组结尾")
        return False


def git_commit() -> bool:
    try:
        subprocess.run(["git", "add", "wechat_articles/index.html"],
                       cwd=PROJECT_ROOT, check=True, capture_output=True)

        commit_msg = f"feat(article): 收录新文章 - 《{sys.argv[1][:50]}...》"

        result = subprocess.run(["git", "commit", "-m", commit_msg],
                               cwd=PROJECT_ROOT, capture_output=True, text=True)

        if result.returncode == 0:
            print(f"✅ Git commit 成功")
            print(f"   提交信息: {commit_msg}")
            return True
        else:
            if "nothing to commit" in result.stderr.lower():
                print("ℹ️ 没有需要提交的更改")
                return True
            print(f"⚠️ Git commit 失败: {result.stderr}")
            return False
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Git 命令执行失败: {e}")
        return False
    except FileNotFoundError:
        print("⚠️ Git 未安装或不在 PATH 中")
        return False


def print_article_summary(article: Dict[str, Any], article_id: int):
    print("\n" + "="*60)
    print(f"📄 文章 #{article_id} 收录完成")
    print("="*60)
    print(f"标题: {article['title']}")
    print(f"公众号: {article['account']}")
    print(f"日期: {article['date']}")
    print(f"标签: {', '.join(article['tags'])}")
    print(f"摘要: {article['summary'][:100]}...")
    print(f"要点数: {len(article['keyPoints'])}")
    if article['repos']:
        print(f"仓库: {', '.join([r['name'] for r in article['repos']])}")
    print("="*60 + "\n")


def main():
    if len(sys.argv) < 2:
        print("用法: python collect_article.py <文章URL>")
        print("示例: python collect_article.py https://mp.weixin.qq.com/s/xxxxx")
        sys.exit(1)

    url = sys.argv[1]

    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    print(f"🔍 正在抓取文章: {url}")

    collector = ArticleCollector(url)
    html = collector.fetch_content()

    if not html:
        print("\n❌ 无法获取文章内容")
        print("请尝试:")
        print("1. 确保链接可从公网访问")
        print("2. 微信公众号可能需要登录，请复制全文内容")
        sys.exit(1)

    print("📝 正在解析文章...")
    article = collector.parse_article(html)
    article["evaluation"] = collector.generate_evaluation(article)

    print_article_summary(article, get_next_id(INDEX_HTML))

    if update_index_html(article):
        git_commit()
        print("\n✨ 完成！更改已提交到本地仓库")
        print("💡 执行 'git push' 将更改推送到远程仓库")
    else:
        print("\n❌ 更新失败")
        sys.exit(1)


if __name__ == "__main__":
    main()
