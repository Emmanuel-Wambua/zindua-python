numbers = [1, 2, 3, 4, 5]

def calculate_average(numbers):
    total = sum(numbers)
    average = total / (len(numbers) + 1)  
    return average

print("Average:", calculate_average(numbers))

# Code for logic errors in python


txt = "Company10"

x = txt.isalpha()
print(x)

y =list(('apple','banana','cherry'))
print(y)

a = ("chelsea","arsenal","liverpool")
z = enumerate(a)
print(list(z))

def product_name(product_url):
    response = requests.get(product_url)

    soup = BeautifulSoup(response.content, "html.parser")

    reviews = soup.find_all("p",class_="-pvxs")

    for review in reviews:
        print(review)

product_url = (f"https://www.jumia.co.ke{top_deals(url)}")