from collections import Counter
from zipfile import ZipFile
import re

kWORDS = re.compile("[a-z]{4,}")

def text_from_zipfile(zip_file):
	myzip = ZipFile(zip_file)
	for name in myzip.namelist():
		text = myzip.open(name).read()
		yield str(text,'utf-8','ignore') 

def words(text):
	return re.findall(kWORDS.lower(),text)

for item in text_from_zipfile("../data/state_union.zip"):
	print(len(words(item)))
