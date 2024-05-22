# import csv

# def load_data(filename):
#     book_list = []
#     with open(filename) as books:
#         books_data = csv.reader(books, delimiter=',')
data = []
with open("books.csv","r") as books:
    for paths in books:
        name,author,price= paths.split(",")
        sumn = {'name':name,'author':author,'price':price}
        data.append(sumn)

    print(data)

search_name = input("Search name: ")

for wank in data:
    nume = wank["name"]
    if (search_name == nume):
        print(wank["author"],wank["price"])

search_author = input("Search author: ")
for gist in data:
    mist = gist["author"]
    if (search_author== mist):
        print(gist["name"],gist["price"])

max_price = int(input("Max price: "))
min_price = int(input("Min price: "))

for skibidi in data:
    flame = int(skibidi["price"])
    if (max_price <= flame and min_price >= flame):
        print(skibidi["name"],skibidi["author"])
