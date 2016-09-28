import urllib.request
import socket
import re
def Proxyfilter():
    socket.setdefaulttimeout(3)
    f = open("proxy.txt")
    lines = f.readlines()
    proxys = []
    f = open("/Users/leotao/PycharmProjects/untitled4/jijing/jijing/proxy_worked.txt","a")
    for i in range(0,len(lines)):
        ip = lines[i].strip("\n").split("\t")
        proxy_host = "http://"+ip[0]+":"+ip[1]
        proxy_temp = {"http":proxy_host}
        proxys.append(proxy_temp)
    url = "http://ip.chinaz.com/getip.aspx"
    for proxy in proxys:
        try:
            proxy_support = urllib.request.ProxyHandler(proxy)
            opener=urllib.request.build_opener(proxy_support)
            res = opener.open(url).read()
            kk=proxy['http']
            print(kk)
            print(proxy)
            print('passed')
            print(res)
            f.write(kk+'\n')
        except Exception as err:
            print(proxy)
            print(err)
    f.close()
