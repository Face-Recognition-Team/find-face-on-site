#!/usr/bin/python
import sys
import recognizer
import re
from image_downloader import download_images

def read_sites_list(sites_file):
    with open(sites_file, "r", encoding="utf-8") as file:
        return [x for x in file.read().split('\n') if x]

def main():
    regex = re.compile(r'www\.(.*)$')
    recognizer.initialize()
    sites_list = read_sites_list(sys.argv[1])
    for site in sites_list:
        print ("Analyzing {}".format(site))
        folder_name = regex.search(site)[1]
        download_images(site, folder_name)
        recognizer.recognize(sys.argv[2], folder_name)

if __name__ == "__main__":
    main()
