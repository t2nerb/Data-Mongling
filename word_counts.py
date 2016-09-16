from collections import Counter
from zipfile import ZipFile
import re

kWORDS = re.compile("[a-z]{4,}")

def text_from_zipfile(zip_file):

def words(text):

def accumulate_counts(words, total=Counter()):

# You should not need to modify this part of the code
if __name__ == "__main__":
    total = Counter()
    for tt in text_from_zipfile("../data/state_union.zip"):
        total = accumulate_counts(words(tt), total)

    for ii, cc in total.most_common(100):
        print("%s\t%i" % (ii, cc))
