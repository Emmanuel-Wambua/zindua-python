#=====importing libraries===========
'''This is the section where you will import libraries'''

#====Login Section====
details = []
with open("user.txt","r") as login:
    for info in login:
        name,password = info.rstrip().split(",")
        about = {"name":name,"password":password}
        details.append(about)
username = input("Please Type in a username: ")
password = input("Please Type in a password: ")

for info in details:
    thing = info["name"]
    code = info["password"]
    if (thing == username and code == password):
        print("You're now logged in")


while True:
    # Present the menu to the user and 
    # make sure that the user input is converted to lower case.
    menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()

    if menu == 'r':
        pass
        new_user = input("Enter a username: ")
        pass_key = input("Enter a password: ")
        with open("user.txt","a") as file:
            file.write(f"{new_user},{pass_key}\n")

    elif menu == 'a':
        pass
        user_namu = input("Type in a username: ")
        title_namu = input("Type in a title: ")
        description_namu = input("Type in a description: ")
        due_date = input("Type in a due date: ")
        current_date = input("Current date today: ")
        complete = input("Is the task completed: ")
        with open("tasks.txt","a") as words:
            words.write(f"{user_namu},{title_namu},{description_namu},{due_date},{complete}\n")

    elif menu == 'va':
        pass
        kamado = []
        with open("tasks.txt","r") as information:
            unit = information.read()
            print(unit)
            

    elif menu == 'vm':
        pass
        search_name = input("User to search for: ")
        with open("tasks.txt","r") as file:
            for lines in file:
                user_namu,title_namu,description_namu,due_date,complete= lines.strip().split(",")
                if(search_name == user_namu):
                    teen = {"title":title_namu,"description":description_namu,"date":due_date,"status":complete}
                    print(teen)

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have entered an invalid input. Please try again")