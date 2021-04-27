# Importing libraries 
import time 
import hashlib 
import urllib.request 
import ssl
import difflib
import notify as ng
import readurl as rd
from urllib.request import urlopen, Request 
from urllib.request import build_opener, HTTPCookieProcessor
opener = build_opener(HTTPCookieProcessor())
global_threshold = 0
ssl._create_default_https_context = ssl._create_unverified_context

def init_url_list():
    url_list = []
    with open('urls.txt') as f:
            url_list = [line.rstrip() for line in f]

    return url_list
    

def get_webpage(url):
    return rd.read_url(url)

def string_diff(string1, string2):
    return [li for li in difflib.ndiff(string1, string2) if li[0] != ' ']

def play(url_list):
    godDict = {}
    
    for url in url_list:
        godDict[url]  = get_webpage(url)

    while True:
        time.sleep(30)
        for url in url_list:
            new = get_webpage(url)
            actual = godDict.get(url)
            diff = string_diff(new,actual)
            diff_amount = len(diff)
            if diff_amount>global_threshold:
                ng.shoot_alert(url)
                godDict[url] = new
                print(url+' : UPADTED ')
                print('Diff= : ', diff)





if __name__ == '__main__':
    url_list = init_url_list()
    print("Running")
    play(url_list)
