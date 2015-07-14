import pdfkit
import pdb
import requests
from bs4 import BeautifulSoup as bs
import os

url = 'http://www.geeksforgeeks.org/tag/amazon/page/'
page_no = 1
anchors = []
while True:
	res = requests.get(url + str(page_no))
	soup = bs(res.text)
	articles = soup.find_all('article')
	if articles[0].get('id') == 'post-0':
		break
	anchors.append([link.find_all('a')[0] for link in articles]) 
	page_no = page_no + 1
	print page_no
pdb.set_trace()
number = 1
for lists in anchors:
	for anchor in lists:
		d_url = anchor.get('href')
		cmnd = 'wkhtmltopdf '+ d_url + ' "' + anchor.text + '".pdf'
		try:
			os.system(cmnd)
		except Exception as e:
			print str(e)
			print anchor.text
		print anchor.text + "-------------" +str(number)
		number = number +1
print 'hello'