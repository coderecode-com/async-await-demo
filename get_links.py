import csv

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def main():
    curr_list = 'https://en.wikipedia.org/wiki/List_of_circulating_currencies'
    all_links = []
    response = requests.get(curr_list)
    soup = BeautifulSoup(response.text, "lxml")
    curr_el = soup.select('p+table td:nth-child(2) > a, p+table td:nth-child(1) > a:nth-child(1)')
    for link_el in curr_el:
        link = link_el.get("href")
        link = urljoin(curr_list, link)
        all_links.append(link)
    with open('links.csv', 'w') as f:
        writer = csv.writer(f)
        for link in all_links:
            writer.writerow([link])


if __name__ == '__main__':
    main()
