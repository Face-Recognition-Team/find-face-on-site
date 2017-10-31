#!/usr/bin/python
import sys
import recognizer
import re
import json
from image_downloader import download_images

def read_sites_list(sites_file='sites.txt'):
    with open(sites_file, "r", encoding="utf-8") as file:
        return [x for x in file.read().split('\n') if x]

def save_results(results, result_file='results.txt'):
    with open(result_file, "w", encoding="utf-8") as file:
        file.write(json.dumps(results))

def main():
    regex = re.compile(r'www\.(.*)$')
    recognizer.initialize()
    sites_list = read_sites_list(sys.argv[1])
    results = {}
    for site in sites_list:
        print ("Analyzing {}".format(site))
        folder_name = regex.search(site).group(1)
        results[site] = download_images(site, folder_name)
        recognizer.recognize(sys.argv[2], folder_name, results[site])
    save_results(results, sys.argv[3])

if __name__ == "__main__":
    main()
