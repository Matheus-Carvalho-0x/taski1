from fastapi import FastAPI, Request
from pathlib import Path
import sqlite3
from fastapi.middleware.cors import CORSMiddleware

# ======== DB configs ========
# Extra safety to create the .db file
BASE_DIR = Path(__file__).resolve().parent
db_path = BASE_DIR.parent/"db"/"database.db"

connection = sqlite3.connect(db_path, check_same_thread=False)
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL
            )""")

# ======== FastAPI configs ========
app = FastAPI()
origins = ['http://localhost:5500', 'http://127.0.0.1:5500']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

# ======== Endpoints ========
@app.post("/insert")
async def insert(request:Request):
    body = await request.json()
    data = body.get("Content")
    cursor.execute(f"""INSERT INTO tasks (task)
                       VALUES (?)""", (data,))
    connection.commit()
    return {"status": "ok"}


@app.get("/data")
def list():
    cursor.execute("SELECT * FROM tasks")
    data = cursor.fetchall()
    data_list = [{"id": x[0], "task": f"{x[1]}"} for x in data]
    return data_list


@app.delete("/delete")
async def delete(request:Request):
    body = await request.json()
    id = body.get("Content")
    cursor.execute("""DELETE FROM tasks
                   WHERE id = (?)""", (id,))
    connection.commit()
    return {"status": "ok"}
