import logging
import os
import urllib2
import datetime


def getData(streamtype):
	urlJSON = 'https://world-georss.waze.com/rtserver/web/TGeoRSS?tk=ccp_partner&ccp_partner_name=Johnny%20Test&format=JSON&types=traffic,alerts,irregularities&polygon=125.641000,7.136000;125.577000,7.073000;125.565000,7.045000;125.611000,7.043000;125.663000,7.121000;125.641000,7.136000;125.641000,7.136000'
	urlXML = 'https://world-georss.waze.com/rtserver/web/TGeoRSS?tk=ccp_partner&ccp_partner_name=Johnny%20Test&format=XML&types=traffic,alerts,irregularities&polygon=125.641000,7.136000;125.577000,7.073000;125.565000,7.045000;125.611000,7.043000;125.663000,7.121000;125.641000,7.136000;125.641000,7.136000'

	time = datetime.datetime.now()

	if streamtype == 'XML':
		print ('Download XML')
		url=urlXML
		filename = 'waze-%s.xml' %(time)

	else:
		print ('Download JSON')
		url=urlJSON
		filename = 'waze-%s.json' %(time)



	response = urllib2.urlopen(url)

	f = open(filename, 'w')
	f.write(response.read())
	f.close

	print ("File created %r") % filename


def main():
	print "hello"
	getData('JSON')

if __name__ == '__main__':
	main()