import ssl
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
ssl._create_default_https_context = ssl._create_unverified_context
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
def read_url(url):
	req = Request(url, headers=headers)
	html = urlopen(req,timeout=20).read()
	soup = BeautifulSoup(html, features="html.parser")
	# kill all script and style elements
	for script in soup(["script", "style"]):
		script.extract()
	# rip it out
	# get text
	text = soup.get_text()
	# break into lines and remove leading and trailing space on each
	lines = (line.strip() for line in text.splitlines())
	# break multi-headlines into a line each
	chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
	# drop blank lines
	text = '\n'.join(chunk for chunk in chunks if chunk)
	return text

if __name__ == '__main__':
    text = read_url("https://www.google.com")
    print (text)