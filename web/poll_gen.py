from lib.poll import *
from jinja2 import Template
import os

WEB_DIR = os.path.split(os.path.abspath(__file__))[0]
TMPL_FILE = "poll.html"
TMPL_FILE_PATH = os.path.join(WEB_DIR,TMPL_FILE)

def gen_poll_html(n=10):

	polls = getn_polls(n)
	template = Template(open(TMPL_FILE_PATH).read())
	res = template.render(polls=polls)
	f = open(TMPL_FILE,"w")
	f.write(res)
	f.close()


