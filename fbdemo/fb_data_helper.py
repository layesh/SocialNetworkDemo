from _ast import operator

import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.facebook.com/'


def scrape_page_list(page_list):
    data_items = []

    i = 1
    for page in page_list:
        write = len(page_list) == 1 or (len(page_list) == i)
        page_data = scrape_page_contents(page, write)
        i = i + 1
        if page_data is not None:
            data_items.append(page_data)

    sorted_data = sorted(data_items, key=lambda k: k['sort_attr'], reverse=True)
    return sorted_data


def scrape_page_contents(page_name, write):
    page = requests.get(BASE_URL + page_name)
    soup = BeautifulSoup(page.content, 'html.parser')

    name_element = soup.find('span', '_81gf')

    if name_element is not None:
        f = open("pages.txt", "a+")
        if write:
            f.write(page_name)
            f.write("\n")
            f.close()
        name = name_element.text

        elements = soup.findAll('div', class_='_4bl9')
        likes = elements[1].find('div').text.split()[0]
        followers = elements[2].find('div').text.split()[0]
        sort_attr = int(followers.replace(',', ''))

        img_element = soup.find('img', class_='scaledImageFitWidth img')
        data_src = img_element['data-src']

        page_data = {
            'name': name,
            'likes': likes,
            'followers': followers,
            'profile_picture_src': data_src,
            'sort_attr': sort_attr
        }

        return page_data

    else:
        return None
