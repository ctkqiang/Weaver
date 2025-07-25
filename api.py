from fastapi import FastAPI
import aiosqlite

app = FastAPI()

@app.get("/news")
async def news():
    rows = []
    async with aiosqlite.connect("data/news.db") as db:
        async with db.execute("SELECT title, url, date, source, content FROM news ORDER BY date DESC") as cursor:
            async for row in cursor:
                rows.append({
                    "title": row[0],
                    "url": row[1],
                    "date": row[2],
                    "source": row[3],
                    "content": row[4]
                })
    return rows
