#步骤
收集url至url.txt
python google.py

打开xray开始监听
python xray.py

自动化网页链接收集并打开
python scan.py


#注意
1.需要安装selenium模块
2.安装chrome浏览器及chromedriver程序
3.chromedriver需要配置环境变量
4.需要添加证书至chrome
5.启动脚本前请删除或转移myscan_report.html以及url_spider.txt

#启动
python main.py

#运行环境
python3.7

#PIP
pip install

selenium
urllib
requests
pyquery
threading
