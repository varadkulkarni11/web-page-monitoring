# Importing libraries 
import time 
import hashlib 
import urllib.request 
import ssl
import notify as ng
from urllib.request import urlopen, Request 
from urllib.request import build_opener, HTTPCookieProcessor
opener = build_opener(HTTPCookieProcessor())

ssl._create_default_https_context = ssl._create_unverified_context

def init_url_list():
    url_list = []
    with open('urls.txt') as f:
            url_list = [line.rstrip() for line in f]

    return url_list

def get_url_responses(url_list):
    responses =[]
    for url in url_list:
        responses.append(urlopen(url).read())
    return responses

def get_html_hashes(responses):
    currentHashes = []
    for response in responses:
        currentHashes.append(hashlib.sha224(response).hexdigest())
    return currentHashes

def initialize_currentHashes(url_list):

    responses = get_url_responses(url_list)
    currentHashes = get_html_hashes(responses) 
     
    return (currentHashes)

def diff(currentHashes,newHashes,url_list):
    sz = len(currentHashes)
    changed = 0
    for i in range(sz):
        if newHashes[i]==currentHashes[i]:
            continue
        else:
            changed = 1
            print("something changed: "+ str(url_list[i])) 
            ng.shoot_alert(url_list[i])

    return changed

def play(url_list):
    while True: 
        try: 
            currentHashes = initialize_currentHashes(url_list)
            time.sleep(30) 
              
            newHashes = initialize_currentHashes(url_list)
            
            changed = diff(currentHashes,newHashes,url_list)
            if changed: 
                time.sleep(30) 
                continue
                  
        except Exception as e: 
            print("error: "+str(e))

    



if __name__ == '__main__':
    url_list = init_url_list()
    print("Running")
    play(url_list)
