import requests
def geturl(url):
    res = requests.head(url)
    url = res.headers.get('location')
    return url
print(geturl('http://login.10086.com'))