from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
from isfile import is_file
import re, sys

adrs = "http://wizard2.sbs.co.kr/w3/template/tp1_podcast_radio_list_down.jsp?vVodId=V2000009300&vProgId=1000987&vMenuId=1021305&cpage=1"

def main(adrs, page):
	html = urlopen(adrs)
	bsobj = BeautifulSoup(html, "html.parser")
	key = ["박문성", "윤태진", "이말년"]
	num = 1

	episodes = bsobj.find("tbody").findAll("tr")
	for n in range(0, len(episodes)):
		part = episodes[n].findAll("td")

		date = is_file(str(part[0]))
		name = part[1].get_text()

		for m in range(0, len(key)):
			if re.search(key[m], name) is not None:

				print(part[1].get_text())
				print("WHEN? >>> %s" % date)
				print("START DOWNLOADING #%d...\n" %num)
				urlretrieve((part[2].input.attrs["value"]), "/media/geunuk/DATA/baetendown/%s.mp3" %date)

				num += 1

			else:
				continue

	print('--------------------------- THIS IS THE END OF PAGE %d ------------------------' %page)
	
	page += 1
	adrs = adrs[:-1] + str(page)
	main(adrs, page)

main(adrs, 1)
