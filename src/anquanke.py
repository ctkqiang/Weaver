# -*- coding: utf-8 -*-
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from model.news import News
from db.news_db import NewsDB

class Anquanke:
    def __init__(self):
        self.url = 'https://www.anquanke.com/'
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
        items = soup.select("div._94 li.item")

        if not items:
            print("❌ 没有找到文章项 ._94 li.item")
            return []

        print(f"📦 共找到 {len(items)} 篇文章")

        for item in items:
            try:
                title_tag = item.select_one("div.item-main div.title a")
                if not title_tag:
                    print("⚠️ 跳过：未找到标题")
                    continue

                title = title_tag.get_text(strip=True)
                url = urljoin(self.url, title_tag.get("href", "#"))

                date = "未知"

                news = News(
                    title=title,
                    url=url,
                    date=date,
                    source="安全客 Anquanke"
                )

                self.db.insert_news(news)
                news_list.append(news)
                print(f"✅ 成功写入: {title} [{date}]")

            except Exception as e:
                print(f"⚠️ 处理文章出错: {e}")
                continue

        return news_list
