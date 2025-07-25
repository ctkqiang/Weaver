# -*- coding: utf-8 -*-
import os
import sys
import webbrowser
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import scrolledtext


sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from src.model.news import News
from src.db.news_db import NewsDB

from src.anquanke import Anquanke
from src.cert import Cert
from src.sinchew import SinChew
from src.secrss import SecRSS
from src.zaobao import ZaoBao


class Weaver:
    def __init__(self, root):
        self.root = root
        self.root.title("Weaver 安全资讯聚合器")
        self.db = NewsDB(path=os.path.join("data", "news.db"))
        self.setup_ui()
        self.load_news()

    def get_news(self):
        anquanke = Anquanke()
        cert = Cert()
        sinchew = SinChew()
        secrss = SecRSS()
        zaobao = ZaoBao()

        anquanke.scrape()
        cert.scrape()
        sinchew.scrape()
        secrss.scrape()
        zaobao.scrape()


    def setup_ui(self):
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("微软雅黑", 13, "bold"), foreground="#ff69b4")
        style.configure("Treeview", font=("微软雅黑", 12), foreground="#d63384")
        style.configure("TLabel", font=("微软雅黑", 14, "bold"), foreground="#ff69b4")

        mainframe = ttk.Frame(self.root, padding=12)
        mainframe.pack(fill=BOTH, expand=True)

        columns = ("title", "source", "date", "url")
        self.tree = ttk.Treeview(
            mainframe,
            columns=columns,
            show="headings",
            bootstyle=SUCCESS
        )

        self.tree.heading("title", text="📰 标题")
        self.tree.heading("source", text="📌 来源")
        self.tree.heading("date", text="📅 日期")
        self.tree.heading("url", text="🔗 链接")

        self.tree.column("title", width=400, anchor="w")
        self.tree.column("source", width=100, anchor="center")
        self.tree.column("date", width=120, anchor="center")
        self.tree.column("url", width=300, anchor="w")

        self.tree.pack(fill=BOTH, expand=True, pady=(0, 12))
        self.tree.bind("<<TreeviewSelect>>", self.show_details)
        self.tree.bind("<Double-1>", self.open_url)
        self.tree.bind("<Button-3>", self.show_context_menu)

        label = ttk.Label(self.root, text="📝 文章内容")
        label.pack(anchor="w", padx=12)

        self.textbox = scrolledtext.ScrolledText(
            self.root, height=12, wrap="word", font=("微软雅黑", 12), foreground="#c71585"
        )
        self.textbox.pack(fill=BOTH, expand=False, padx=12, pady=(0, 10))

        # 添加右键菜单
        self.context_menu = ttk.Menu(self.root, tearoff=0)
        self.context_menu.add_command(label="在浏览器中打开", command=self.context_open_url)
        self.context_menu.add_command(label="复制链接", command=self.context_copy_url)
        self.context_menu.add_command(label="分享链接到剪贴板", command=self.context_share_url)

    def load_news(self):
        self.get_news()

        self.news_list = self.db.fetch_all_news()
        for news in self.news_list:
            self.tree.insert("", END, values=(news.title, news.source, news.date, news.url))

    def show_details(self, event):
        selected = self.tree.selection()
        if not selected:
            return
        index = self.tree.index(selected[0])
        news = self.news_list[index]
        self.textbox.delete(1.0, END)
        self.textbox.insert(END, f"📰 标题：{news.title}\n")
        self.textbox.insert(END, f"📅 日期：{news.date}\n")
        self.textbox.insert(END, f"📌 来源：{news.source}\n")
        self.textbox.insert(END, f"🔗 链接：{news.url}\n\n")
        self.textbox.insert(END, f"📖 正文内容：\n{news.content or '暂无内容'}")

    def open_url(self, event):
        self._open_selected_url()

    def show_context_menu(self, event):
        selected_item = self.tree.identify_row(event.y)
        if selected_item:
            self.tree.selection_set(selected_item)
            self.context_menu.post(event.x_root, event.y_root)

    def context_open_url(self):
        self._open_selected_url()

    def context_copy_url(self):
        url = self._get_selected_url()
        if url:
            self.root.clipboard_clear()
            self.root.clipboard_append(url)

    def context_share_url(self):
        url = self._get_selected_url()
        if url:
            share_text = f"我想和你分享一篇文章：\n{url}"
            self.root.clipboard_clear()
            self.root.clipboard_append(share_text)

    def _get_selected_url(self):
        selected = self.tree.selection()
        if not selected:
            return None
        index = self.tree.index(selected[0])
        return self.news_list[index].url


    def _open_selected_url(self):
        url = self._get_selected_url()
        
        if url:
            try:
                webbrowser.open_new_tab(url)
            except Exception as e:
                print(f"无法打开链接：{e}")


if __name__ == "__main__":

    app = ttk.Window(
        title="Weaver",
        themename="morph", 
        size=(1100, 700),
        resizable=(True, True)
    )
    Weaver(app)
    app.mainloop()
