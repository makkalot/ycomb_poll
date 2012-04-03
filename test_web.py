from web.poll_gen import *
import sys

#poll = [{'answers': [[u'3', u"Yes, I\'d love some peace and quiet"], [u'3', u'No, I could care less'], [u'1', u'Indifferent']], 'title': u'Poll: Child-free flights'}]
#gen_poll_html(cache_polls = poll)
#sys.exit(0)
if len(sys.argv) == 2:
	gen_poll_html(int(sys.argv[1]))
else:
	gen_poll_html()

