import requests
from bs4 import BeautifulSoup

def scrape_ycombinator_jobs():
    url = 'https://www.ycombinator.com/jobs/role/software-engineer'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    job_listings = []
    for job in soup.find_all('div', class_='job-item'):
        title = job.find('h4').text.strip()
        description = job.find('div', class_='job-description').text.strip()
        # Add more fields as needed
        job_listings.append({'title': title, 'description': description})
    
    return job_listings

# if __name__ == "__main__":
#     jobs = scrape_ycombinator_jobs()
#     for job in jobs:
#         pr

print(scrape_ycombinator_jobs())