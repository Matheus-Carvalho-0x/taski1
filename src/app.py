flag = True
item_list = []
i = 0
x = True

while flag:
    print("#======================================#")
    choice = int(input("""Type: 
1 - Add a new item;
2 - See all itens;
3- Edit an item;
4- Delete an item;
5- To exit;\n"""))
    
    match choice:
        case 1:
            item = input("Type a new item: ")
            i += 1
            item_list.append([i, item])
            print("New item added!")
        case 2:
            print("Item list: ")
            for item in item_list:
                print(f"{item[0]} - {item[1]}")
        case 3:
            change = int(input("Choose an item to change: "))
            new_data = input("Type the new item: ")
            for item in item_list:
                if item[0] == change:
                    item[1] = new_data
                    print("Changed!")
                    x = False
            if x:
                print("Item not found!")
        case 4:
            delete = int(input("Choose an item to delete: "))
            for item in item_list:
                if item[0] == delete:
                    item_list.pop(delete-1)
            print("Item deleted!")
        case 5:
            print("Bye!")
            flag = False
        case _:
            print("Invalid Value!")
    print("#======================================#")