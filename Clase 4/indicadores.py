from urllib.request import Request, urlopen
from pyquery import PyQuery

class Indicadores():

    def __init__(self):
        self.trm = 0
        self.uvr = 0
        self.dtf = 0
        self.salarioMinimo = 0

    def ExtraeData(self):
        url = 'https://www.dane.gov.co/index.php/indicadores-economicos'
        req = Request(url, None,{'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'})
        content = urlopen(req).read()
        pq = PyQuery(content)
        trm = [i.text() for i in pq('table').eq(1)('h1').items()]
        self.trm = float(trm[0].replace(".",'').replace("$",'').replace(",",'.'))
        
        uvr = [i.text() for i in pq('table').eq(2)('h1').items()]
        self.uvr = float(uvr[0].replace(".",'').replace("$",'').replace(",",'.'))

        dtf = [i.text() for i in pq('table').eq(3)('h1').items()]
        self.dtf = float(dtf[0].replace(".",'').replace("$",'').replace(",",'.').replace("%",''))

        salarioMinimo = [i.text() for i in pq('table').eq(7)('h1').items()]
        self.salarioMinimo = float(salarioMinimo[0].replace(".",'').replace("$",'').replace(",",'.'))

        print(self.trm)
        print(self.uvr)
        print(self.dtf)
        print(self.salarioMinimo)