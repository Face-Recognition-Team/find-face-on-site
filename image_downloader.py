import re
import requests
import os
import asyncio
import aiohttp
from bs4 import BeautifulSoup

async def download_file(url, filepath):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                with open(filepath, 'wb') as f:
                    f.write(await response.read())
    except Exception as e:
        print('exception while download image:')
        print(e)


def download_images(site, output_dir = 'photos'):
    if not site.startswith('http'):
        site = 'http://' + site
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    response = requests.get(site)

    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')

    urls = [img['src'] for img in img_tags if img.get('src') is not None]
    coros = []
    for url in urls:
        filename = re.search(r'/([\w_-]+[.](jpg))', url)
        if not filename:
            continue
        filepath = os.path.join(output_dir, filename.group(1))
        if 'http' not in url:
            # sometimes an image source can be relative 
            # if it is provide the base url which also happens 
            # to be the site variable atm. 
            url = '{}{}'.format(site, url)
        coros.append(download_file(url, filepath))
        # with open(os.path.join(output_dir, filename.group(1)), 'wb') as f:
        #     response = requests.get(url)
        #     f.write(response.content)
    loop = asyncio.get_event_loop()
    wait_task = asyncio.wait(coros)
    loop.run_until_complete(wait_task)
    loop.close()

if __name__ == '__main__':
    download_images('https://www.facebook.com/max.vedernikov.7')
