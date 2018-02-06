print('Set Up Complete \nWelcome to To Do Lister')
item_number = 1 #Sets most of the required variables and lists
todo_list = []
todo_list_temp = []
item_1 = ''
item_2 = ''

with open('todo.txt') as f: #Opens the files with a 'with' statement: closes when it
    todo_file = f           #reaches the end of the block
    for item in todo_file:
        item = str(item_number) + ". " + item.strip() #Strips each item from the doc and appends to the main list
        item_number += 1
        todo_list.append(item)
    user = input('Enter Command: ').lower()

    while user:
        if user in 'list':
            for item in todo_list: #If called, prints the entire list
                print (item)

        if user in 'add':
            new_item = input('New ToDo: ')
            if new_item != '':
                todo_list.append(str(item_number) + ". " + new_item) #Adds a new item to the list with a number in front
                item_number += 1

        if user in 'remove':
            remove_item = input('Enter ID to Remove: ') #Removes and item and adjusts all of the numbers
            if remove_item != '':
                remove_item = int(remove_item)
                todo_list.remove(todo_list[remove_item - 1])
                item_number = 1
                todo_list_temp = []
                for item in todo_list:
                    if item_number <= 9:
                        todo_list_temp.append(str(item_number) + '. ' + item[3:])
                    if item_number >= 10:
                        todo_list_temp.append(str(item_number) + '. ' + item[4:])
                    item_number += 1
                todo_list = todo_list_temp

        if user in 'exit': #Quits the program
            exit()

        if user in 'search': #Search feature. Searches the entire list for the entered keyword. If found it prints the result with a new number based on the order it was in the original list.
            search_query = input('Enter Search Query: ')
            item_number = 1
            counter = 0
            for item in todo_list:
                counter += 1
                if search_query in item.lower():
                    if counter <= 9:
                        print(str(item_number) + '. ' + item[3:]) #Changes the number of digits removed from the start based on the value (ten and above need more taken)
                    if counter >= 10:
                        print(str(item_number) + '. ' + item[4:])
                    item_number += 1

        if user in 'swap': #Swaps two items based on the inputed number
            code_1 = input('Enter top item: ')
            code_2 = input('Enter bottom item: ')
            for item in todo_list:
                if code_1 in item:
                    item_1 = item
                if code_2 in item:
                    item_2 = item
            i1 = todo_list.index(item_1)
            i2 = todo_list.index(item_2)
            if item_1 != False and item_2 != False:
                todo_list[i2], todo_list[i1] = todo_list[i1], todo_list[i2]
            item_number = 1
            todo_list_temp = []
            counter = 0
            for item in todo_list:
                counter += 1
                if counter <= 9:
                    todo_list_temp.append(str(item_number) + '. ' + item[3:]) #Changes the number of digits removed from the start based on the value (ten and above need more taken)
                if counter >= 10:
                    todo_list_temp.append(str(item_number) + '. ' + item[4:])
                item_number += 1
            todo_list = todo_list_temp

        if user in 'clear': #Creates a clear function with Are You Sure to make sure you don't clear if you didn't want to.
            confirm = input('Are You Sure? ').lower()
            if 'yes' in confirm:
                todo_list = []
                print ('Cleared')
        todo_list_temp = []
        if user in 'insertnew':
            insert_where = int(input('Enter Location: '))
            counter = 0
            item_number = 1
            for item in todo_list:
                counter += 1
                if counter == insert_where:
                    new_item = input("Enter Item: ")
                    if counter <= 9:
                        todo_list_temp.append(str(item_number) + '. ' + new_item) #Changes the number of digits removed from the start based on the value (ten and above need more taken)
                    if counter >= 10:
                        todo_list_temp.append(str(item_number) + '. ' + new_item)
                if counter <= 9:
                    todo_list_temp.append(str(item_number) + '. ' + item[3:]) #Changes the number of digits removed from the start based on the value (ten and above need more taken)
                if counter >= 10:
                    todo_list_temp.append(str(item_number) + '. ' + item[4:])
                item_number += 1
            todo_list = todo_list_temp

        n = open('todo.txt', 'w') #Opens the file to write- will over ride all other information in the file.
        item_number = 1
        for item in todo_list:
            if item_number <= 9:
                print(item[3:], file=n)
            if item_number >= 10:
                print(item[4:], file=n)
            item_number += 1
        n.close() #Closes file

        user = input('Enter Command: ').lower() #Gets the next command
