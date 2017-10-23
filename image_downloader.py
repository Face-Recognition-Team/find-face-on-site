import re
import requests
import os
from bs4 import BeautifulSoup


def download_images(site, output_dir = 'photos'):
    if not site.startswith('http'):
        site = 'http://' + site
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    response = requests.get(site)

    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')

    urls = [img['src'] for img in img_tags if 'src' in img]

    for url in urls:
        filename = re.search(r'/([\w_-]+[.](jpg))$', url)
        if not filename:
            continue
        with open(os.path.join(output_dir, filename.group(1)), 'wb') as f:
            if 'http' not in url:
                # sometimes an image source can be relative 
                # if it is provide the base url which also happens 
                # to be the site variable atm. 
                url = '{}{}'.format(site, url)
            response = requests.get(url)
            f.write(response.content)

if __name__ == '__main__':
    download_images('e1.ru')
