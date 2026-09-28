# Yi Pan · Academic homepage

线上主页：https://yipan-eclab.github.io/
源码仓库：https://github.com/YiPan-ECLab/YiPan-ECLab.github.io

基于 **[AcadHomepage](https://github.com/RayeRen/acad-homepage.github.io)** 重做，与参考网站 [Wenqi Zhang](https://zwq2018.github.io/) 使用同一模板。保留白底、左侧个人资料、顶部导航、蓝色链接和分节正文，已公开展示全部五项工作。作者栏中的 Yi Pan 以蓝色加粗、浅蓝底和下划线高亮。

## 内容维护

- `_config.yml`：姓名、单位、邮箱、OpenReview、GitHub 和 Scholar 链接。
- `_pages/about.html`：介绍、研究方向、动态、教育和联系方式。
- `_data/publications.json`：五项工作，完整作者顺序、真实发表状态、链接及 BibTeX。
- `_includes/author-profile.html`：侧栏，`_includes/research-paper.html`：论文条目。
- `assets/css/main.scss`、`_sass/`：AcadHomepage 原始主题样式。
- `assets/css/homepage.css`、`assets/js/homepage.js`：响应式调整、作者高亮、论文搜索与引用复制。
- `TEMPLATE.md`、`LICENSE.acadhomepage`：新模板来源与许可证；`SOURCES.md`：内容来源。

三项 ICLR 2027 工作于 2026-09-28 经本人明确同意公开，标注 Conference submission。不得把投稿写成已录用，也不添加未经确认的一作、共一或通讯标记。头像暂用 YP 字母；将照片放入 `images/` 并填写 `_config.yml` 中的 `author.avatar` 即可替换。

## 本地构建

推荐 Ruby 3.3 和 Bundler。

```sh
bundle install
bundle exec jekyll build --strict_front_matter
python3 scripts/check_site.py
bundle exec jekyll serve --host 127.0.0.1 --port 4173
```

## 自动部署

推送 `main` 后 GitHub Actions 自动构建、校验、发布到 GitHub Pages。无须在仓库中存放账号密码或 token。`work/` 为本地工作文件，被 Git 与 Jekyll 排除。

2026-09-28 重做版使用浅色学术主页样式，不再加载旧版绿色主题。内容在构建时写入 HTML，不依赖运行时论文 API、访问统计或外部字体 CDN。
