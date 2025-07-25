# -*- coding: utf-8 -*-
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from model.news import News
from db.news_db import NewsDB


class SinChew:
    def __init__(self):
        self.url = "https://www.sinchew.com.my/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8/"
        self.headers = {
            "User-Agent": "Mozilla/5.0"
        }
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(self.base_dir, "..", "data", "news.db")
        self.db = NewsDB(path=self.db_path)

    def scrape(self):
        news_list = []

        try:
            res = requests.get(self.url, headers=self.headers, timeout=10)
            res.raise_for_status()
        except requests.RequestException as e:
            print(f"❌ 网络请求失败: {e}")
            return []

        soup = BeautifulSoup(res.text, 'html.parser')
        containers = soup.select("div.horizontal-post-frame.mobile-border")

        if not containers:
            print("❌ 没有找到文章容器 (.horizontal-post-frame)")
            return []

        print(f"📦 共找到 {len(containers)} 篇文章")

        for container in containers:
            try:
                a_tag = container.select_one("a.internalLink")
                if not a_tag:
                    continue

                title = a_tag.get("data-title", "").strip() or "无标题"
                href = a_tag.get("href", "").strip()
                url = urljoin(self.url, href)

                date_div = container.select_one("div.meta")
                date = date_div.get_text(strip=True) if date_div else "未知日期"

                summary_div = container.select_one("div.desc")
                content = summary_div.get_text(strip=True) if summary_div else ""

                news = News(
                    title=title,
                    url=url,
                    date=date,
                    source="Sinchew 星洲网",
                    content=content
                )

                self.db.insert_news(news)
                news_list.append(news)

                print(f"✅ 已保存: {title} [{date}]")

            except Exception as e:
                print(f"⚠️ 处理文章时出错: {e}")

        return news_list

