

users = []
with open("manage.txt","r") as file:
    for mambo in file:
        name,email,isActive = mambo.rstrip().split(",")
        login_info = {"name":name,"email":email,"status":isActive}
        users.append(login_info)
    
    name = str(input("Please Enter your name: "))
    email = str(input("Please Enter your email: "))
    isActive = True
    with open("manage.txt","a") as reader:
        reader.write(f"{name},{email},{isActive}\n")

