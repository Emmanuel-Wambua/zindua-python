
import requests

from bs4 import BeautifulSoup

url = "https://www.jumia.co.ke/catalog/productratingsreviews/sku/NI534ST0DQQMYNAFAMZ/"

def top_deals(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    
    products = soup.find_all("p",class_="-pvs")
    

    for product in products:
        print(product.text)


top_deals(url)


