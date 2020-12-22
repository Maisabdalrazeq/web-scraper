from web_scraper.web_scraper import get_citations_needed_count ,get_citations_needed_report

def test_citation_count(): 
    expected = 5 
    actual = get_citations_needed_count('https://en.wikipedia.org/wiki/History_of_Mexico') 
    assert actual == expected

# def test_citation_report():  
#     URL = "https://en.wikipedia.org/wiki/History_of_Mexico"
#     actual = get_citations_needed_report(URL)
#     expected = "The citations_needed paragraph :During the three centuries of colonial rule, fewer than 700,000 Spaniards, most of them men, settled in Mexico.[citation needed] Europeans, Africans, and indigenous intermixed, creating a mixed-race casta population in a process known as mestizaje. Mestizos, people of mixed European-indigenous ancestry, constitute the majority of Mexico's population."
#     assert actual == expected

   