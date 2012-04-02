from bs4 import BeautifulSoup
import urllib2
import re
import time
from urlparse import urljoin


DOMAIN_NAME = "http://news.ycombinator.com"
MAIN_URL = "http://news.ycombinator.com/newest"
FIND_ITEM_RE = "^item\?id\=(\d+)$"
HN_ITEM_STR = "item?id=%s"


def get_html(url):
	resp = urllib2.urlopen(url)
	return resp.read()  

def get_poll_title(html):
	soup = BeautifulSoup(html)
 	title = soup.find_all("td",{"class":"title"})[0].text   
	return title

def get_answers(html):
	soup = BeautifulSoup(html)
	options = soup.find_all("td",{"class":"comment"})	
	answ_pack = []
	for option in options:
		points = option.parent.findNextSibling("tr").text.strip()
		points = re.match("^(\d+).*",points)
		if not points:
			continue
		points = points.group(1)
		answer = option.text.strip()
		answ_pack.append((points,answer))
	
	return answ_pack

def get_answer_pack(url):
	html =  get_html(url)
	title = get_poll_title(html)
	answs = get_answers(html)
	return {"title":title,"answers":answs}

def find_page_links(html):
	soup = BeautifulSoup(html)
 	urls = filter(lambda a: not a is None, 
							map(lambda td: td.a if td.find_all('a') else None,
								soup.find_all("td",{"class":"title"})))

	return urls

def find_more_link(html):
	"""
	Finds the 'more' link in the hackernews page
	"""
 	urls = find_page_links(html)
	if not urls:
		return None

	return urls[-1].get('href')

def find_poll_urls(urls):
	"""
	Finds the poll urls in given url list
	The list is a soup list not normal one
	"""
	flist = []
	for url in urls:
		text = url.text.strip().lower()
		if text.startswith('poll'):
			#print "POLL : ",text
			flist.append(url.get('href'))

	return flist

def get_poll_process_data(urls):
	"""
	Traverses the given urls and extracts
	from them poll data if any and returns
	back a list of it.
	"""
	poll_data = []
	for url in urls:
		try:
			poll_res = get_answer_pack(urljoin(DOMAIN_NAME,url))
			if not poll_res['answers']:
				continue
			print "POLL : %s "%poll_res
			#sometimes they get angry when pull lots of data
			time.sleep(1)
			poll_data.append(poll_res)
		except Exception,ex:
			print "EXception : ",str(ex)
			time.sleep(1)
			continue
		
	return poll_data

def getn_polls(n=10):
	"""
	Goes to hackernews and pulls the only polls
	"""
	search_html = get_html(MAIN_URL)
	poll_data = get_poll_process_data(find_poll_urls(find_page_links(search_html)))
	if len(poll_data) == n:
		return poll_data 
	link = find_more_link(search_html)
	print link
	while True:
		search_html = get_html(urljoin(DOMAIN_NAME,link))
		poll_data.extend(get_poll_process_data(find_poll_urls(find_page_links(search_html))))
		if len(poll_data) >= n:
			return poll_data
		link = find_more_link(search_html)
		print "NEXT 10: ",link

	return poll_data


if __name__ == "__main__":
	#h = get_html("http://news.ycombinator.com/item?id=3771286")
	#get_answers(h)
	#get_poll_title(h)
	import sys
	#print get_answer_pack("http://news.ycombinator.com/item?id=3771286")
	print get_answer_pack(sys.argv[1])


