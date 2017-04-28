import os, sys

def is_file(date):

	path_dir = "/media/geunuk/DATA/baetendown"
	file_list = os.listdir(path_dir)
	file_list.sort()

	date = date.replace(".", "")
	date = date.replace("<td>", "")	
	date = date.replace("</td>", "")
	date = date + ".mp3"

	if date in file_list:
		print("This is the end")
		sys.exit(1)

	else:
		return date[:-4]


