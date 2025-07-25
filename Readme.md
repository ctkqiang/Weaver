# Weaver 安全资讯聚合器

## 项目简介
Weaver 是一个基于 Python 的安全资讯聚合工具，旨在从多个安全资讯网站自动抓取最新的安全新闻，并以图形界面展示给用户，方便安全从业者及时获取行业动态。

![demo](./assets/截屏2025-07-25%20下午10.11.24.png)

## 主要功能
- 自动爬取多个安全资讯网站（如安全客、国家互联网应急中心、星洲网、SecRSS、早报网络权）
- 将抓取的新闻存储到本地 SQLite 数据库
- 通过图形界面展示新闻列表，支持查看新闻详情
- 支持通过右键菜单操作，如在浏览器中打开链接、复制链接、分享链接

## 项目结构
```
Weaver/
├── .gitignore               # Git 忽略配置
├── assets/                  # 资源文件，如图标
├── build.py                 # 打包脚本，支持 macOS 和 Windows
├── main.py                  # 主程序入口，包含 GUI 逻辑
└── src/                     # 源代码目录
    ├── anquanke.py          # 安全客爬虫模块
    ├── cert.py              # 国家互联网应急中心爬虫模块
    ├── sinchew.py           # 星洲网爬虫模块
    ├── secrss.py            # SecRSS 爬虫模块
    ├── zaobao.py            # 早报网络权爬虫模块
    ├── db/                  # 数据库操作模块
    │   └── news_db.py       # SQLite 数据库封装
    └── model/               # 数据模型
        └── news.py          # 新闻数据类
```

## 依赖环境
- Python 3.10+
- requests
- beautifulsoup4
- ttkbootstrap

可通过 `pip install -r requirements.txt` 安装依赖。

## 激活虚拟环境
```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 使用说明
1. 克隆项目并进入目录
2. 运行 `python main.py` 启动程序
3. 程序启动后会自动抓取各大安全资讯网站的最新新闻并展示
4. 在新闻列表中点击可查看详情，右键菜单支持打开链接、复制链接等操作

## 打包说明
- 使用 `build.py` 脚本进行打包
- 支持 macOS 生成 `.app` 和 `.dmg` 安装包
- 支持 Windows 生成 `.exe` 可执行文件

## 代码说明
- 各爬虫模块负责从对应网站抓取新闻，解析后存入数据库
- `NewsDB` 类封装了 SQLite 数据库的增删查改操作
- `Weaver` 类负责 GUI 界面搭建和事件处理


## 👩‍💻 作者信息

- 👩🏻‍💻 项目作者：灵儿（ctkqiang）
- 🐱 GitHub：`https://github.com/ctkqiang`
- 📚 Gitcode：`https://gitcode.com/ctkqiang_sr`
- 📝 个人博客：`https://blog.ctkqiang.com`
- 📮 反馈邮箱：`ctkqiang@dingtalk.com`

---

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request 来帮助改进这个项目！

1. Fork 本仓库
2. 创建您的特性分支 (git checkout -b feature/AmazingFeature)
3. 提交您的更改 (git commit -m 'Add some AmazingFeature')
4. 推送到分支 (git push origin feature/AmazingFeature)
5. 打开一个 Pull Request

---

## 👥 作者

- 作者：钟智强
- 邮箱：johnmelodymel@qq.com
- QQ：3072486255
- 微信：ctkqiang

---


## 🫶 Star 一下让我知道你看见我啦！

这不仅是个工具，也是我热爱的安全世界的一部分 ❤️


## 🌟 开源项目赞助计划

### 用捐赠助力发展

感谢您使用本项目！您的支持是开源持续发展的核心动力。  
每一份捐赠都将直接用于：  
✅ 服务器与基础设施维护（魔法城堡的维修费哟~）  
✅ 新功能开发与版本迭代（魔法技能树要升级哒~）  
✅ 文档优化与社区建设（魔法图书馆要扩建呀~）

点滴支持皆能汇聚成海，让我们共同打造更强大的开源工具！  
（小仙子们在向你比心哟~）

---

### 🌐 全球捐赠通道

#### 国内用户

<div align="center" style="margin: 40px 0">

<div align="center">
<table>
<tr>
<td align="center" width="300">
<img src="https://github.com/ctkqiang/ctkqiang/blob/main/assets/IMG_9863.jpg?raw=true" width="200" />
<br />
<strong>🔵 支付宝</strong>（小企鹅在收金币哟~）
</td>
<td align="center" width="300">
<img src="https://github.com/ctkqiang/ctkqiang/blob/main/assets/IMG_9859.JPG?raw=true" width="200" />
<br />
<strong>🟢 微信支付</strong>（小绿龙在收金币哟~）
</td>
</tr>
</table>
</div>
</div>

#### 国际用户

<div align="center" style="margin: 40px 0">
  <a href="https://qr.alipay.com/fkx19369scgxdrkv8mxso92" target="_blank">
    <img src="https://img.shields.io/badge/Alipay-全球支付-00A1E9?style=flat-square&logo=alipay&logoColor=white&labelColor=008CD7">
  </a>
  
  <a href="https://ko-fi.com/F1F5VCZJU" target="_blank">
    <img src="https://img.shields.io/badge/Ko--fi-买杯咖啡-FF5E5B?style=flat-square&logo=ko-fi&logoColor=white">
  </a>
  
  <a href="https://www.paypal.com/paypalme/ctkqiang" target="_blank">
    <img src="https://img.shields.io/badge/PayPal-安全支付-00457C?style=flat-square&logo=paypal&logoColor=white">
  </a>
  
  <a href="https://donate.stripe.com/00gg2nefu6TK1LqeUY" target="_blank">
    <img src="https://img.shields.io/badge/Stripe-企业级支付-626CD9?style=flat-square&logo=stripe&logoColor=white">
  </a>
</div>

---

### 📌 开发者社交图谱

#### 技术交流

<div align="center" style="margin: 20px 0">
  <a href="https://github.com/ctkqiang" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-开源仓库-181717?style=for-the-badge&logo=github">
  </a>
  
  <a href="https://stackoverflow.com/users/10758321/%e9%92%9f%e6%99%ba%e5%bc%ba" target="_blank">
    <img src="https://img.shields.io/badge/Stack_Overflow-技术问答-F58025?style=for-the-badge&logo=stackoverflow">
  </a>
  
  <a href="https://www.linkedin.com/in/ctkqiang/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-职业网络-0A66C2?style=for-the-badge&logo=linkedin">
  </a>
</div>

#### 社交互动

<div align="center" style="margin: 20px 0">
  <a href="https://www.instagram.com/ctkqiang" target="_blank">
    <img src="https://img.shields.io/badge/Instagram-生活瞬间-E4405F?style=for-the-badge&logo=instagram">
  </a>
  
  <a href="https://twitch.tv/ctkqiang" target="_blank">
    <img src="https://img.shields.io/badge/Twitch-技术直播-9146FF?style=for-the-badge&logo=twitch">
  </a>
  
  <a href="https://github.com/ctkqiang/ctkqiang/blob/main/assets/IMG_9245.JPG?raw=true" target="_blank">
    <img src="https://img.shields.io/badge/微信公众号-钟智强-07C160?style=for-the-badge&logo=wechat">
  </a>
</div>

---

🙌 感谢您成为开源社区的重要一员！  
💬 捐赠后欢迎通过社交平台与我联系，您的名字将出现在项目致谢列表！