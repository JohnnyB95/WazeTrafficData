
# REFERENCE: https://www.tutorialspoint.com/python/python_xml_processing.htm

from xml.dom.minidom import parse
import xml.dom.minidom
import datetime 

# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse("waze-sample4.xml")
print "Step 1 COMPLETE"


collection = DOMTree.documentElement
print "Step 2 COMPLETE"
#if collection.hasAttribute("rss"):
#	print "Step 3 Complete"
   #print "Root element : %s" % collection.getAttribute("xmlns:georss")


items = collection.getElementsByTagName("item")
print "Step 3 COMPLETE"

for item in items:
   print "*****Item*****"
  
   title = item.getElementsByTagName('title')[0]
   print "TITLE: %s" % title.childNodes[0].data

   pubDate = item.getElementsByTagName('pubDate')[0]
   #print pubDate
   #pubYear = pubDate[0:4]
   print "PUBDATE: %s" % pubDate.childNodes[0].data

   speed = item.getElementsByTagName('linqmap:speedKMH')[0]
   print "SPEED: %s" % speed.childNodes[0].data

   street = item.getElementsByTagName('linqmap:street')[0]
   print "STREET: %s" % street.childNodes[0].data

print "Step 4 COMPLETE"