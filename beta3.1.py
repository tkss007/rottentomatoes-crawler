__author__ = "Zhouxiang Meng"
__copyright__ = "Copyright (C) 2018 Zhouxiang Meng"
__license__ = "Public Domain"
__version__ = "3.1"

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
import time
import os

i = 1

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
    r = s.xpath('//*[@id="reviews"]/div/div[1]/div/div[2]/p/text()')
    tom_s = s.xpath('//*[@id="tomato_meter_link"]/span[2]/span/text()')
    aud_s = s.xpath('//*[@id="scorePanel"]/div[2]/div[1]/a/div/div[2]/div[1]/span/text()')
    info_1 = s.xpath('//*[@id="movieSynopsis"]/text()')

    result_name = []
    result_info_text = []
    result_info = []
    result_cast = []
    result_cast2 = []
    result_cast3 = []
    result_cast4 = []
    result_review = []
    result_tom_s = []
    result_aud_s = []


    for name in x:
        result1 = name
        result1 = (result1).replace("\n","")
        result1 = (result1).replace("  ","")
        result_name = result_name + [result1]

    for info_text in info_1:
        result = info_text
        result = (result).replace("\n","")
        result = (result).replace("  ","")
        result_info_text = result_info_text + [result]

    for info in soup.find_all('div', class_ = 'meta-value'):
        result2 = info.text
        result2 = (result2).replace("\n","")
        result2 = (result2).replace("  ","")
        result_info = result_info + [result2]
    #print result_info[3]
    if "wide" in result_info[3]:
        result_info.insert(3,'None')
    if "$" not in result_info[6]:
        result_info.insert(6,'None')
    if "minutes" not in result_info[7]:
        result_info.insert(7,'None')
        #print result_info[6]
            
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
    

    for review in r:
        result4 = review
        result4 = (result4).replace("\n","")
        result4 = (result4).replace("  ","")
        result_review = result_review + [result4]

    for tom_soc in tom_s:
        result5 = tom_soc
        result5 = (result5).replace("\n","")
        result5 = (result5).replace("  ","")
        result_tom_s = result_tom_s + [result5]
        if result_tom_s != 0:
            break
    for aud_soc in aud_s:
        result6 = aud_soc
        result6 = (result6).replace("\n","")
        result6 = (result6).replace("  ","")
        result_aud_s = result_aud_s + [result6]

    result = result_name + result_tom_s + result_aud_s + result_info_text + result_info
    if result_cast != []:
        if len(result_cast) < 6:
            n = len(result_cast)
            for x in range(n,6):
                result_cast.insert(x,'None')
        result = [result + result_cast[:6] + result_review[:10]]
    elif result_cast2 != []:
        if len(result_cast2) < 6:
            n = len(result_cast2)
            for x in range(n,6):
                result_cast2.insert(x,'None')
       	result = [result + result_cast2[:6] + result_review[:10]]
    elif result_cast3 != []:
        if len(result_cast) < 6:
            n = len(result_cast3)
            for x in range(n,6):
                result_cast3.insert(x,'None')
    	result = [result + result_cast3[:6] + result_review[:10]]
    else:
        if len(result_cast) < 6:
            n = len(result_cast4)
            for x in range(n,6):
                result_cast4.insert(x,'None')
    	result = [result + result_cast4[:6] + result_review[:10]]


    with open("test.csv","a") as csvfile: 
    	writer = csv.writer(csvfile)
       	writer.writerows(result)
	
    #print ('Working ...' + str(i-99) + '%')
    if (i-99) == 100:
        print ('\nCongratulation!!! \nJob is Completed!!!!!!!')   
    return result

class ProgressBar():
    def __init__(self, width=50):
        self.pointer = 0
        self.width = width
    def __call__(self,x):
        # x in percent
        self.pointer = int(self.width*(x/100.0))
        return "Working on: " + result_category[0] + "\n|" + ">"*self.pointer + "-"*(self.width-self.pointer)+ "|\n %d%% finished\n" % int(x)

with open("test.csv","w") as csvfile: 
	writer = csv.writer(csvfile)
	writer.writerow(['Title','Rotten_Tomatoes_Score','Audience_Score','Info_Text','Rating','Genre','Dircted_By','Written_BY','In_Theaters','On_Sisc/Streaming','Box_Office','Runtime','Studio','Actor_1','Actor_2','Actor_3','Actor_4','Actor_5','Actor_6','Review_1','Review_2','Review_3','Review_4','Review_5','Review_6','Review_7','Review_8','Review_9','Review_10'])


"""url_top_100 = 'https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/'
"""
url_top_100 = raw_input("Enter the url of the website of the top 100: ")
prefix = 'https://www.rottentomatoes.com/'

res = requests.get(url_top_100)
soup = BeautifulSoup(res.content, 'lxml')

page = requests.get(url_top_100).content
mpage = etree.HTML(page)
mp = mpage.xpath('//*[@id="top_movies_main"]/h2/text()')
result_category = []
for category in mp:
    result = category
    result = (result).replace("\n","")
    result = (result).replace("  ","")
    result_category = result_category + [result]

table = soup.find('div', class_='panel-body content_body allow-overflow').find('table')
trs = table.find_all('tr')

url_list = []

for i, tr in enumerate(trs[1:]):
    url = prefix + tr.find(class_='unstyled articleLink').get('href').strip()
    url_list.append(url)


for url in url_list:
    i = i + 1
    pb = ProgressBar()
    os.system('clear')
    print pb(i-99)
    print 'Author: Zhouxiang Meng\n', 'Copyright (C) 2018 Zhouxiang Meng\n', 'License: Public Domain\n', 'Version: 3.1'
    getinfo(url)
    
      
