from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

adrs = "http://wizard2.sbs.co.kr/w3/template/tp1_podcast_radio_list_down.jsp?vVodId=V2000009300&vProgId=1000987&vMenuId=1021305"
html = urlopen(adrs)
bsobj = BeautifulSoup(html, "html.parser")

key = ["박문성", "윤태진", "이말년"]

episodes = bsobj.find("tbody").findAll("tr")
for n in range(0, len(episodes)):
	part = episodes[n].findAll("td")
	
	name = part[1].get_text()
	for m in range(0, len(key)):
		if re.search(key[m], name) is not None:
			print(part[1].get_text())
			date = str(part[0])
			date = date.replace(".", "")
			date = date.replace("<td>", "")
			date = date.replace("</td>", "")
			print("Date is " + date)
			url = part[2].find("url")
			print(url)
			print("")

		else:
			continue

