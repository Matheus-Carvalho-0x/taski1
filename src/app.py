import db
from fastapi import FastAPI, Request
from pathlib import Path
import sqlite3
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

# while 1:
#     print("#======================================#")
#     choice = int(input("""Type: 
# 1- Add a new item;
# 2- See all itens;
# 3- Edit an item;
# 4- Delete an item;
# 5- To exit;\n"""))
    
#     match choice:
#         case 1:
#             item = input("Type a new item: ")
#             db.startDB((1, item))
#             print("New item added!")
#         case 2:
#             task_list = db.startDB((2,))
#             print("Item list: ")
#             for item in task_list:
#                 print(f"{item[0]} - {item[1]}")
#         case 3:
#             change = int(input("Choose an item to change: "))
#             new_data = input("Type the new item: ")
#             db.startDB((3, (change, new_data)))
#             print("Changed!")
#         case 4:
#             delete = int(input("Choose an item to delete: "))
#             db.startDB((4, delete))
#             print("Item deleted!")
#         case 5:
#             print("Bye!")
#             break
#         case _:
#             print("Invalid Value!")
#     print("#======================================#")


# Extra safety to create the .db file
BASE_DIR = Path(__file__).resolve().parent
db_path = BASE_DIR.parent/"db"/"database.db"

connection = sqlite3.connect(db_path)
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL
            )""")

app = FastAPI()
app.mount("/static", StaticFiles(directory="../front-end", html=True), name="static")

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
