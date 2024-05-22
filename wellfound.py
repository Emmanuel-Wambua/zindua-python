
import requests

from bs4 import BeautifulSoup

url = "https://www.ycombinator.com/companies/mixrank/jobs/35HrJ61-software-engineer-global-remote"

def top_deals(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    
    title = soup.find_all("h1",class_="ycdc-section-title")
    salary = soup.find_all("strong")
    locations = soup.find_all("span")
    project_href = [i['href'] for i in soup.find_all('a',class_="ycdc-btn",href=True)]
    link = "".join(project_href)
    print(link)

    for product in title:
        print(product.text)
    for salar,location in zip(salary,locations):
        print(f"{salar.text} - {location.text}")

top_deals(url)

print("\n")

new_url="https://www.ycombinator.com/companies/mixrank/jobs/SaoXMWj-data-engineer-global-remote"
def data_science(new_url):
    response = requests.get(new_url)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find_all("h1",class_="ycdc-section-title")
    salary = soup.find_all("strong")
    locations = soup.find_all("span")
    project_href = [i['href'] for i in soup.find_all('a',class_="ycdc-btn",href=True)]
    link = "".join(project_href)
    for product in title:
        print(product.text)
    for salar,location in zip(salary,locations):
        print(f"{salar.text} - {location.text}")
        with open("random.json"mode="w") as file:
            file.dump(f"{product.text},{salar.text},{location.csv}\n")

data_science(url)