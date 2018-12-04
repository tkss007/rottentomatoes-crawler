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

"""start_urls = ["https://www.rottentomatoes.com/m/avengers_infinity_war/"]
for i in range(1, 5):
    start_urls.append("https://www.rottentomatoes.com/m/avengers_infinity_war/")
    url = urllib2.requests(start_urls)
    sock = urllib2.urlopen(url)
    r = sock.read()
    sock.close"""


#r = urllib.urlopen('https://www.rottentomatoes.com/m/avengers_infinity_war/').read()
def getinfo(url):
    r = urllib.urlopen(url).read()
    page = requests.get(url).content
    soup = BeautifulSoup(r, 'lxml')
    s = etree.HTML(page)

    x = s.xpath('//*[@id="movie-title"]/text()')
    y = s.xpath('//*[@id="mainColumn"]/section[4]/div/div[2]/ul/li/div[2]/text')
    z = s.xpath('//*[@id="mainColumn"]/section[6]/div/div/div/div/a/span/text()')


    result_name = []
    result_info = []
    result_cast = []


    for name in x:
        result1 = name
        result1 = (result1).replace("\n","")
        result1 = (result1).replace("  ","")
        result_name = result_name + [result1]
    #print result_name

    for info in soup.find_all('div', class_ = 'meta-value'):
        result2 = info.text
        result2 = (result2).replace("\n","")
        result2 = (result2).replace("  ","")
        result_info = result_info + [result2]
    #print result_info

    for cast in z:
        result3 = cast
        result3 = (result3).replace("\n","")
        result3 = (result3).replace("  ","")
        result_cast = result_cast + [result3]
    #print result3
    #print result_cast
    result = result_name + result_info + result_cast[:6]
    #return result

    #return result

    file = open('/Users/TKSS/Desktop/result.txt','a')


    """
    for i in range(0,len(result1)):
        result = zip(result1[i],result2[i],result3[i])
        print result"""

    """for i in range(0,len(aa)):
        file.write(aa[i])"""
        #file.write('\n')
    s = ''.join([str(x) for x in result])

    file.write(s)
    file.write('\n')

    file.close

    return result

#for i in range(1,101):
#url = r'file:///Users/TKSS/Desktop/1.html'
    #localPath = r'/Users/TKSS/Desktop/'
#url = 'https://www.rottentomatoes.com/m/avengers_infinity_war/'
urls = ['https://www.rottentomatoes.com/m/mad_max_fury_road','https://www.rottentomatoes.com/m/avengers_infinity_war/']
print type(urls)


url_top_100 = 'https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/'
prefix = 'https://www.rottentomatoes.com/'

res = requests.get(url_top_100)
soup = BeautifulSoup(res.content, 'lxml')

table = soup.find('div', class_='panel-body content_body allow-overflow').find('table')
trs = table.find_all('tr')

url_list = []

for i, tr in enumerate(trs[1:]):
    #tmeter_score = int(tr.find(class_='tMeterScore').text.strip()[:-1])
    #title = tr.find(class_='unstyled articleLink').text.strip()
    url = prefix + tr.find(class_='unstyled articleLink').get('href').strip()
    #no_of_reviews = int(tr.find(class_='right hidden-xs').text.strip())
    url_list.append(url)

#print movie_list

for url in url_list:
    #urls = ['https://www.rottentomatoes.com/m/mad_max_fury_road','https://www.rottentomatoes.com/m/avengers_infinity_war/']
    print getinfo(url)

