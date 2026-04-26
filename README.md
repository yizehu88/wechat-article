# 📚 公众号文章收藏索引 (WeChat Article Collection)

> **量化交易 · 金融AI · 开源工具** — 专业的微信公众号文章收藏与索引系统，支持文章摘要展示、标签筛选、GitHub仓库一键直达

![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-部署成功-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.11+-yellow?style=flat-square)
![Last Update](https://img.shields.io/badge/更新时间-2026--04--24-orange?style=flat-square)

## ✨ 项目简介

本项目是一个**纯前端静态网站**，用于系统化地收藏、整理和展示微信公众号中的高质量技术文章，重点关注：

- 🔬 **AI/大模型**：金融LLM、多智能体系统、深度学习应用
- 📊 **量化交易**：策略开发、回测框架、技术指标
- 💰 **金融数据**：市场行情、基本面分析、风险管理
- 🛠️ **开源工具**：开发者工具、部署方案、效率提升

每篇文章都包含：**标题摘要 + 核心要点 + 关联GitHub仓库 + 个人评价**，帮助快速了解文章价值并找到相关代码资源。

---

## 🎯 核心功能

### 1️⃣ **智能卡片式展示**
- 🎴 **折叠/展开设计**：默认显示摘要，点击展开查看完整详情
- 🏷️ **多维标签系统**：支持按主题分类筛选（AI/大模型、量化框架、工具等）
- 🔍 **全文搜索**：支持搜索标题、项目名、关键词
- 📊 **实时统计**：显示总文章数、仓库数、当前可见数量

### 2️⃣ **丰富的文章信息**
- 📝 **基本信息**：公众号名称、作者、发布日期、原文链接
- 🎯 **核心要点**：提炼文章的5-8个关键知识点
- 📦 **关联仓库**：直接链接到相关GitHub项目，显示本地路径和Clone状态
- 💡 **个人评价**：与实际项目的关联度分析和使用建议

### 3️⃣ **优秀的用户体验**
- 🌙 **暗色主题**：护眼的深色界面，适合长时间阅读
- 📱 **响应式设计**：完美适配桌面端、平板和手机
- ⚡ **流畅动画**：折叠展开、筛选过滤都有平滑过渡效果
- 🔄 **批量操作**：支持一键全部展开/全部折叠
- ⬆️ **回到顶部**：滚动后自动显示返回顶部按钮

### 4️⃣ **自动化部署**
- 🚀 **GitHub Actions CI/CD**：推送到main分支自动触发部署
- 🌐 **GitHub Pages托管**：零成本托管静态网站
- ⏱️ **快速构建**：自动化流程，无需手动操作

---

## 🛠️ 技术栈

| 技术 | 版本 | 用途 |
|------|------|------|
| **HTML5** | - | 页面结构和语义化标记 |
| **CSS3** | - | 样式设计、响应式布局、动画效果 |
| **JavaScript (ES6+)** | - | 业务逻辑、DOM操作、事件处理 |
| **GitHub Pages** | - | 静态网站托管服务 |
| **GitHub Actions** | v4 | 自动化CI/CD部署流程 |

### 技术特点
- ✅ **零依赖**：无需任何前端框架或构建工具
- ✅ **轻量级**：单文件HTML，加载速度快
- ✅ **SEO友好**：语义化HTML结构
- ✅ **可维护性高**：代码结构清晰，注释完整

---

## 📁 项目结构

```
wechat-article/
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Actions自动部署配置
├── wechat_articles/
│   ├── index.html              # 主页面（包含所有HTML/CSS/JS代码）
│   └── runtime.txt             # Python版本要求文件（3.11.12）
├── README.md                   # 项目说明文档
├── LICENSE                     # MIT开源许可证
└── test_connection.md          # Git连接测试文件
```

### 目录说明

#### `wechat_articles/` - 主程序目录
- **[index.html](wechat_articles/index.html)**：项目的核心文件，包含完整的页面结构、样式和交互逻辑
  - HTML部分（第1-696行）：页面骨架和语义化标记
    - Header区域：项目标题和副标题
    - Toolbar工具栏：搜索框 + 标签筛选按钮
    - 统计栏：文章总数、仓库数统计
    - 文章卡片容器：动态渲染的文章列表
    - Footer页脚：更新时间和数据来源
    
  - CSS部分（第8-610行）：暗色主题样式系统
    - CSS变量定义（`:root`）：统一管理颜色、字体、间距
    - 暗色主题配色：`#0d1117`背景、`#e6edf3`文字、`#58a6ff`强调色
    - 响应式布局：`@media (max-width:600px)` 移动端适配
    - 动画效果：`transition` 实现平滑的折叠/展开动画
    - 卡片样式：`.article-card` 包含折叠视图和展开视图
    
  - JavaScript部分（第697-1174行）：业务逻辑和数据管理
    - 数据层：`articles` 数组存储13篇文章的完整信息
    - 渲染函数：`renderArticles()` 动态生成卡片DOM
    - 筛选逻辑：`filterCards()` 支持标签组合筛选和全文搜索
    - 交互控制：`toggleCard()` / `expandAll()` / `collapseAll()`
    - 标签系统：动态生成标签按钮并管理激活状态

#### `.github/workflows/deploy.yml` - CI/CD配置
- 触发条件：推送到 `main` 分支时自动执行
- 执行环境：Ubuntu最新版 (`ubuntu-latest`)
- 权限配置：
  - `contents: write` - 允许写入仓库内容
  - `pages: write` - 允许部署到GitHub Pages
  - `id-token: write` - 允许身份验证
- 构建步骤：
  1. 使用 `actions/checkout@v4` 拉取代码
  2. 使用 `actions/configure-pages@v4` 配置Pages环境
  3. 使用 `actions/upload-pages-artifact@v3` 上传 `wechat_articles/` 目录作为构建产物
  4. 使用 `actions/deploy-pages@v4` 自动部署到GitHub Pages

#### `runtime.txt` - Python版本要求
- 内容：`python-3.11.12`
- 说明：虽然项目是纯前端静态站点，但保留此文件以备未来可能的Python工具脚本扩展

---

## 🚀 快速开始

### 方式一：在线访问（推荐）

直接访问GitHub Pages托管的网站：
👉 **https://yizehu88.github.io/wechat-article/**

### 方式二：本地运行

1. **克隆仓库**
   ```bash
   git clone https://github.com/yizehu88/wechat-article.git
   cd wechat-article
   ```

2. **本地预览**
   
   方法A：直接打开HTML文件
   ```bash
   # Windows
   start wechat_articles/index.html
   
   # macOS
   open wechat_articles/index.html
   
   # Linux
   xdg-open wechat_articles/index.html
   ```
   
   方法B：使用本地服务器（推荐）
   ```bash
   # Python 3
   cd wechat_articles
   python -m http.server 8080
   
   # 然后在浏览器打开 http://localhost:8080
   
   # Node.js (需要安装http-server)
   npx http-server wechat_articles -p 8080
   ```

3. **开始浏览**
   - 使用顶部搜索框输入关键词
   - 点击标签按钮进行筛选
   - 点击文章卡片展开查看详情
   - 点击"阅读原文"跳转到微信文章
   - 点击GitHub链接访问相关代码仓库

---

## 📝 如何添加新文章

### 方法：手动编辑 `index.html`

1. 打开 [wechat_articles/index.html](wechat_articles/index.html) 文件

2. 找到JavaScript部分的 `articles` 数组（约第699行）

3. 在数组末尾添加新的文章对象，格式如下：

```javascript
{
  id: 14,  // 文章ID（递增，当前最大为13）
  title: "文章标题",
  account: "公众号名称",
  author: "作者姓名",  // 可选字段
  date: "2026-04-26",  // 发布日期 YYYY-MM-DD 格式
  url: "https://mp.weixin.qq.com/s/xxxxx",  // 原文完整链接
  tags: ["AI/大模型", "量化框架"],  // 标签列表（从现有标签中选择或新建）
  summary: "文章摘要，一两句话概括主要内容",  // 显示在卡片上的简介（建议50-100字）
  keyPoints: [
    "核心要点1",
    "核心要点2",
    "核心要点3"
    // 建议5-8个要点，每个要点30-60字
  ],
  repos: [
    {
      name: "项目名称",
      github: "https://github.com/user/repo",  // GitHub完整地址
      localPath: "../本地路径",  // 本地克隆相对路径（如无可填"—"）
      status: "ok",  // "ok"表示已clone到本地，"pending"表示待clone
      stars: "10k+"  // Star数量（可选，如未知可留空""）
    }
    // 一篇文章可关联多个仓库
  ],
  evaluation: "与我的项目关联度评价和使用建议"  // 可选字段，个人分析评价
}
```

4. **保存文件并提交**

```bash
git add wechat_articles/index.html
git commit -m "docs: 添加新文章 - 《文章标题》"
git push origin main
```

5. **等待自动部署**

GitHub Actions会在1-2分钟内自动完成构建和部署，刷新网站即可看到新文章。

### 标签规范

建议使用的标准标签（已内置颜色映射）：

| 标签 | 颜色类别 | 适用场景 |
|------|----------|----------|
| **AI/大模型** | 蓝色 (`tag-ai`) | LLM、深度学习、NLP、Transformer等 |
| **量化框架** | 黄色 (`tag-quant`) | 回测系统、交易平台、策略引擎、技术指标 |
| **金融数据** | 绿色 (`tag-financial`) | 行情API、基本面数据、财务指标、另类数据 |
| **期货CTP** | 蓝色 (`tag-futures`) | 期货交易、CTP接口、SIMNOW仿真 |
| **工具** | 灰色 (`tag-tool`) | 开发工具、效率提升、部署方案、IM通讯 |
| **开源项目** | 灰色 (`tag-tool`) | GitHub开源项目介绍和评测 |
| **智能体** | 蓝色 (`tag-ai`) | AI Agent、多智能体系统、AutoGPT等 |
| **交易心理** | 绿色 (`tag-financial`) | 投资心理学、行为金融、概率思维 |
| **风险管理** | 黄色 (`tag-quant`) | 仓位管理、止损止盈、风控规则、组合优化 |
| **策略优化** | 黄色 (`tag-quant`) | 参数优化、过拟合防范、回测改进 |
| **架构设计** | 黄色 (`tag-quant`) | 系统架构、设计模式、微服务 |
| **LLM** | 紫色 (`tag-llm`) | 大语言模型应用、Prompt工程 |
| **形态识别** | 黄色 (`tag-quant`) | K线形态、杯柄形态、头肩顶等 |

---

## 🎨 界面预览

### 主要区域布局

```
┌─────────────────────────────────────────────┐
│  📚 公众号文章收藏索引                        │  ← Header区域
│  量化交易·金融AI·开源工具                    │
├─────────────────────────────────────────────┤
│ [🔍 搜索框] [标签1][标签2]... [✕清除筛选]     │  ← Toolbar工具栏
├─────────────────────────────────────────────┤
│ 共 13 篇文章 · 5 个仓库 · 当前显示 13 篇      │  ← 统计栏
│ [📂 全部展开] [📁 全部折叠]                   │  ← 批量操作
├─────────────────────────────────────────────┤
│ ┌─────────────────────────────────────────┐ │
│ │ #1 Kronos：重塑金融市场的语言模型    ▼   │ │  ← 折叠视图
│ │ 📝 AI探秘人 · 静弦心 · 2026-04-11        │ │
│ │ [AI/大模型] [金融时序] [LLM]             │ │
│ │ 首个开源金融K线基础模型（AAAI 2026...    │ │
│ │ 📦 1 个仓库 · 点击查看详情 ↓             │ │
│ ├─────────────────────────────────────────┤ │
│ │ [🔗 阅读原文] [⭐ 打开Kronos GitHub]     │ │  ← 展开视图
│ │ • 核心创新：专用分词器+自回归Transformer  │ │
│ │ • 训练规模：45家全球交易所...            │ │
│ │ ...                                      │ │
│ │ 📦 关联仓库表格                           │ │
│ │ 💡 与我的回测系统关联度：高度相关！        │ │
│ └─────────────────────────────────────────┘ │
│ ...更多文章卡片...                            │
├─────────────────────────────────────────────┤
│ 最后更新: 2026-04-24 · 数据来源: 微信公众号   │  ← Footer页脚
└─────────────────────────────────────────────┘
                              [↑]              ← 回到顶部按钮
```

### 卡片结构详解

**折叠视图**（始终可见）：
- **序号标识**：圆形徽章显示文章编号
- **文章标题**：加粗显示，字号17px
- **发布信息**：公众号名、作者（可选）、发布日期
- **标签徽章**：彩色圆角标签，不同分类不同颜色
- **文章摘要**：最多显示2行，超出省略号截断
- **仓库提示**：显示关联仓库数量
- **展开图标**：▼箭头指示可点击展开

**展开视图**（点击后显示，平滑动画）：
- **操作按钮栏**：
  - 蓝色主按钮："🔗 阅读原文"（跳转微信文章）
  - 灰色次按钮："⭐ 打开 XXX GitHub"（跳转GitHub仓库）
- **核心要点列表**：无序列表展示5-8个关键点
- **关联仓库表格**：4列（名称、GitHub地址、本地路径、Clone状态）
  - 状态徽章：✅ 已Clone（绿色）/ ⏳ 待Clone（橙色）
  - Star数量显示在项目名下方
- **个人评价框**：蓝色左边框的评价区块（可选）

---

## ⚠️ 项目约束与限制

### 🔒 技术约束

#### 1. **纯静态站点架构**
- ❌ **无后端服务器**：不涉及Node.js/Python/PHP等服务端运行时
- ❌ **无数据库支持**：无法使用MySQL/MongoDB/SQLite等数据库
- ✅ **数据硬编码**：所有文章数据存储在JavaScript数组中
- **影响范围**：
  - 每次添加/修改/删除文章都必须手动编辑HTML源码
  - 无法实现用户注册登录、权限管理等动态功能
  - 不支持服务端数据处理（如数据聚合、统计分析API）
- **适用场景**：个人博客、文档站、作品集等低频更新场景
- **不适用场景**：社交平台、电商系统、内容管理系统等需要动态数据的场景

#### 2. **单文件架构限制**
- **当前实现**：所有代码（HTML+CSS+JS≈1200行）集中在单个 `index.html` 文件
- **性能影响**：
  - 文件大小随文章数量线性增长（目前13篇约100KB）
  - 首屏加载时间会增加（浏览器需解析完整DOM）
  - 浏览器内存占用持续上升
- **维护挑战**：
  - 多人协作时容易产生代码冲突
  - 代码审查困难（文件过长）
  - 版本对比效率低（每次改动都涉及同一文件）
- **建议阈值**：
  - ⚠️ 文章数 < 30篇：当前架构可接受
  - ⚠️ 文章数 30-50篇：建议拆分为独立JSON数据文件
  - ❌ 文章数 > 50篇：强烈建议重构为多文件架构或引入前端框架

#### 3. **无用户认证与权限系统**
- **缺失功能**：
  - 无注册/登录表单
  - 无Session/Cookie/Token管理
  - 无角色权限控制（管理员/普通用户/访客）
  - 无个人信息设置页面
- **安全影响**：
  - 所有内容公开可见，无法设置私密文章
  - 无法追踪用户行为（阅读历史、收藏记录）
  - 无法实现评论系统的用户身份验证
- **替代方案**（如需认证）：
  - 使用GitHub OAuth（适合开发者社区）
  - 使用Firebase Authentication（免费额度充足）
  - 使用Auth0/Supabase Auth（企业级方案）

#### 4. **单向信息流设计**
- **缺失互动功能**：
  - ❌ 无评论系统（无法对文章发表看法）
  - ❌ 无点赞/收藏功能（无法表达喜好）
  - ❌ 无分享功能（无法生成分享卡片或二维码）
  - ❌ 无订阅通知（无法接收新文章推送）
- **用户体验影响**：
  - 缺乏社区氛围和用户粘性
  - 无法收集读者反馈改进内容质量
  - 信息传播依赖用户手动复制链接
- **可行增强方向**：
  - 集成Giscus（基于GitHub Discussions的评论系统）
  - 使用Umami/Plausible做访问统计（隐私友好）
  - 添加Web Share API实现原生分享功能

### ⚙️ 功能限制

#### 5. **客户端搜索的局限性**
- **当前实现**：基于字符串匹配的简单搜索
  ```javascript
  const searchMatch = !query || searchText.includes(query);
  ```
- **不支持的高级特性**：
  - ❌ **模糊搜索**：输入"kronos"无法匹配"Kronos"（大小写敏感）
  - ❌ **拼音搜索**：输入"jlqt"无法匹配"量化交易"
  - ❌ **语义搜索**：输入"金融AI"无法匹配"重塑金融市场"
  - ❌ **分词搜索**：输入"金融 LLM"无法匹配同时包含两个词的文章
  - ❌ **搜索高亮**：匹配的关键词不会高亮显示
  - ❌ **搜索历史**：无法记住之前的搜索词
- **性能问题**：
  - 每次输入都遍历所有文章的所有字段（O(n*m)复杂度）
  - 文章数量超过100篇时可能出现明显延迟
- **优化方案**：
  - 引入Fuse.js（轻量级模糊搜索库，<10KB）
  - 使用Lunr.js（全文搜索引擎，支持中文分词）
  - 使用Elasticsearch/Algolia（云端搜索服务）

#### 6. **标签系统的简化设计**
- **当前实现的局限**：
  - 标签需要在JavaScript代码中手动维护 `allTags` 和 `tagColorMap`
  - 新增标签必须同步修改两处：数据数组 + 颜色映射对象
  - 无标签层级结构（如：量化 > 技术指标 > 趋势指标）
  - 无标签云可视化（Tag Cloud）
  - 无标签热度统计（哪些标签下文章最多）
  - 无标签自动推荐（根据文章内容智能打标签）
- **数据一致性风险**：
  ```javascript
  // 如果忘记在这里添加新标签
  const tagColorMap = {
    "AI/大模型": "tag-ai",
    // 缺少 "新标签": "tag-xxx"
  };
  // 那么新标签会显示为无颜色的默认样式
  ```
- **改进建议**：
  - 从文章数据自动提取标签集合（`[...new Set(articles.flatMap(...))]`）
  - 为未定义标签提供默认颜色（已在代码中实现：`return tagColorMap[tag] || ""`）
  - 添加标签管理界面（仅管理员可见）

#### 7. **数据导入导出的缺失**
- **无法批量导入**：
  - ❌ 不支持从CSV/Excel/Notion批量导入文章
  - ❌ 不支持从其他平台迁移（如知乎收藏、CSDN bookmark）
  - ❌ 不支持API接口自动抓取（如微信RSS、公众号文章抓取）
  - ❌ 不支持浏览器插件一键收藏
- **无法数据导出**：
  - ❌ 无法导出为PDF（打印友好的文档格式）
  - ❌ 无法导出为Markdown（方便在其他平台发布）
  - ❌ 无法导出为JSON（程序化处理或备份）
  - ❌ 无法导出为CSV（Excel表格分析）
- **实际痛点**：
  - 迁移到其他平台时需要逐条手工复制
  - 备份只能通过Git版本控制（不够直观）
  - 无法离线查看或在其他设备上同步

#### 8. **移动端体验的妥协**
- **响应式设计的局限性**：
  - 复杂表格在小屏幕上需要横向滚动（仓库表格有4列）
  - 长文章卡片在手机上需要大量滚动（展开后有要点+表格+评价）
  - 工具栏在窄屏下换行较多（搜索框+多个标签按钮+清除按钮）
  - 批量操作按钮在移动端可能误触
- **缺少的移动端优化**：
  - ❌ 无触摸手势支持（左滑删除、右滑收藏）
  - ❌ 无底部导航栏（移动端标准交互模式）
  - ❌ 无PWA支持（无法添加到主屏幕、离线访问）
  - ❌ 无App-like体验（全屏模式、启动画面）
- **测试覆盖不足**：
  - 未在真实移动设备上全面测试（iPhone SE、iPad、Android手机）
  - 未考虑横屏模式的布局调整
  - 未考虑Safe Area（刘海屏、底部横条）的适配

### 🏗️ 运维约束

#### 9. **强依赖GitHub基础设施**
- **依赖链条**：
  ```
  本地Git → GitHub仓库 → GitHub Actions → GitHub Pages → 用户浏览器
  ```
- **单点故障风险**：
  - ⚠️ GitHub服务宕机（历史上发生过多次 outage）
  - ⚠️ GitHub Actions构建失败（配额超限、依赖版本冲突）
  - ⚠️ GitHub Pages部署失败（域名DNS问题、SSL证书过期）
  - ⚠️ 仓库被恶意攻击（supply chain attack、账号被盗）
- **服务级别协议（SLA）**：
  - GitHub承诺99.95%可用性（每月约停机22分钟）
  - 免费账户无SLA保障，商业账户有99.99%
  - 国内访问速度可能较慢（需考虑CDN加速）
- **降级方案**：
  - 同时部署到Gitee Pages（国内访问更快）
  - 使用Cloudflare Pages/Vercel作为备用托管
  - 定期导出静态文件备份到云存储（OSS/S3）

#### 10. **域名与品牌限制**
- **默认域名格式**：
  ```
  https://yizehu88.github.io/wechat-article/
  ```
- **存在的问题**：
  - 域名过长，不易记忆和传播
  - `.github.io` 子域名显得不够专业
  - SEO权重低于顶级域名（com/cn/io）
  - 无法自定义邮箱域名（如 admin@wechat-article.com）
- **自定义域名方案**：
  - 购买域名（如 `wechat-article.dev` 或 `article-index.cn`）
  - 配置DNS CNAME记录指向GitHub Pages
  - 申请SSL证书（Let's Encrypt免费证书）
  - 成本：域名约 $10-50/年，完全可接受
- **权衡考虑**：
  - 个人项目用默认域名足够（省钱省事）
  - 商业项目或希望建立品牌建议购买自定义域名

#### 11. **更新频率与工作流瓶颈**
- **当前工作流耗时**：
  ```
  编辑HTML → 本地测试 → git add → git commit → git push → 等2分钟部署 → 刷新验证
  总计：约 5-10 分钟/次
  ```
- **高频更新的障碍**：
  - 每天更新 > 3篇时，工作流变得繁琐
  - 无法快速修正错误（如错别字、链接失效）
  - 团队协作时容易出现合并冲突
  - 移动端无法编辑提交（需要电脑）
- **不适合的场景**：
  - 新闻聚合类网站（需要实时更新）
  - 用户生成内容（UGC）平台（需要即时发布）
  - 协作编辑环境（多人同时编辑同一文件）
- **优化方向**：
  - 使用GitHub Web Editor在线编辑（无需本地环境）
  - 使用Headless CMS（如Strapi、Contentful）分离内容和展示
  - 开发浏览器书签工具或Chrome插件一键收藏

#### 12. **版本控制策略的缺失**
- **当前实践**：
  - 所有修改都在 `main` 分支上直接提交
  - 无功能分支（feature branch）
  - 无预发布环境（staging/preview）
  - 无语义化版本号（Semantic Versioning）
- **潜在风险**：
  - 推送错误代码直接影响线上环境（无测试环节）
  - 无法并行开发多个功能（串行等待）
  - 回滚困难（只能revert commit或reset到历史版本）
  - 无法追溯某个功能是在哪个版本引入的
- **推荐的Git工作流**：
  ```
  main（生产环境，受保护）
   └── develop（开发环境）
        ├── feature/add-search-highlight
        ├── feature/dark-mode-toggle
        └── fix/typo-in-article-5
  
  工作流程：
  1. 从develop创建feature分支
  2. 本地开发和测试
  3. 提交Pull Request到develop
  4. Code Review通过后合并
  5. 从develop创建Release PR到main
  6. 合并后自动部署到生产环境
  ```

### 📚 内容约束

#### 13. **文章来源单一性**
- **当前支持的平台**：
  - ✅ 微信公众号（mp.weixin.qq.com）
- **不支持的平台**：
  - ❌ 知乎专栏（zhuanlan.zhihu.com）
  - ❌ CSDN博客（blog.csdn.net）
  - ❌ 掘金社区（juejin.cn）
  - ❌ 博客园（cnblogs.com）
  - ❌ Medium（medium.com）
  - ❌ 个人博客（自定义域名）
- **扩展难度评估**：
  - 低难度：调整 `url` 字段的校验规则（正则表达式）
  - 中难度：添加平台图标和来源筛选功能
  - 高难点：不同平台的文章结构差异大（摘要提取、正文解析）
- **数据结构调整建议**：
  ```javascript
  {
    // 当前
    url: "https://mp.weixin.qq.com/s/xxxxx",
    
    // 建议
    source: {
      platform: "wechat",  // wechat/zhihu/csdn/juejin/custom
      url: "https://mp.weixin.qq.com/s/xxxxx",
      originalId: "s_xxxx",  // 平台内的唯一标识
      favicon: "https://res.wx.qq.com/favicon.ico"  // 平台图标
    }
  }
  ```

#### 14. **语言与国际化限制**
- **当前支持的语言**：
  - ✅ 中文简体（界面UI）
  - ✅ 中文简体（文章内容）
  - ✅ 英文（代码和技术术语）
- **不支持的语言**：
  - ❌ 英语（英文界面和英文文章）
  - ❌ 繁体中文（港澳台用户）
  - ❌ 日语/韩语（亚洲其他地区）
  - ❌ 其他欧洲语言（法语、德语、西班牙语等）
- **国际化（i18n）工作量估算**：
  - UI文案翻译：约50条字符串，工作量 2-4小时
  - 日期格式适配：`2026-04-26` vs `04/26/2026` vs `26.04.2026`
  - 布局方向：阿拉伯语/希伯来语需要RTL（从右到左）布局
  - 搜索分词：中文不需要空格分词，英文需要tokenize
- **是否需要国际化**：
  - 如果目标读者仅限国内量化圈 → 不需要
  - 如果希望吸引海外华人或国际用户 → 建议至少支持中英双语

#### 15. **版权与法律合规**
- **文章内容的版权归属**：
  - ✅ 原文版权归原作者和微信公众号运营者所有
  - ✅ 本项目仅做索引、摘要和短评整理（合理使用Fair Use）
  - ⚠️ 不拥有原文的任何版权
- **需要注意的法律风险**：
  - ⚠️ **转载权**：即使标注来源，大量转载仍可能侵权
  - ⚠️ **改编权**：摘录要点属于改编行为，需控制在合理范围内
  - ⚠️ **信息网络传播权**：提供原文链接通常被视为合法引用
  - ⚠️ **名誉权**：负面评价可能构成诽谤（注意评价措辞）
- **合规建议**：
  - 每篇文章都提供原始链接（已实现）
  - 摘要控制在200字以内（避免大段复制）
  - 明确声明"文章版权归原作者所有"（建议在Footer添加）
  - 收到版权投诉后24小时内移除相关内容（DMCA合规）
  - 联系公众号作者获得书面授权（最佳实践）

---

## 🔧 开发指南

### 本地开发环境搭建

**必需工具**：
- ✅ Git（版本控制系统，建议2.30+）
- ✅ 现代文本编辑器（VS Code推荐，安装Live Server插件）
- ✅ 现代浏览器（Chrome 90+/Firefox 88+/Safari 14+/Edge 90+）

**可选工具**：
- 🔧 Python 3.x（用于启动本地HTTP服务器）
- 🔧 Node.js 16+（用于npm包管理和高级构建工具）
- 🔧 VS Code插件：
  - Live Server（实时刷新预览）
  - Prettier（代码格式化）
  - Markdown Preview Enhanced（README预览）

### 推荐的开发工作流（Git Flow）

```bash
# 1. 确保在main分支且是最新的
git checkout main
git pull origin main

# 2. 创建功能分支（命名规范：feature/类型-简要描述）
git checkout -b feature/article-kronos-llm

# 3. 使用VS Code编辑 wechat_articles/index.html
#    - 在 articles 数组中添加新文章对象
#    - 保存后Live Server自动刷新浏览器
#    - 测试搜索、筛选、展开/折叠等功能

# 4. 本地测试清单
#    □ 新文章正确显示在列表末尾
#    □ 标签颜色正确（检查tagColorMap是否有对应项）
#    □ 点击卡片能正常展开/折叠
#    □ "阅读原文"链接能跳转到正确的微信文章
#    □ GitHub仓库链接能正确打开
#    □ 搜索框输入关键词能找到该文章
#    □ 点击该文章的标签能筛选出来
#    □ 移动端响应式布局正常（F12切换设备模拟器）
#    □ 不同浏览器兼容性（Chrome/Firefox/Safari）

# 5. 提交更改（遵循Conventional Commits规范）
git add wechat_articles/index.html
git commit -m "feat(article): 添加Kronos金融LLM文章"

# 6. 推送功能分支到远程
git push origin feature/article-kronos-llm

# 7. 在GitHub上创建Pull Request
#    - Title: feat: 添加Kronos金融LLM文章
#    - Description:
#      ## 变更内容
#      - 新增文章 #14：Kronos：重塑金融市场的语言模型
#      - 来源：AI探秘人公众号
#      - 标签：AI/大模型、金融时序、LLM
#      
#      ## 测试结果
#      - [x] Chrome 100 通过
#      - [x] Firefox 98 通过
#      - [x] Safari 15 通过
#      - [x] iPhone SE 模拟器通过
#      
#      ## 截图
#      （附上新文章卡片的截图）

# 8. Code Review通过后合并到main
#    （由项目负责人或自己合并）

# 9. 清理本地分支（可选）
git branch -d feature/article-kronos-llm
git pull origin main
```

### Commit Message 规范（Conventional Commits）

采用[Conventional Commits](https://www.conventionalcommits.org/)规范：

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Type 类型**：
- `feat`: 新功能（新增文章、添加功能模块）
- `fix`: 修复bug（修复显示错误、链接失效）
- `docs`: 文档变更（更新README、添加注释）
- `style`: 代码格式调整（不影响运行的代码风格变化）
- `refactor`: 重构（既不是新功能也不是bug修复的代码改动）
- `perf`: 性能优化（提升加载速度、减少内存占用）
- `test`: 添加测试（目前项目无测试框架，预留）
- `chore`: 构建/工具变动（更新依赖、修改配置文件）

**Scope 范围**：
- `article`: 文章数据相关
- `ui`: 界面样式相关
- `search`: 搜索功能相关
- `filter`: 筛选功能相关
- `deploy`: 部署配置相关
- `readme`: 文档相关

**示例**：
```bash
feat(article): 添加SSQuant量化框架文章

新增文章 #2：SSQuant(v0.4.3)基于SKILLS标准的量化交易智能体框架
来源：松鼠Quant公众号，包含24个策略示例和Flask AI Agent介绍

fix(ui): 修复移动端工具栏溢出问题

标签按钮过多时在窄屏设备上换行异常，
调整为flex-wrap并设置max-width限制

docs(readme): 更新项目约束说明文档

补充15项技术和运维约束的详细说明，包括影响范围和解决方案
```

### 代码风格指南

#### HTML规范
- 使用语义化标签（`<header>`, `<main>`, `<article>`, `<section>`, `<footer>`）
- 保持适当的缩进（2空格或4空格，保持一致）
- 属性顺序：class → id → data-* → src/href → title/alt → 其他
- 自闭合标签不加斜杠：`<br>` 而非 `<br />`
- 示例：
  ```html
  <article class="article-card" data-id="1" data-tags="ai,llm">
    <div class="card-summary">
      <h2 class="card-title">文章标题</h2>
    </div>
  </article>
  ```

#### CSS规范
- 使用CSS变量（Custom Properties）管理主题色彩
- 采用BEM命名规范（Block__Element--Modifier）
- 选择器嵌套不超过3层（避免性能问题）
- 使用rem/em单位而非px（便于响应式缩放）
- 示例：
  ```css
  :root {
    --accent-color: #58a6ff;
    --border-radius: 8px;
  }
  
  .article-card { /* Block */
    &__title { /* Element */
      font-size: 1.125rem;
      
      &--featured { /* Modifier */
        color: var(--accent-color);
      }
    }
  }
  ```

#### JavaScript规范
- 使用ES6+语法（const/let、箭头函数、模板字符串、解构赋值）
- 函数职责单一（每个函数只做一件事）
- 使用JSDoc注释添加函数说明
- 变量命名使用camelCase，常量使用UPPER_SNAKE_CASE
- 避免全局变量污染（使用IIFE或模块化）
- 示例：
  ```javascript
  /**
   * 根据标签筛选文章卡片
   * @param {Set<string>} activeTags - 当前激活的标签集合
   * @returns {void}
   */
  function filterCards(activeTags) {
    const cards = document.querySelectorAll('.article-card');
    
    cards.forEach(card => {
      const cardTags = card.dataset.tags.split(',');
      const isMatch = activeTags.size === 0 || 
                     [...activeTags].every(tag => cardTags.includes(tag));
      
      card.classList.toggle('hidden', !isMatch);
    });
    
    updateStats();
  }
  ```

### 性能优化建议

#### 当前性能基线（13篇文章）
- **文件大小**：~100KB（HTML+CSS+JS合并）
- **首屏加载时间**：< 1秒（本地）/ 1-2秒（GitHub Pages国内）
- **DOM节点数**：~500个（每篇文章约40个节点）
- **内存占用**：~5MB（Chrome DevTools测量）

#### 优化优先级矩阵

| 优化项 | 影响程度 | 实现难度 | 推荐时机 |
|--------|----------|----------|----------|
| 压缩HTML/CSS/JS | ⭐⭐ | ⭐ | 文件>200KB时 |
| 图片懒加载 | ⭐⭐⭐ | ⭐⭐ | 添加文章封面图时 |
| 虚拟滚动 | ⭐⭐⭐ | ⭐⭐⭐ | 文章>50篇时 |
| 分页加载 | ⭐⭐ | ⭐⭐ | 文章>100篇时 |
| CDN加速 | ⭐⭐⭐ | ⭐ | 国内访问慢时 |
| Service Worker缓存 | ⭐⭐ | ⭐⭐ | 需要离线支持时 |
| 代码分割 | ⭐⭐ | ⭐⭐⭐ | 引入框架后 |

#### 具体优化实施示例

**1. Gzip压缩（通过GitHub Pages自动启用）**
```html
<!-- 无需额外配置，GitHub Pages默认启用gzip -->
<!-- 可在Response Headers中看到：Content-Encoding: gzip -->
```

**2. 外部CSS/JS拆分（当文件>150KB时）**
```html
<!-- 将CSS抽取为独立文件 -->
<link rel="stylesheet" href="styles.css">

<!-- 将JS抽取为独立文件 -->
<script src="app.js"></script>

<!-- 优势：浏览器可以并行下载，利用缓存 -->
```

**3. 数据文件分离（当文章>30篇时）**
```javascript
// articles-data.js
const articles = [...]; // 纯数据，无逻辑

// app.js
import { articles } from './articles-data.js';
// 渲染逻辑...
```

**4. 懒加载非关键资源**
```javascript
// 使用Intersection Observer实现图片懒加载
const imageObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const img = entry.target;
      img.src = img.dataset.src;
      imageObserver.unobserve(img);
    }
  });
});

document.querySelectorAll('img[data-src]').forEach(img => {
  imageObserver.observe(img);
});
```

---

## 📈 未来规划（Roadmap）

### Phase 1：基础增强（短期，1-2周）

- [ ] **数据外部化**
  - [ ] 将 `articles` 数组抽取为独立的 `data/articles.json` 文件
  - [ ] 使用 `fetch()` API异步加载JSON数据
  - [ ] 添加加载状态指示器（Loading spinner）
  - [ ] **收益**：数据与视图分离，便于批量编辑和版本管理

- [ ] **搜索功能升级**
  - [ ] 引入 Fuse.js 库（~7KB gzipped）实现模糊搜索
  - [ ] 支持拼音首字母搜索（如 "jl" 匹配 "量化"）
  - [ ] 添加搜索关键词高亮显示
  - [ ] 添加搜索历史记录（localStorage持久化）
  - [ ] **收益**：大幅提升查找效率，用户体验显著改善

- [ ] **标签系统优化**
  - [ ] 显示每个标签下的文章数量（如 "AI/大模型 (5)"）
  - [ ] 添加标签热度排序（按文章数量降序）
  - [ ] 实现"显示更多/收起"标签折叠功能（已有按钮但未实现逻辑）
  - [ ] **收益**：标签栏更整洁，热门标签更易发现

### Phase 2：交互增强（中期，2-4周）

- [ ] **文章收藏功能**
  - [ ] 使用 localStorage 存储收藏状态
  - [ ] 添加"❤️ 收藏"按钮（切换收藏状态）
  - [ ] 新增"我的收藏"筛选视图
  - [ ] 添加收藏数量统计
  - [ ] **收益**：用户可以标记重要文章，二次访问更便捷

- [ ] **阅读进度跟踪**
  - [ ] 记录每篇文章的展开/折叠状态（localStorage）
  - [ ] 记录上次访问时间
  - [ ] 显示"最近阅读"列表
  - [ ] 标记"已读"/"未读"状态
  - [ ] **收益**：断点续读，避免重复查看相同内容

- [ ] **分享功能增强**
  - [ ] 集成 Web Share API（原生分享菜单）
  - [ ] 生成分享卡片图片（使用 html2canvas）
  - [ ] 复制文章链接到剪贴板（一键复制）
  - [ ] 生成微博/ Twitter分享文案
  - [ ] **收益**：便于社交媒体传播，提高项目知名度

- [ ] **暗色/亮色主题切换**
  - [ ] 添加主题切换按钮（🌙/☀️）
  - [ ] 定义两套CSS变量（light/dark theme）
  - [ ] 使用 localStorage 记住用户偏好
  - [ ] 尊重系统偏好（prefers-color-scheme）
  - [ ] **收益**：白天使用亮色更舒适，夜间使用暗色护眼

### Phase 3：架构升级（长期，1-2月）

- [ ] **引入前端框架（Vue 3 / React 18）**
  - [ ] 组件化拆分（ArticleCard、SearchBar、TagFilter、StatsBar）
  - [ ] 状态管理（Pinia / Redux Toolkit / Zustand）
  - [ ] 路由管理（Vue Router / React Router）（如需多页面）
  - [ ] 构建工具（Vite / Webpack 5）
  - [ ] **收益**：代码可维护性大幅提升，开发效率提高50%+

- [ ] **后端 API 服务（Node.js / Python Flask）**
  - [ ] RESTful API 设计（CRUD文章接口）
  - [ ] 数据库集成（SQLite / PostgreSQL / MongoDB）
  - [ ] 用户认证系统（JWT / OAuth2）
  - [ ] 管理后台界面（文章增删改查）
  - [ ] **收益**：支持动态内容管理，可实现UGC和多用户协作

- [ ] **PWA 支持（Progressive Web App）**
  - [ ] 注册 Service Worker（Workbox）
  - [ ] 实现离线缓存策略（Cache-first / Network-first）
  - [ ] 添加 manifest.json（应用图标、启动画面、主题色）
  - [ ] 支持"添加到主屏幕"（A2HS）
  - [ ] 推送通知（新文章上线提醒）
  - [ ] **收益**：类原生应用体验，可离线访问，提高用户留存率

### Phase 4：生态扩展（远期，3-6月）

- [ ] **多平台支持**
  - [ ] 支持知乎、CSDN、掘金、Medium等平台文章
  - [ ] 统一的数据模型和解析器（Adapter Pattern）
  - [ ] 平台图标和来源筛选功能
  - [ ] **收益**：打破微信公众号单一来源限制，内容更丰富

- [ ] **评论与互动系统**
  - [ ] 集成 Giscus（基于 GitHub Discussions）
  - [ ] 或使用 utterances（轻量级替代方案）
  - [ ] 支持点赞/踩（ reactions 功能）
  - [ ] @提及用户和消息通知
  - [ ] **收益**：建立社区氛围，促进知识交流

- [ ] **智能化功能**
  - [ ] AI 自动生成文章摘要（调用 OpenAI / Claude API）
  - [ ] 智能标签推荐（基于TF-IDF或BERT embedding）
  - [ ] 相似文章推荐（协同过滤或内容-based推荐）
  - [ ] 个性化排序（根据用户阅读历史调整展示顺序）
  - [ ] **收益**：降低人工维护成本，提升内容发现效率

- [ ] **数据分析与可视化**
  - [ ] 文章阅读量统计（Umami / Plausible）
  - [ ] 标签分布饼图（Chart.js / ECharts）
  - [ ] 时间线视图（按月份展示文章发布趋势）
  - [ ] 热门文章排行榜（Top 10 Most Viewed）
  - [ ] 导出报告（PDF / Excel）
  - [ ] **收益**：数据驱动的内容策略优化

---

## 🤝 贡献指南

欢迎对本项目提出改进建议和贡献代码！

### 如何贡献代码

1. **Fork 本仓库**
   ```
   点击 GitHub 页面右上角的 "Fork" 按钮
   → 复制一份到你自己的 GitHub 账户下
   ```

2. **克隆你的 Fork 到本地**
   ```bash
   git clone https://github.com/YOUR_USERNAME/wechat-article.git
   cd wechat-article
   ```

3. **创建新的功能分支**
   ```bash
   # 命名规范：type/issue-number-short-description
   git checkout -b feature/42-add-fuzzy-search
   ```

4. **进行开发和测试**
   - 安装 VS Code 和推荐插件
   - 使用 Live Server 启动本地预览
   - 编写代码并充分测试
   - 确保代码符合项目风格指南

5. **提交你的更改**
   ```bash
   git add .
   git commit -m "feat(search): 添加Fuse.js模糊搜索支持"
   ```

6. **推送到你的 Fork**
   ```bash
   git push origin feature/42-add-fuzzy-search
   ```

7. **创建 Pull Request**
   - 在 GitHub 上进入你的 Fork 仓库
   - 点击 "New Pull Request" 按钮
   - 选择目标分支：`main`
   - 填写 PR 模板：
     
     **PR 标题**：`feat: 添加模糊搜索功能`
     
     **PR 描述**：
     ## 相关 Issue
     Closes #42
     
     ## 变更类型
     - [x] ✨ 新功能 (feature)
     - [ ] 🐛 Bug 修复 (bugfix)
     - [ ] 📝 文档更新 (docs)
     - [ ] 🎨 样式调整 (style)
     
     ## 变更说明
     - 引入 Fuse.js 库（7KB gzipped）替换原有的字符串匹配搜索
     - 支持模糊匹配、拼音搜索、关键词高亮
     - 添加搜索历史记录（localStorage，最多保存20条）
     
     ## 测试环境
     - [x] Chrome 100 (Windows)
     - [x] Firefox 98 (macOS)
     - [x] Safari 15 (iOS)
     - [x] Android Chrome
     
     ## 截图
     （粘贴搜索前后的对比截图）
     
     ## Checklist
     - [x] 代码符合项目风格指南
     - [x] 已在本地充分测试
     - [x] 无 console.error 或 warning
     - [x] 移动端响应式正常
     - [x] 已更新 README 文档（如有必要）

8. **等待 Code Review 和合并**
   - 维护者会在1-3天内审核你的PR
   - 可能会要求修改一些细节（请及时响应）
   - 审核通过后会合并到 `main` 分支
   - GitHub Actions 会自动部署到生产环境

### 贡献类型示例

| 类型 | 图标 | 示例 | 难度 |
|------|------|------|------|
| **Bug 修复** | 🐛 | 修复Safari浏览器卡片展开动画闪烁 | ⭐ |
| **新功能** | ✨ | 添加文章收藏功能（localStorage） | ⭐⭐ |
| **文档完善** | 📝 | 补充API文档和使用示例 | ⭐ |
| **UI 改进** | 🎨 | 优化移动端工具栏布局 | ⭐⭐ |
| **性能优化** | ⚡ | 实现虚拟滚动（文章>50篇时） | ⭐⭐⭐ |
| **国际化** | 🌍 | 添加英文界面语言包 | ⭐⭐⭐ |
| **测试覆盖** | 🧪 | 添加 Jest 单元测试 | ⭐⭐ |
| **CI/CD** | 🔄 | 添加 Prettier 代码格式化检查 | ⭐⭐ |

### 贡献者公约

本项目遵循 [Contributor Covenant v2.1](https://www.contributor-covenant.org/version/2/1/code_of_conduct/) 行为准则：

- ✅ 使用 welcoming 和 inclusive 的语言
- ✅ 尊重不同的观点和经验
- ✅ 优雅地接受建设性批评
- ✅ 关注对社区最有利的事情
- ✅ 对其他社区成员表示同理心

**禁止行为**：
- ❌ 使用性化的语言或图像
- ❌ 人身攻击或政治攻击
- ❌ 公开或私下的骚扰行为
- ❌ 未经许可发布他人的私人信息
- ❌ 其他违反专业操守的行为

---

## 📄 许可证

本项目采用 **MIT License** 开源协议。

© 2026 yizehu88. All rights reserved.

### MIT License 核心条款

```
Copyright (c) 2026 yizehu88

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of THE SOFTWARE.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### 权利与义务总结

**你可以自由地**：
- ✅ **商业使用**：将此项目用于商业产品或服务
- ✅ **修改**：修改源代码以满足你的需求
- ✅ **分发**：分发原始或修改后的副本
- ✅ **私下使用**：个人学习和研究用途
- ✅ **再授权**：在修改后可以更换许可证（但不能移除原许可证）

**你需要遵守的唯一条件**：
- ⚠️ **保留版权声明**：在所有副本中包含上述版权声明和许可声明
- ⚠️ **不做担保**：软件按"原样"提供，不提供任何明示或暗示的担保

**你不能做的**：
- ❌ **起诉作者**：作者不对软件造成的任何损失负责
- ❌ **移除许可证**：不能删除或修改MIT许可证文本

详见 [LICENSE](LICENSE) 文件。

---

## 👨‍💻 作者与维护信息

### 项目维护者

- **GitHub**: [yizehu88](https://github.com/yizehu88)
- **角色**：创始人、核心开发者、项目维护者
- **负责领域**：产品规划、架构设计、代码审核、社区运营

### 项目链接

- **🏠 仓库地址**：https://github.com/yizehu88/wechat-article
- **🌐 在线演示**：https://yizehu88.github.io/wechat-article/
- **📖 文档中心**：https://github.com/yizehu88/wechat-article/blob/main/README.md
- **🐛 问题反馈**：https://github.com/yizehu88/wechat-article/issues
- **💬 讨论区**：https://github.com/yizehu88/wechat-article/discussions
- **📝 更新日志**：https://github.com/yizehu88/wechat-article/commits/main

### 联系方式

如有以下需求，欢迎通过相应渠道联系：

| 联系目的 | 推荐渠道 | 响应时间 |
|----------|----------|----------|
| 🐛 **报告Bug** | [GitHub Issues](https://github.com/yizehu88/wechat-article/issues/new?template=bug_report.md) | 1-3个工作日 |
| 💡 **功能建议** | [GitHub Issues](https://github.com/yizehu88/wechat-article/issues/new?template=feature_request.md) | 1周内回复 |
| 💬 **技术讨论** | [GitHub Discussions](https://github.com/yizehu88/wechat/discussions/categories/general) | 社区互助 |
| 🤝 **贡献代码** | [Pull Request](https://github.com/yizehu88/wechat-article/pulls) | 1-3天审核 |
| 📧 **商务合作** | 通过GitHub邮箱联系 | 3个工作日内 |
| 🔒 **安全问题** | 通过GitHub Security Advisories私密报告 | 24小时内 |

---

## 🙏 致谢（Acknowledgments）

感谢以下开源项目、服务和社区对本项目的支持和启发：

### 核心技术与基础设施
- **[GitHub](https://github.com/)**：提供免费的代码托管、版本控制和协作平台
- **[GitHub Pages](https://pages.github.com/)**：零成本的静态网站托管服务，让项目可以公开展示
- **[GitHub Actions](https://github.com/features/actions)**：强大的CI/CD自动化工具，实现持续集成和部署
- **[Google Fonts](https://fonts.google.com/)**：提供的 PingFang SC、Microsoft YaHei 等中文字体

### 内容来源
- **微信公众号生态**：所有被收录文章的原作者和公众号运营者
  - AI探秘人、松鼠Quant、Git Trend、踏浪而行生活圈
  - AI Code、我爱程序化、汇商琅琊榜、量化Quantide
  - AI工具教程、葛瑞斯Grace、创艺记、量化交易核心社群
  - （以及未来会收录的更多优质公众号）

### 设计灵感
- **[GitHub Dark Theme](https://github.com/primer/github-dark-theme)**：暗色配色方案的参考
- **[Notion](https://www.notion.so/)**：卡片式布局和折叠交互的设计灵感
- **[Dev.to](https://dev.to/)**：标签系统和文章列表的UI参考
- **[Material Design](https://material.io/design)**：Material Design设计规范的指导原则

### 开源社区
- **所有被收录文章中提到的开源项目和作者**：
  - [Kronos](https://github.com/shiyu-coder/Kronos)：金融K线基础模型
  - [ssquant](https://github.com/songshuquant/ssquant)：量化交易框架
  - [AI Hedge Fund](https://github.com/virattt/ai-hedge-fund)：多智能体交易系统
  - [Blinko](https://github.com/blinkospace/blinko)：AI笔记工具
  - [Dexter](https://github.com/virattt/dexter)：金融研究智能体
  - [OpenAlice](https://github.com/TraderAlice/OpenAlice)：AI交易代理
  - [daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)：股票分析系统
  - [Riskfolio-Lib](https://github.com/dcajasn/Riskfolio-Lib)：投资组合优化库
  - 以及更多优秀项目...

### 特别致谢
- **开源精神的践行者们**：正是因为有无数开发者的无私分享，才有了如此丰富的技术生态
- **微信公众号的创作者们**：产出高质量的技术内容，推动了行业知识传播
- **本项目的每一位访客和Star贡献者**：你们的关注是我持续维护的动力

---

## 📊 项目统计与元信息

### 基本信息
- **项目名称**：公众号文章收藏索引 (WeChat Article Collection)
- **创建时间**：2026年
- **首次提交**：（查看 `git log --reverse` 获取准确时间）
- **最后更新**：2026-04-24
- **开发语言**：HTML (56%) + CSS (32%) + JavaScript (12%)
- **许可证**：MIT License

### 内容统计（截至 2026-04-26）
- **文章总数**：13篇
- **覆盖公众号**：12个
- **关联GitHub仓库**：20+ 个
- **总Star数**：138k+（所有关联项目的星标总和）
- **标签种类**：16种
- **平均每篇文章要点数**：6.5个

### 标签分布
| 标签 | 文章数 | 占比 |
|------|--------|------|
| AI/大模型 | 7 | 53.8% |
| 量化框架 | 5 | 38.5% |
| 工具 | 4 | 30.8% |
| LLM | 3 | 23.1% |
| 智能体 | 3 | 23.1% |
| 开源项目 | 3 | 23.1% |
| 金融数据 | 2 | 15.4% |
| 期货CTP | 1 | 7.7% |
| 技术指标 | 2 | 15.4% |
| 交易心理 | 1 | 7.7% |
| 风险管理 | 1 | 7.7% |
| 策略优化 | 2 | 15.4% |
| 架构设计 | 1 | 7.7% |
| IM即时通讯 | 1 | 7.7% |
| 私有部署 | 1 | 7.7% |
| 企业级 | 1 | 7.7% |
| 金融时序 | 1 | 7.7% |
| 多智能体 | 1 | 7.7% |
| 形态识别 | 1 | 7.7% |

### 访问统计（如果集成了 Umami/Plausible）
- *(待补充：需要先集成访问统计工具)*
- 月均访问量 (PV)：
- 独立访客数 (UV)：
- 平均停留时长：
- 跳出率：
- 热门文章 Top 3：

### GitHub 统计
- **Stars**：（请访问 GitHub 仓库查看最新数据）
- **Forks**：
- **Watchers**：
- **Contributors**：
- **Open Issues**：
- **Closed Issues**：
- **Pull Requests**：

---

## 📜 更新日志 (Changelog)

### [Unreleased]

#### 计划中
- 数据外部化（抽取为JSON文件）
- 模糊搜索功能（Fuse.js）
- 文章收藏功能（localStorage）
- 暗色/亮色主题切换

### [2026-04-26] - v1.1.0

#### 新增 (Added)
- ✨ 完整的 README.md 文档（项目介绍、功能说明、技术架构、约束分析、开发指南、贡献指南等）
- ✨ 详细的项目约束说明（15项技术/功能/运维/内容约束）
- ✨ Git 连接测试文件 `test_connection.md`
- ✨ GitHub Actions 自动部署工作流 `deploy.yml`

#### 变更 (Changed)
- 📝 README 从单行标题更新为完整的项目文档
- 🎨 优化了项目结构的目录树说明

#### 文档 (Documented)
- 📖 添加了详细的使用指南和快速开始教程
- 📖 添加了如何添加新文章的分步说明
- 📖 添加了代码风格指南和Commit Message规范
- 📖 添加了性能优化建议和未来规划路线图

### [2026-04-24] - v1.0.0

#### 新增 (Added)
- ✨ 初始版本发布
- ✨ 13篇高质量微信公众号文章收录
- ✨ 智能卡片式展示系统（折叠/展开交互）
- ✨ 多维度标签筛选功能
- ✅ 全文搜索功能
- ✨ 暗色主题UI设计
- ✅ 响应式布局（支持移动端）
- ✨ GitHub Pages 自动部署
- ✨ 关联GitHub仓库展示
- ✨ 个人评价和分析功能

---

<div align="center">

---

## ⭐ 如果这个项目对你有帮助

**请给一个 Star 支持一下！** ⭐

你的 star 是我持续维护和更新的动力 💪

**Star 历史**：
![Stars](https://img.shields.io/github/stars/yizehu88/wechat-article.svg?style=social&label=Star)

**如何 Star**：
1. 访问 https://github.com/yizehu88/wechat-article
2. 点击页面右上角的 ⭐ 按钮
3. 完成！（也可以点击 👁️ Watch 接收更新通知）

---

**Made with ❤️ and ☕ by [yizehu88](https://github.com/yizehu88)**

*最后更新：2026-04-26 · 基于 MIT License 开源*

</div>
