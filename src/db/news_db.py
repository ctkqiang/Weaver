import os
import sqlite3
from typing import List
from model.news import News

class NewsDB:
    def __init__(self, path) -> None:
        os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)

        self.dbName = "news.db"
        self.conn = sqlite3.connect(path)
        self._create_table()

    def _create_table(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS news (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                url TEXT,
                date TEXT,
                source TEXT,
                content TEXT
            )
        """)
        self.conn.commit()

    def insert_news(self, news: News):
        try:
            print("✅ 正在写入数据库:", self.conn.execute("PRAGMA database_list;").fetchall())
            self.conn.execute(
                "INSERT INTO news (title, url, date, source, content) VALUES (?, ?, ?, ?, ?)",
                (news.title, news.url, news.date, news.source, news.content)
            )
            self.conn.commit()  # 这个超级关键！💥
            print(f"✅ 插入成功: {news.title}")
        except sqlite3.IntegrityError as e:
            pass

    def insert_batch(self, news_list: List[News]):
        for news in news_list:
            self.insert_news(news)

    def fetch_all(self) -> List[News]:
        cursor = self.conn.execute("SELECT title, url, date, source, content FROM news")
        rows = cursor.fetchall()
        return [News(*row) for row in rows]

    def delete_by_url(self, url: str):
        self.conn.execute("DELETE FROM news WHERE url = ?", (url,))
        self.conn.commit()

    def close(self):
        self.conn.close()