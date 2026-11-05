# Chao Tang — Academic Homepage

基于 [RayeRen / AcadHomepage](https://github.com/RayeRen/acad-homepage.github.io) 直接定制的 Jekyll 学术主页。目标地址：https://chao142857.github.io 。公开部署目标为同名 GitHub Pages 仓库。

## 本地预览

已生成 `_site/`，这台机器可以立即预览（不需要重新安装 Ruby）：

```bash
cd chao
python3 -m http.server 4000 --bind 127.0.0.1 --directory _site
```

浏览器打开 http://127.0.0.1:4000 。按 Ctrl+C 停止。修改源码后需要重新构建。

常规开发环境推荐 Ruby 3.3，Bundler 2.4.22 或兼容版本：

```bash
gem install bundler -v 2.4.22
bundle config set --local path vendor/bundle
bundle install
bundle exec jekyll serve --host 127.0.0.1
```

生产构建及检查：

```bash
JEKYLL_ENV=production bundle exec jekyll build
python3 scripts/check_site.py _site
```

本次已使用本机 Ruby 2.6.10 完成真实 Jekyll 3.10 构建。系统 Ruby / Xcode 的路径和老 RubyGems 中文路径问题已通过临时、隔离的构建处理解决，未修改系统。依赖缓存位于被 Git 忽略的 vendor/；新机器优先使用 Ruby 3.3，不必复刻这些本机兼容处理。

## 结构与编辑入口

```text
_config.yml                  站点 URL、姓名、学校、GitHub
_pages/about.md              简介、经历、教育、个人兴趣
_data/projects.yml           三个项目的内容与图片/视频路径
_data/navigation.yml         顶部导航
_layouts/default.html        AcadHomepage 主布局
_includes/                   头像侧栏、导航、页面头信息
_sass/_chao.scss              个人配色、排版与响应式样式
_sass/                       保留的原模板 Sass 基础
assets/css/main.scss         样式入口
assets/video/                三段本地、无音轨 MP4
images/                      原始头像、原创月亮图标、视频封面
.github/workflows/pages.yml   GitHub Pages 构建、检查、部署
scripts/check_site.py         资源、链接、锚点、模板残留检查
LICENSE                      原 AcadHomepage MIT 许可
THIRD_PARTY_NOTICES.md        上游和媒体说明
docs/                        内容来源、待补资料、验收记录
```

页面无额外 JavaScript 库、远程字体、分析追踪或 Scholar 爬虫。assets/js/site.js 仅使用少量原生 JavaScript 实现主题切换。三个项目展示为自动循环 GIF，桌面展示尺寸保持 240×150；无展开播放器。Video 链接直接打开保留的原速 MP4。系统启用减少动态效果时使用静态帧。暗色模式默认跟随系统，顶栏按钮可切换并记住选择。头像保留完整正方形与原始像素。已加入真实 Gmail mailto 联系方式；Publications、Scholar、CV 未创建。

## GitHub Pages 部署

1. 登录 `chao142857`，创建公开仓库 **chao142857.github.io**。本次公开访问返回 404；若你的账号内已有同名私有仓库，先核实并备份，不要覆盖。新仓库不要预生成 README、LICENSE 或 .gitignore。
2. 把本目录的内容放在仓库根目录，不能再套一层 `chao/`。不要上传 vendor/、_site/、.bundle/ 或 QA 截图。GIF 与三段原速视频合计约 43 MiB，首次上传前可在本地确认画面及公开范围；原始 75.9 MiB MOV 不在源码中。
3. 仓库 **Settings → Pages → Build and deployment → Source** 选择 **GitHub Actions**。
4. 审核下面命令后手动执行。只适用于新建且空的远程仓库；不使用 force push：

```bash
cd chao
git init -b main
git add .
git diff --cached --stat
git status --short
# 审核清单与视频之后，再执行：
git commit -m "Build Chao Tang academic homepage"
git remote add origin https://github.com/chao142857/chao142857.github.io.git
git push -u origin main
```

5. 在 Actions 等待 Build and deploy Jekyll site 成功。工作流先构建并检查，再部署到 github-pages 环境；PR 只构建，不部署。
6. 打开 https://chao142857.github.io 。`_config.yml` 已设置正确的 url 与空 baseurl。后续 main 分支提交会触发更新。若改为项目子路径部署，同时修改 baseurl，并保留所有 relative_url 过滤器。

工作流采用 GitHub 官方 Pages artifact/deploy 方式：
https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages

## 内容维护

见 docs/CONTENT_SOURCES.md 与 docs/TO_COMPLETE.md。更新经历和项目时只加入可核实的信息。添加研究结果时保留实机/仿真边界，SGS 不写成原创方法或已证明优于基线。当前实习条目只列用户提供的职位类别与时间，没有推断职责。
