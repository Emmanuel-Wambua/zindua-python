

running = True

while running:

    operator = input("Select operation (+ - / * vp): ")

    try:
        if operator == '+':
            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))
            result = num1 + num2
            print(round(result, 3))
            with open("equations.txt","a") as file:
                file.write(f"Addition of {num1} and {num2} is {result} \n")
        elif operator == 'vp':
            with open("equations.txt","r") as file:
                text = file.read()
                print(text)
                running = False
        elif operator == '-':
            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))
            result = num1 - num2
            print(round(result, 3))
            with open("equations.txt","a") as file:
                file.write(f"Subtraction of {num1} and {num2} is {result} \n")
        elif operator == '*':
            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))
            result = num1 * num2
            print(round(result, 3))
            with open("equations.txt","a") as file:
                file.write(f"Multiplication of {num1} and {num2} is {result} \n")
        elif operator == '/':
            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))
            result = num1/num2
            print(round(result, 3))
            with open("equations.txt","a") as file:
                file.write(f"Division of {num1} and {num2} is {result} \n")
        else:
            print(f"{operator} is not an option")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except ValueError:
        print("Please Type in a number")
    else:
        print(f"Nice {operator} there")

    calculate_again = input("Do you want to calculate again?(y/n): ").lower()
    if not calculate_again == 'y':
        running = False

print("THANK YOU FOR CALCULATING")

