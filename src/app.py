from fastapi import FastAPI, Request
from pathlib import Path
import sqlite3
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

# ======== DB configs ========
# Extra safety to create the .db file
BASE_DIR = Path(__file__).resolve().parent
db_path = BASE_DIR.parent/"db"/"database.db"

connection = sqlite3.connect(db_path)
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL
            )""")

# ======== FastAPI configs ========
app = FastAPI()
app.mount("/static", StaticFiles(directory="../front-end", html=True), name="static")


# ======== Endpoints ========
@app.get("/")
def home():
    return FileResponse("../front-end/index.html")


@app.post("/insert")
async def insert(request:Request):
    body = await request.json()
    data = body.get("Content")
    cursor.execute(f"""INSERT INTO tasks (task)
                       VALUES (?)""", (data,))
    connection.commit()
    return {"status": "ok"}
