import db

while 1:
    print("#======================================#")
    choice = int(input("""Type: 
1- Add a new item;
2- See all itens;
3- Edit an item;
4- Delete an item;
5- To exit;\n"""))
    
    match choice:
        case 1:
            item = input("Type a new item: ")
            db.startDB((1, item))
            print("New item added!")
        case 2:
            task_list = db.startDB((2,))
            print("Item list: ")
            for item in task_list:
                print(f"{item[0]} - {item[1]}")
        case 3:
            change = int(input("Choose an item to change: "))
            new_data = input("Type the new item: ")
            db.startDB((3, (change, new_data)))
            print("Changed!")
        case 4:
            delete = int(input("Choose an item to delete: "))
            db.startDB((4, delete))
            print("Item deleted!")
        case 5:
            print("Bye!")
            break
        case _:
            print("Invalid Value!")
    print("#======================================#")
