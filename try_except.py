# x = "Mark"

# try:
#     print(int(x))
# except NameError:
#     print("x is not defined")
# except:
#     print("Something else is wrong with your code")
# finally:
#     print("End of 'try except block' ")

# try:
#     print("Hello World")
# except:
#     print("Could not be executed")
# else:
#     print("No issues detected")

age = "Bir"

def eligibilty(age):

        if not type(age) is int:
            raise TypeError("Must be an integer")
        elif(age < 18):
            raise Exception("You're a nonce")
        else:
            print("You're good")
    

    
eligibilty(age)
