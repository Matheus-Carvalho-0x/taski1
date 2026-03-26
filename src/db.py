from pathlib import Path
import sqlite3

def startDB(data):
    # Start
    data = data

    # Extra safety to create the .db file
    BASE_DIR = Path(__file__).resolve().parent
    db_path = BASE_DIR.parent/"db"/"database.db"

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL
                )""")
    
    # Functions: create, read, update, delete
    def insert(data):
        cursor.execute(f"""INSERT INTO tasks (task)
                       VALUES ('{data}')""")

    def select():
        cursor.execute(f"""SELECT * FROM tasks""")
        task_list = cursor.fetchall()
        return task_list

    def update(data):
        cursor.execute(f"""UPDATE tasks SET task = '{data[1]}' 
                       WHERE id = {data[0]}""")

    def delete(data):
        cursor.execute(f"DELETE FROM tasks WHERE id = {data}")


    # Operational
    match data[0]:
        case 1:
            insert(data[1])
        case 2:
            tasks = select()
            return tasks
        case 3:
            update(data[1])
        case 4:
            delete(data[1])

    connection.commit()
