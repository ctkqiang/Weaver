# -*- coding: utf-8 -*-
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from model.news import News
from db.news_db import NewsDB


class Cert:
    def __init__(self):
        self.base_url = "https://www.cert.org.cn/publish/main/11/index.html"
        self.headers = {
            "User-Agent": "Mozilla/5.0"
        }
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(self.base_dir, "..", "data", "news.db")
        self.db = NewsDB(path=self.db_path)

    def scrape(self):
        news_list = []

        resp = requests.get(self.base_url, headers=self.headers)
        resp.encoding = "utf-8"
        soup = BeautifulSoup(resp.text, "lxml")

        ul = soup.find("ul", class_="waring_con")

        if not ul:
            print("❌ 没有找到 waring_con 的 UL")
            return []

        for li in ul.find_all("li"):
            try:
                date = li.find("span").text.strip()
                a = li.find("a")
                title = a.text.strip()
                url = urljoin(self.base_url, a['href'])

                news = News(
                    title=title,
                    url=url,
                    date=date,
                    source="中国国家互联网应急中心"
                )


                news_list.append(news)
            except Exception as e:
                print(f"⚠️ 解析错误: {e}")

        for news in news_list:
            inserted = self.db.insert_news(news)

            if inserted:
                print(f"✅ 插入成功: {news.title}")
            else:
                return

        return news_list
