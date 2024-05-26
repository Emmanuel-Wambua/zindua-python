import time
import schedule
import requests
from bs4 import BeautifulSoup
import json
url = "https://www.workatastartup.com/companies?demographic=any&hasEquity=any&hasSalary=any&industry=any&interviewProcess=any&jobType=any&layout=list-compact&sortBy=created_desc&tab=any&usVisaNotRequired=any"
def get_jobs(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,"html.parser")
    company_name=soup.find_all("span",class_="company-name hover:underline")
    role=soup.find_all("a",class_="font-medium text-gray-900 hover:underline sm:text-lg")
    type=soup.find_all("span",class_="after:inline-block after:content-[''] after:mx-3 after:my-auto after:text-xs after:px-1 after:w-2 after:h-2 after:rounded-md after:bg-gray-700 capitalize capitalize sm:flex")
    locations=soup.find_all("span",class_="after:inline-block after:content-[''] after:mx-3 after:my-auto after:text-xs after:px-1 after:w-2 after:h-2 after:rounded-md after:bg-gray-700 capitalize")
    data=[]
    for comp,rol,ty,loca in zip(company_name,role,type,locations):
        info={"Company":comp.text,
              "Role":rol.text,
              "Type":ty.text,
              "Location":loca.text}
        data.append(info)
    return data
job=get_jobs(url)
json_file='jobs.json'
with open(json_file,mode="w",encoding="utf-8") as file:
        json.dump(job,file,indent=4)

url = "https://www.workatastartup.com/companies?demographic=any&hasEquity=any&hasSalary=any&industry=any&interviewProcess=any&jobType=any&layout=list-compact&sortBy=created_desc&tab=any&usVisaNotRequired=any"
def get_internship(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,"html.parser")
    company_name=soup.find_all("span",class_="company-name hover:underline")
    role=soup.find_all("a",class_="font-medium text-gray-900 hover:underline sm:text-lg")
    type=soup.find_all("span",class_="after:inline-block after:content-[''] after:mx-3 after:my-auto after:text-xs after:px-1 after:w-2 after:h-2 after:rounded-md after:bg-gray-700 capitalize capitalize sm:flex")
    locations=soup.find_all("span",class_="after:inline-block after:content-[''] after:mx-3 after:my-auto after:text-xs after:px-1 after:w-2 after:h-2 after:rounded-md after:bg-gray-700 capitalize")
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
json_file='intern.json'
with open(json_file,mode="w",encoding="utf-8") as file:
        json.dump(internship,file,indent=4)

