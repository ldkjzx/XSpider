#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Jarod Zheng'

'''
Get pictures from webside
'''

import os
import re  
import urllib  
from urllib import request
from bs4 import BeautifulSoup


#PATH = os.path.join(os.path.dirname(__file__), 'pic', '%s.jpg')

'''
def getHtml(url):  
    req = request.Request(url)
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25') 
    page = request.urlopen(req)  
    html = page.read()  
    return html  
  
def getImg(html):  
    reg = r'src="(.+?\.jpg)" '  
    imgre = re.compile(reg)  
    html = html.decode('utf-8')
    imglist = imgre.findall(html)  
    x = 0  
    for imgurl in imglist:  
        urllib.request.urlretrieve(imgurl, PATH % x)  
        x = x + 1          
     




html = getHtml("https://tieba.baidu.com/p/1546249911")  
getImg(html)
print('Completed!!!')
'''


Source = ['http://tieba.baidu.com/p/1864966611', 
'http://tieba.baidu.com/p/1962466429', 
'http://tieba.baidu.com/p/1962466429?pid=25908281312&cid=0#25908281312', 
'http://tieba.baidu.com/p/2028824237', 
'http://tieba.baidu.com/p/2028824237?pid=26953482114&cid=0#26953482114',
'http://tieba.baidu.com/p/2066742642', 
'http://tieba.baidu.com/p/2122598315', 
'http://tieba.baidu.com/p/2170607777', 
'http://tieba.baidu.com/p/2202869537']

f = 370

for html_doc in Source:
#html_doc = "https://tieba.baidu.com/p/1794831901"
    
    Temp_PATH = os.path.join(os.path.dirname(__file__), 'pic', '%s' % f)
    os.makedirs(Temp_PATH)
    PATH = os.path.join(Temp_PATH, '%s.jpg')




    req = urllib.request.Request(html_doc)  
    webpage = urllib.request.urlopen(req)  
    html = webpage.read()


    soup = BeautifulSoup(html, 'html.parser')


    #抓取图片地址
    #抓取img标签且class为BDE_Image的所有内容
    img_src=soup.findAll("img",{'class':'BDE_Image'})
    
    try:
        x = 0 
        for img in img_src:
            urllib.request.urlretrieve(img.get('src'), PATH % x)  
            print(x)
            x = x + 1  

            #img=img.get('src')   #抓取src
            #print(img)
    except urllib.error.URLError as e:
        print('except:', e)
    finally:
        pass
    print(f)
    f = f+1



