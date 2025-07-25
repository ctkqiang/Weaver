# -*- coding: utf-8 -*-
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from model.news import News
from db.news_db import NewsDB

class ZaoBao:
    def __init__(self):
        self.url = 'https://www.zaobao.com.sg/keywords/wang-luo-quan'
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
        containers = soup.find_all("div", class_="content-header")

        if not containers:
            print("❌ 没有找到 .content-header 区块")
            return []

        print(f"📦 共找到 {len(containers)} 篇文章")

        for container in containers:
            try:
                a_tag = container.find("a")
                if not a_tag:
                    continue

                title = a_tag.get("aria-label", "").strip() or "无标题"
                url = urljoin(self.url, a_tag.get("href", "#"))

                timestamp_div = container.select_one("div.timestamp")
                date = timestamp_div.get_text(strip=True) if timestamp_div else "未知"

                news = News(
                    title=title,
                    url=url,
                    date=date,
                    source="Zaobao 网络权"
                )

                self.db.insert_news(news)
                news_list.append(news)

                print(f"✅ 成功写入: {title} [{date}]")

            except Exception as e:
                return

        return news_list
