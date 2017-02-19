import urllib.request   #网络电池
import urllib.parse
import json
import time
while True:
    nei = input('输入q!退出。输入要翻译的内容:')
    if nei == 'q!':
        break

    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link'

    '''
    head = {}    #隐藏的一种方式，生成Request之前User-Agent 通过Request的headers参数修改
head['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3004.3 Safari/537.36'
    '''

    data = {}
    data['type'] = 'AUTO'
    data['i'] = nei
    data['doctype'] = 'json'
    data['xmlVersion'] = '1.8'
    data['keyfrom'] = 'fanyi.web'
    data['ue'] = 'UTF-8'
    data['action'] = 'FY_BY_CLICKBUTTON'
    data['typoResult'] = 'true'
    data = urllib.parse.urlencode(data).encode('utf-8')         #编码为utf-8

    req = urllib.request.Request(url,data)
    req.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3004.3 Safari/537.36')  #第二种通过Request.add_header()方法修改
    response = urllib.request.urlopen(req) 
    html = response.read().decode('utf-8')  #解码
    target = json.loads(html)
    target = target['translateResult'][0][0]['tgt']

    print (target)
    time.sleep(0.5)
#print ("结果为： %s " % (target['translateResult'][0][0]['tgt']))
