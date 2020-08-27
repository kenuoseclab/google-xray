#__author__:aydcyhr
#!/usr/bin/python
# -*- coding:utf-8 -*-
import os

if os.path.exists('myscan_report.html'):
	os.remove('myscan_report.html')
	print("原myscan_report.html文件已删除")
else:
	print("没有myscan_report.html残留")

os.system('xray.exe webscan --listen 127.0.0.1:23333 --json-output myscan_report.json')