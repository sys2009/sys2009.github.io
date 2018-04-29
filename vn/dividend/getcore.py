#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests 
from gettk import Py4Js
import json
import datetime
import time
import urllib.parse
import os
#import urllib.request
#import chardet
import re
import csv

def writefile(path,content):
    f = open(path, 'w',encoding="utf-8")
    f.write(content)
    f.close()

def trans(content):
    js = Py4Js()
    tk = js.getTk(content) 
    print(tk)

    if len(content) > 4891:    
        print("翻译的长度超过限制！！！")    
        pass 
    else:
        param = {'tk': tk,'q': content }
        result = requests.get("""http://translate.google.cn/translate_a/single?client=t&sl=vi&tl=zh-CN
        &hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss
        &dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1&srcrom=0&ssel=0&tsel=0&kc=2""", params=param)
    #返回的结果为Json，解析为一个嵌套列表
    #for text in result.json()[0][0:-1]:
        #print(text)
        #print('****')
    return result.json()[0][0:-1][0]

nowdate = datetime.datetime.now().timetuple()
print(nowdate)
print(nowdate.tm_year)
td = datetime.datetime.fromtimestamp(int(time.mktime(nowdate)))
fdate =  td.strftime("%d/%m/%Y")
todate = td.strftime("%Y-%m-%d")
timeStamp = int(time.mktime(nowdate))+2*24*30*24*60*60
#timeStamp = int(time.mktime(nowdate))+2*24*30*24*60*60
tdate = datetime.datetime.fromtimestamp(timeStamp).strftime("%d/%m/%Y")
param = {'fdate': fdate,'tdate': tdate }
baseurl = """http://finance.vietstock.vn/Controls/Event/Data/GetEvent.ashx?type=filter&scode=&etypechild=-1&catid=-1&dir=asc&page=1&psize=800"""
url="&fdate="+str(nowdate.tm_mon)+"%2F"+str(nowdate.tm_mday)+"%2F"+str(nowdate.tm_year)+"&tdate="+str(nowdate.tm_mon)+"%2F"+str(nowdate.tm_mday)+"%2F"+str(nowdate.tm_year+5)
content = requests.get(baseurl+url)
content = content.json()

dirpath = os.getcwd()
os.chdir(dirpath)

path =dirpath+'/'+todate+'origin.json'
contentorigin = json.dumps(content,ensure_ascii=False)
writefile(path,contentorigin)

#print(content['Event'])
for data in content['Event']:
    del data['ColorId']
    del data['TotalRow']
    del data['PerChange']
    del data['Change']
    del data['Location']
    del data['Title']
    del data['Content']
    del data['CompanyName2']
    if data['GDKHQDate'] is None:
        pass
    else:
        data['GDKHQDate'] = datetime.datetime.fromtimestamp(int(data['GDKHQDate'][6:-5])).strftime("%Y-%m-%d")
    if data['NDKCCDate'] is None:
        pass
    else:
        data['NDKCCDate'] = datetime.datetime.fromtimestamp(int(data['NDKCCDate'][6:-5])).strftime("%Y-%m-%d")

    if data['Time'] is None:
        pass
    else:
        data['Time'] = datetime.datetime.fromtimestamp(int(data['Time'][6:-5])).strftime("%Y-%m-%d")
    #print(data)
    #print('***')
    #print(data['Note'])
    #print('***---')

    #data['Note'] = trans(data['Note'])
'''    
    d = data['Note'][0]
    d = re.sub('(\d)/20(\d{2})',r'\2年第\1次', d)
    d = d.replace("额外交易", "增发股上市流通")
    d = d.replace("额外交易", "增发股上市流通")
    d = d.replace("东/股", "越南盾/股")
    d = d.replace("VND / CP", "越南盾/股")
    d = d.replace("股票评级", "股票奖励 ")
    d = d.replace("由VB毕业", "收到股东书面意见 ")
'''    

#    data['Title'] = trans(data['Title'])
#    data['Content'] = trans(data['Content'])

path =dirpath+'/'+todate+'core.json'
content_tran = json.dumps(content,ensure_ascii=False)
writefile(path,content_tran)    




'''
random.seed(datetime.datetime.now())  
  
csvfile = open('test.csv', 'wt', newline='', encoding='utf-8')  
writer = csv.writer(csvfile)  
  
  
def store(title, content):  
    csvrow = []  
    csvrow.append(title)  
    csvrow.append(content)  
    writer.writerow(csvrow)  
  
  
def get_links(acticle_url):  
    html = urlopen('http://en.wikipedia.org' + acticle_url)  
    soup = BeautifulSoup(html, 'html.parser')  
    title = soup.h1.get_text()  
    content = soup.find('div', {'id': 'mw-content-text'}).find('p').get_text()  
    store(title, content)  
    return soup.find('div', {'id': 'bodyContent'}).findAll('a', href=re.compile("^(/wiki/)(.)*$"))  
  
links = get_links('')  
  
try:  
    while len(links) > 0:  
        newActicle = links[random.randint(0, len(links) - 1)].attrs['href']  
        links = get_links(newActicle)  
        print(links)  
finally:  
    csvfile.close()  

    data['Note'] = trans(data['Note'])
    data['Title'] = trans(data['Title'])
    data['Content'] = trans(data['Content'])
'''

