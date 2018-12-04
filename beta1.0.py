from bs4 import BeautifulSoup
import requests
import urllib
import urllib2
from urllib2 import urlopen
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from lxml import etree
import pandas as pd

i = 0

def getinfo(url):
    r = urllib.urlopen(url).read()
    page = requests.get(url).content
    soup = BeautifulSoup(r, 'lxml')
    s = etree.HTML(page)

    x = s.xpath('//*[@id="movie-title"]/text()')
    y = s.xpath('//*[@id="mainColumn"]/section[4]/div/div[2]/ul/li/div[2]/text')
    z = s.xpath('//*[@id="mainColumn"]/section[6]/div/div/div/div/a/span/text()')
    z2 = s.xpath('//*[@id="mainColumn"]/section[5]/div/div/div/div/a/span/text()')
    z3 = s.xpath('//*[@id="mainColumn"]/section[4]/div/div/div/div/a/span/text()')
    z4 = s.xpath('//*[@id="mainColumn"]/section[3]/div/div/div/div/a/span/text()')

    result_name = []
    result_info = []
    result_cast = []
    result_cast2 = []
    result_cast3 = []
    result_cast4 = []

    for name in x:
        result1 = name
        result1 = (result1).replace("\n","")
        result1 = (result1).replace("  ","")
        result_name = result_name + [result1]

    for info in soup.find_all('div', class_ = 'meta-value'):
        result2 = info.text
        result2 = (result2).replace("\n","")
        result2 = (result2).replace("  ","")
        result_info = result_info + [result2]

    for cast in z:
        result3 = cast
        result3 = (result3).replace("\n","")
        result3 = (result3).replace("  ","")
        result_cast = result_cast + [result3]
    for cast2 in z2:
        result3_2 = cast2
        result3_2 = (result3_2).replace("\n","")
        result3_2 = (result3_2).replace("  ","")
        result_cast2 = result_cast2 + [result3_2]
    for cast3 in z3:
        result3_3 = cast3
        result3_3 = (result3_3).replace("\n","")
        result3_3 = (result3_3).replace("  ","")
        result_cast3 = result_cast3 + [result3_3]
    for cast4 in z4:
        result3_4 = cast4
        result3_4 = (result3_4).replace("\n","")
        result3_4 = (result3_4).replace("  ","")
        result_cast4 = result_cast4 + [result3_4]

    if result_cast != []:
	    result = [result_name + result_info + result_cast[:6]]
    elif result_cast2 != []:
    	result = [result_name + result_info + result_cast2[:6]]
    elif result_cast3 != []:
    	result = [result_name + result_info + result_cast3[:6]]
    else:
    	result = [result_name + result_info + result_cast4[:6]]


    with open("test.csv","a") as csvfile: 
    	writer = csv.writer(csvfile)
       	writer.writerows(result)
	
	print ('Working ...' + str(i-99) + '%')   
    return result


with open("test.csv","w") as csvfile: 
	writer = csv.writer(csvfile)
	writer.writerow(['Title','Rating','Genre','Dircted By','Written BY','In Theaters','On Sisc/Streaming','Box Office','Runtime','Studio','Actor1','Actor2','Actor3','Actor4','Actor5','Actor6'])


url_top_100 = 'https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/'
prefix = 'https://www.rottentomatoes.com/'

res = requests.get(url_top_100)
soup = BeautifulSoup(res.content, 'lxml')

table = soup.find('div', class_='panel-body content_body allow-overflow').find('table')
trs = table.find_all('tr')

url_list = []

for i, tr in enumerate(trs[1:]):
    url = prefix + tr.find(class_='unstyled articleLink').get('href').strip()
    url_list.append(url)


for url in url_list:
    i = i + 1
    getinfo(url)

