from web.poll_gen import *
import sys


if len(sys.argv) == 2:
	gen_poll_html(int(sys.argv[1]))
else:
	gen_poll_html()

