#Python 2.7
#Process Waze Data stream JSON/XML

import json
import csv

with open('waze-sample1.json') as f:
	wazedata = json.load(f)

print wazedata

with open ('waze-sample1.csv')

# for i in wazedata:
# 	print (i+'='+wazedata[i])

