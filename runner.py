from Proxy import Proxydownloader
from ip_check import Proxyfilter
for i in range(5):
    url = 'http://www.xicidaili.com/nn/'+str(i+1)
    Proxydownloader(url)
Proxyfilter()
