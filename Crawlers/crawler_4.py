import requests
import lxml.html
import re

def main():
    session = requests.Session()
    response = session.get('http://hanbit.co.kr/store/books/new_book_list.html')
    urls = scraping_list_page(response)
    for url in urls:
        response = session.get(url)
        ebook = scraping_detail_page(response)
        print(ebook)

def scraping_list_page(response):
    root = lxml.html.fromstring(response.content)
    root.make_links_absolute(response.url)
    for a in root.cssselect('.view_box .book_tit a'):
        url = a.get('href')
        yield url

def scraping_detail_page(response):
    root = lxml.html.fromstring(response.content)
    ebook = {
        'url': response.url,
        'title': root.cssselect('.store_product_info_box h3')[0].text_content(),
        'price': root.cssselect('.pbr strong')[0].text_content(),
        'content': [normalize_space(p.text_content())
            for p in root.cssselect('#tabs_3 .hanbit_edit_view p')
            if normalize_space(p.text_content()) !='']
    }
    return ebook

def normalize_space(s):
    return re.sub(r'\s+', '', s).strip()

if __name__ == '__main__':
    main()