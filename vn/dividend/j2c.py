# coding: utf-8
import csv
import json
import sys
import os
import datetime
import time
import random
import importlib
import chardet


def trans(path):
    f = open(path+'.json', 'r', encoding='utf-8')   
    #jsonData= f.read()
    #print(jsonData)
    jsonData= f.read()[10:-1]
    #print(jsonData)
    dic = json.loads(jsonData)
    flag=[]
    for num in range(0,int(len(dic)/10)):  
        flag.append(int(len(dic)*random.random()))
    f1 = 0
    for line in dic:#获取属性列表
        #dic=json.loads(line[0:-2])
        #line.encode("utf8")
        #print(line)
        #dic=json.loads(line)
        #print(dic)
        keys=line.keys()
        #print(keys)
        break

    adstring = ' --以上内容由 王张昆开发 自动翻译插件发布 - 越南9年一遇牛市 越南股票 股指期货开户咨询微信 wzk201607'
    ad = []
    ad.append(adstring)
    for i in range(2,len(line)):
        ad.append('')
        
        
    csvfile = open(path+'.csv', 'w',newline='', encoding='utf-8') 
    writer = csv.writer(csvfile)
    
    
    writer.writerow(keys)#将属性列表写入csv中
    
    
    for line in dic:#读取json数据的每一行，将values数据一次一行的写入csv中
        #dic=json.loads(line[0:-2])
        f1 = f1+1
        writer.writerow(line.values())
        if f1 in flag and (int(f1/9) <6):
            writer.writerow(ad)
    f.close()
    csvfile.close()

nowdate = datetime.datetime.now().timetuple()
td = datetime.datetime.fromtimestamp(int(time.mktime(nowdate)))
todate = td.strftime("%Y-%m-%d")

dirpath = os.getcwd()
os.chdir(dirpath)

path =dirpath+'/'+todate+'origin'
trans(path)
path =dirpath+'/'+todate+'core'
trans(path)



#ori = 'GDKHQDate,NDKCCDate,Time,CompanyName,Exchange,Note,Fileurl,LastPrice,StockURL'
#newstr = '除权日,登记日,实施日,代码,市场,事件,文件,最新价,链接'
csvfile = open(path+'.csv', 'r', encoding='utf-8')  
d = csvfile.read()
#dict_data = {}
with open(dirpath+"/ch_tran.txt", 'r', encoding='utf-8')  as df:
    for kv in [dl.strip().split('=') for dl in df]:
        d = d.replace(kv[0], kv[1])
        #dict_data[kv[0]] = kv[1]

csvfile.close()

csvfilech = open(path+'-ch.csv', 'w', encoding='utf-8') 
csvfilech.write(d)
csvfilech.close()


