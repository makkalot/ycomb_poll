from lib.poll import get_answer_pack

TEST_URLS = [
	"http://news.ycombinator.com/item?id=3771286",
	"http://news.ycombinator.com/item?id=3146321",
	"http://news.ycombinator.com/item?id=3746692",
	"http://news.ycombinator.com/item?id=3298905"
]

for url in TEST_URLS:
	print "Testing Url : ",url
	ap = get_answer_pack(url)
	print "Title : ",ap["title"]
	print "Answers : ",ap["answers"]


