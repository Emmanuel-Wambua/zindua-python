import time
import schedule
import requests
from bs4 import BeautifulSoup
import json
url="https://www.workatastartup.com/"
def get_jobs(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,"html.parser")
    company_name=soup.find_all("span",class_="font-bold")
    role=soup.find_all("a",class_="font-bold captialize mr-5")
    type=soup.find_all("span",class_="capitalize text-sm font-thin")
    locations=soup.find_all("span",class_="before:inline-block before:content-[''] before:mx-3 before:my-auto before:text-xs before:px-1 before:w-2 before:h-2 before:rounded-md before:bg-gray-700 capitalize text-sm font-thin")
    data=[]
    for comp,rol,ty,loca in zip(company_name,role,type,locations):
        info={"Company":comp.text,
              "Role":rol.text,
              "Type":ty.text,
              "Location":loca.text}
        data.append(info)
    return data
job=get_jobs(url)
json_file='random.json'
with open(json_file,mode="w",encoding="utf-8") as file:
        json.dump(job,file,indent=4)

url="https://www.workatastartup.com/"
def get_internship(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,"html.parser")
    company_name=soup.find_all("span",class_="font-bold")
    role=soup.find_all("a",class_="font-bold captialize mr-5")
    type=soup.find_all("span",class_="capitalize text-sm font-thin")
    locations=soup.find_all("span",class_="before:inline-block before:content-[''] before:mx-3 before:my-auto before:text-xs before:px-1 before:w-2 before:h-2 before:rounded-md before:bg-gray-700 capitalize text-sm font-thin")
    data=[]
    difference=[]
    for comp,rol,ty,loca in zip(company_name,role,type,locations):
        info={"Company":comp.text,
              "Role":rol.text,
              "Type":ty.text,
              "Location":loca.text}
        data.append(info)
    name=input("Enter:")
    for inter in data:
        if (inter["Type"]==name):
            difference.append(inter)
    return difference
internship=get_internship(url)
json_file='internship.json'
with open(json_file,mode="w",encoding="utf-8") as file:
        json.dump(internship,file,indent=4)

schedule.every(10).minutes.do(get_jobs)
while True:
    schedule.run_pending()
    time.sleep(1)
