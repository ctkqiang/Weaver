# -*- coding: utf-8 -*-
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from model.news import News
from db.news_db import NewsDB


class SecRSS:
    def __init__(self):
        self.base_url = "https://www.secrss.com"
        self.list_url = f"{self.base_url}/articles?tag=%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB"
        self.headers = {
            "User-Agent": "Mozilla/5.0"
        }
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(self.base_dir, "..", "data", "news.db")
        self.db = NewsDB(path=self.db_path)

    def scrape(self):
        try:
            response = requests.get(self.list_url, headers=self.headers)
            response.raise_for_status()
        except Exception as e:
            print(f"🚨 请求失败: {e}")
            return

        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.select("ul#article-list > li.list-item")

        if not articles:
            print("⚠️ 没有找到任何文章元素")
            return

        for article in articles:
            try:
                title_tag = article.select_one("h2.title a")
                if not title_tag:
                    continue

                title = title_tag.get_text(strip=True)
                url = urljoin(self.base_url, title_tag["href"])

                time_tag = article.select_one("span.time")
                date = time_tag.get_text(strip=True) if time_tag else "未知"

                summary_tag = article.select_one("p.intro")
                summary = summary_tag.get_text(strip=True) if summary_tag else ""

                news = News(
                    title=title,
                    url=url,
                    date=date,
                    source="SecRSS",
                    content=summary 
                )


                self.db.insert_news(news)

                print(f"✅ 成功保存: {title}")

            except Exception as err:
                print(f"❌ 处理文章出错: {err}")
