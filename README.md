# Yi Pan · Academic homepage

个人学术主页，基于 [Academic Pages](https://github.com/academicpages/academicpages.github.io) 定制。

线上地址：**https://yipan-eclab.github.io/**

## 内容维护

- `_config.yml`：姓名、学校、公开邮箱、主页域名、GitHub 与 OpenReview 链接。
- `_pages/about.html`：个人介绍、研究兴趣、教育经历和联系方式。
- `_data/research.yml`：WAM、VLA、世界模型和具身智能研究方向。
- `_data/publications.json`：公开作品，含完整作者顺序、发表状态、原始链接和 BibTeX。
- `assets/css/research.css`、`assets/js/research.js`：响应式样式、主题切换、论文检索与引用复制。
- `SOURCES.md`：事实来源与核对说明。
- `TEMPLATE.md`、`LICENSE`：上游模板版本与许可证。

仅增加确实能够公开的作品。投稿条目应保留 submission 标识，不能写成已录用论文。
如要添加头像，可在 `_layouts/research.html` 中把当前 YP 字母图形换为自己的照片。

## 本地运行

推荐 Ruby 3.3 与 Bundler；当前 Gemfile 同样已在本机 Ruby 2.6.10 下构建通过。

```sh
bundle install
bundle exec jekyll serve --host 127.0.0.1 --port 4173
```

然后访问 http://127.0.0.1:4173/ 。修改 `_config.yml` 后需要重启服务。

构建和内容验证：

```sh
bundle exec jekyll build --strict_front_matter
python3 scripts/check_site.py
```

## GitHub Pages 发布

GitHub 仓库：`YiPan-ECLab/YiPan-ECLab.github.io`。
在 Settings → Pages 中将 Source 设为 **GitHub Actions**。
推送到 `main` 后，`.github/workflows/pages.yml` 会构建并发布页面。
个人主页使用空 `baseurl`；未来迁移到项目站点时，工作流会从 Pages 设置中读取子路径。

不需要在仓库中保存任何 GitHub / OpenReview 密码或 token。
`work/` 只存放本地草稿，被 Git 和 Jekyll 排除；不要提交该目录。

## 初版设计

英文界面、浅绿与暖白配色、YP 字母图形、移动端布局、深浅主题切换、论文搜索、BibTeX 展开与复制。
内容在构建时直接写入 HTML；访客关闭 JavaScript 后仍可阅读论文和使用外部链接。
没有外部字体、分析统计或运行时论文 API 依赖。
