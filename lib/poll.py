from bs4 import BeautifulSoup
import urllib2
import re

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

if __name__ == "__main__":
	#h = get_html("http://news.ycombinator.com/item?id=3771286")
	#get_answers(h)
	#get_poll_title(h)
	import sys
	#print get_answer_pack("http://news.ycombinator.com/item?id=3771286")
	print get_answer_pack(sys.argv[1])


