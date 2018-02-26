import re

class Hunter:
    def __init__(self,content):
        self.content = content
    
    def catch(self,param):
        str = r'\W' + param + r'\s*=\s*\'?\(*(-?\d+(\.\d+)?((e|E)(-|\+)?\d+)?)'
        m = re.search(str,self.content,re.I)
        if m is not None:
            return m.groups()[0]
        else:
            return ''
            
    def geometry(self):
        return {
                'Wmax' : self.catch('wmax'),
                'Wmin' : self.catch('wmin'),
                'XW'   : self.catch('xw'),
                'WINT' : self.catch('wint'),
                'WL'   : self.catch('wl'),
                'WLN'  : self.catch('wln'),
                'WW'   : self.catch('ww'),
                'WWN'  : self.catch('wwn'),
                'WWL'  : self.catch('wwl'),
                'Lmax' : self.catch('lmax'),
                'Lmin' : self.catch('lmin'),
                'XL'   : self.catch('xl'),
                'LINT' : self.catch('lint'),
                'LL'   : self.catch('ll'),
                'LLN'  : self.catch('lln'),
                'LW'   : self.catch('lw'),
                'LWN'  : self.catch('lwn'),
                'LWL'  : self.catch('lwl'),
                'DWJ'  : self.catch('dwj'),
                'DLC'  : self.catch('dlc'),
                'DWC'  : self.catch('dwc'),
                'WLC'  : self.catch('wlc'),
                'WWC'  : self.catch('wwc'),
                'WWLC' : self.catch('wwlc'),
                'LLC'  : self.catch('llc'),
                'LWC'  : self.catch('lwc'),
                'LWLC' : self.catch('lwlc')
                }

if __name__=='__main__':  
    file = r'D:\Github/n40g40.mdl'
    content = open(file,'r').read()
    hunter = Hunter(content)
    x = hunter.geometry()
    print(x,hunter.catch('wvth0'))