import requests
from bs4 import BeautifulSoup


def web_scrapping():
    url = "https://timesofindia.indiatimes.com/topic/headline"

    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.content, "html.parser")
    soup.prettify()

    head_class = soup.find_all('div', class_ = 'fHv_i o58kM')

    headlines = list()
    for i in head_class:
        head = i.get_text().strip()
        headlines.append(head)
    return file_generation(headlines)

def file_generation(headlines):
    file = open("Headlines.txt",'w')
    S_no = 1
    for i in headlines:
        file.write(f"{S_no}. {i}\n")
        S_no += 1
    file.close()
    return "Successfully completed"

if __name__ == "__main__":
    web_scrapping()
