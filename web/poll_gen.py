from lib.poll import *
from jinja2 import Template
import os

WEB_DIR = os.path.split(os.path.abspath(__file__))[0]
TMPL_FILE = "poll.html"
TMPL_FILE_PATH = os.path.join(WEB_DIR,TMPL_FILE)

def gen_poll_html(n=10,cache_polls=None):
	
	if not cache_polls:
		polls = getn_polls(n)
	else:
		polls = cache_polls
		
	web_polls = []
	for p in polls:
		answ_pack = []
		for ap in p['answers']:
			#quick hack
			answ_pack.append([str(ap[0]),str(ap[1].replace("'",""))])
		
		web_polls.append({'title':p['title'],'answers':answ_pack})
	template = Template(open(TMPL_FILE_PATH).read())
	res = template.render(polls=web_polls)
	f = open(TMPL_FILE,"w")
	f.write(res)
	f.close()


