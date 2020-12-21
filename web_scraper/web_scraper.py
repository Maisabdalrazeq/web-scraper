import requests 
from bs4 import BeautifulSoup 
import json

def get_citations_needed_count(URL):
    '''
    (get_citations_needed) function to count how many citations_needed in the page !
    '''
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.findAll(class_='noprint Inline-Template Template-Fact') 
    return len(results)

  

def get_citations_needed_report(URL):
    '''
    (get_citations_needed_report) function to return the paragraph and the line that contain the citation_needed
    '''
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.findAll(class_='noprint Inline-Template Template-Fact') 

    for x in results:
        citation_section = x.find_parent('p')
        print(f'The citations_needed paragraph :{citation_section.text}')






if __name__ == "__main__":
   URL = "https://en.wikipedia.org/wiki/History_of_Mexico"
   print(f'The citations_needed Num : {get_citations_needed_count(URL)}') 
   print()
   print()
   print(f'The citations_needed paragraph : {get_citations_needed_report(URL)}') 
   print() 
   print()

