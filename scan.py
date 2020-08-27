#__author__:aydcyhr
#!/usr/bin/python
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
import os
from faker import Factory
import time

def spider(url,num):
	option=Options()
	option.add_argument("--headless")#没有窗口
	option.add_argument('–disable-javascript')
	#option.add_argument('--window-size=300,200')
	option.add_argument('–no-sandbox')
	#option.add_argument('--blink-settings=imagesEnabled=false')#不显示图片
	option.add_argument('--proxy-server=http://127.0.0.1:23333')
	#使用随机ua，不然封ip需要人机验证
	f = Factory.create()
	ua = f.user_agent()
	print('使用UA：'+ua)
	option.add_argument('--user-agent="'+ua+'"')
	driver =webdriver.Chrome(options=option)
	driver.get(url)
	#标签分类
	nodelist = driver.find_elements_by_tag_name('a') + driver.find_elements_by_tag_name('script') + driver.find_elements_by_tag_name('img') + driver.find_elements_by_tag_name('link') + driver.find_elements_by_tag_name('iframe')
	for url in nodelist:
		print(url)
		if url.get_attribute("src"):
			url1 = url.get_attribute("src")
			if str(url1)[0:4]=='http':
				print(str(url1))
				file = 'url/url_'+str(num)+'.txt'
				fp=open(file,"a+",encoding="utf-8")
				fp.write(url1+'\n')
				fp.close()
		if url.get_attribute("href"):
			url2 = url.get_attribute("href")
			if str(url2)[0:4]=='http':
				print(str(url2))
				file = 'url/url_'+str(num)+'.txt'
				fp=open(file,"a+",encoding="utf-8")
				fp.write(str(url2)+'\n')
				fp.close()
	driver.quit()

number = int(input("请输入扫描迭代次数："))
num = 1
while num <= number:
	txt = 'url/url_'+str(num-1)+'.txt'
	print(txt)
	with open(txt, 'r') as x:
		for line in x:
			if line and line[0:4]=='http':
				print(line)
				spider(line,num)
	time.sleep(10)
	num = num+1