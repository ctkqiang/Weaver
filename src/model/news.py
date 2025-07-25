class News:
    def __init__(self, title: str, url: str, date: str, source: str, content: str = "") -> None:
        self.title = title
        self.url = url
        self.date = date
        self.source = source
        self.content = content


    def __str__(self):
        return f"<News(title={self.title[:20]}..., source={self.source})>"

    def __repr__(self):
        return f"= {self.date} | {self.title}  \n"