# word_list = []


# with open("words.txt","r") as file:
#     text = file.read()
    
#     words = text.strip().split()

#     for word in words:
#         if len(word) > 9:
#             word_list.append(word)
# print(word_list)
# some_text = ["Skibidi" , "Toilet" , "Sigmapooo"]
# with open("test.txt","w") as file:
#     files = file.writelines(some_text)
# extend the script to get words with the length 
# greater than nine and store them in a list


# def find_palindromes(text):
#     return text == text[::-1]

# def printage():
#     with open("words.txt","r") as file:
#         text = file.read().splitlines()
    
#     for palindromes in text:
#         if find_palindromes(palindromes):
#             print(palindromes)

# printage()

# def new_make(palindromes):
#     with open("pali.txt","w") as trial:
#         trial = trial.writelines(palindromes)


with open("words.txt","r") as file:
    text = file.read().split()
    for word in text:
        if word == word[::-1]:
            print(word)


with open("trial.txt","w") as file:
    files = file.writelines(word)