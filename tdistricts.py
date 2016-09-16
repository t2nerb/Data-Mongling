from collections import defaultdict
from csv import DictReader, DictWriter
from districts import district_margins, all_states, all_state_rows
import heapq
kHEADER = ["STATE", "DISTRICT", "MARGIN"]
def parsefloat(val):
	try:
		if val:
			return float(val[:-1].replace(",", "."))
	except ValueError or TypeError:
		return 0

def parseint(val):
	try:
		if val:
			return int(val[:2])
	except ValueError or TypeError:
		return 0

def margin(lines, district):
	alist = []
	for ii in lines:
		if ii["D"] == district and ii["GENERAL %"]:
			alist.append(parsefloat(ii["GENERAL %"]))
	if len(alist) > 1:
		margin = max(alist) - sorted(alist)[len(alist)-2]
		return margin
	elif len(alist) == 1:
		return alist[0]
	else: 
		return 0


lines = list(DictReader(open("../data/2014_election_results.csv")))
margins = district_margins(all_state_rows(lines,'West Virginia'))
for item in lines:
	if item["D"][5:] == "UNEXPIRED TERM":
		print(item["STATE"]," has ",item["D"])


