import re

pattern_email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z.-]+\.[a-zA-Z]'
pattern_number = r'\(\d{3}\) \d{3}-\d{4}'
pattern_street = r'\D\s?\D\s?\D\s?\d{5}'

with open("sample.txt","r") as file:
    text = file.read()

number = re.findall(pattern_number,text)
print(number)
email = re.findall(pattern_email,text)
print(email)

street = input("Street name: ")
if(re.search(pattern_street,street)):
    print("Yes")
else:
    print("No")

