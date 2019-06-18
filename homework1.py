import urllib.request
import urllib.parse

# homewrok1: 定义一个函数,把参数写活
def name1
 print(请输入要搜索的内容:)
a=input()
 
data = urllib.parse.urlencode({'wd':'a'})
print(data)
url = 'http://www.baidu.com/s?' + data
response = urllib.request.urlopen(url)
HTML = response.read().decode('utf8')
print(HTML)


# 把 路由和参数写活

def name2
 print(请输入参数:)
a=input()
print(请输入路由:)
ly=input()

data = bytes(urllib.parse.urlencode({'pw':'a'}),enconding='utf8')
url = 'ly'
response = urllib.request.urlopen(url,data=data)
result = response.read().decode('utf8')
print(result)