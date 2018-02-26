import re

class Select:

    def __init__(self,file):
        self.file = file
        self.whole = open(file,'r').read()
        self.devices = re.findall('(.model\s+(.+)\s+(n|p)mos)',self.whole,re.I)
        self.count = len(self.devices)
        if self.count > 0:
            self.check()
        
    def check(self):
        self.til_list = [x[0] for x in self.devices]
        self.dvc_list = [x[1] for x in self.devices] 
        self.dic = {x:y for x,y in zip(self.dvc_list,self.til_list)}
        
    def row(self,title,wholelines):
        for i,line in enumerate(wholelines):
            line = line.lstrip(' ')
            if line[:len(title)] == title:
                break
        return i
        
    def extract(self,dv_name):
        wholelines = open(self.file,'r').readlines()
        title = self.dic[dv_name]
        start = self.row(title,wholelines)

        str = wholelines[start]        
        for line in wholelines[start+1:]:
            line = line.lstrip(' ')
            if line[0] == '*':
                # comment in hspice
                continue
            elif line[0] == '.':
                # another model
                break
            else:
                str += line       
        return str