import requests
from bs4 import BeautifulSoup
import json
url = "https://meet.google.com/xms-ksdw-ovt"
def top_deals(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    products = soup.find_all("p", class_="-pvs")
    deals = []
    for product in products:
        deals.append(product.text.strip())
    return deals
deals_data = top_deals(url)
json_file = 'top_deals.json'
with open(json_file, mode='w') as file:
    json.dump(deals_data, file, indent=4)
print(f"Data has been stored in {json_file}")