from collections import Counter
from zipfile import ZipFile
import re

kWORDS = re.compile("[a-z]{4,}")

def text_from_zipfile(zip_file):
	#open zipfile in 'read' mode
	myzip = ZipFile(zip_file, 'r')
	#for each filename in zipfile
	for name in myzip.namelist():
		#binary literal string read from each filename
		text = myzip.open(name).read()
		#yield 'utf-8' encoded string, and 'ignore' encoding errors
		yield str(text,'utf-8','ignore')

def words(text):
	#return a list of all words matching kWORDS regex (iterable)
	return re.findall(kWORDS,text.lower())

def accumulate_counts(words, total=Counter()):
	for word in words:
		# Ex. {'hello': 8}
		total[word] += 1
	assert isinstance(total, Counter)
	return total 

# You should not need to modify this part of the code
if __name__ == "__main__":
    total = Counter()
    for tt in text_from_zipfile("../data/state_union.zip"):
        total = accumulate_counts(words(tt), total)

    for ii, cc in total.most_common(100):
        print("%s\t%i" % (ii, cc))
