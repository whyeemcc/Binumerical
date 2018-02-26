class Cal:

    def __init__(self,list):  
        self.Wmax   = list[0]
        self.Wmin   = list[1]
        self.xw     = list[2]
        self.wint   = list[3]
        self.wl     = list[4]
        self.wln    = list[5]
        self.ww     = list[6]
        self.wwn    = list[7]
        self.wwl    = list[8]
        self.Lmax   = list[9]
        self.Lmin   = list[10]
        self.xl     = list[11]
        self.lint   = list[12]
        self.ll     = list[13]
        self.lln    = list[14]
        self.lw     = list[15]
        self.lwn    = list[16]
        self.lwl    = list[17]
        self.Base   = list[18]
        self.Lvalue = list[19]
        self.Wvalue = list[20]
        self.Pvalue = list[21]
        self.upper  = list[22]
        self.lower  = list[23]
        
    def Weff(self,Wdesign,Ldesign):
        Wphy = Wdesign + self.xw
        Lphy = Ldesign + self.xl
        deltaW = self.wint + self.wl/(Lphy**self.wln) + self.ww/(Wphy**self.wwn) + self.wwl/(Lphy**self.wln)/(Wphy**self.wwn)
        return Wphy - 2*deltaW
        
    def Leff(self,Wdesign,Ldesign):
        Wphy = Wdesign + self.xw
        Lphy = Ldesign + self.xl
        deltaL = self.lint + self.ll/(Lphy**self.lln) + self.lw/(Wphy**self.lwn) + self.lwl/(Lphy**self.lln)/(Wphy**self.lwn)
        return Lphy - 2*deltaL

    def result(self):
        Binlist = []
        for W in (self.Wmax,self.Wmin):
            for L in (self.Lmax,self.Lmin):
                Weff = self.Weff(W,L)
                Leff = self.Leff(W,L)
                Base = self.Base
                Bin_L = self.Lvalue/Leff
                Bin_W = self.Wvalue/Weff
                Bin_P = self.Pvalue/(Leff*Weff)
                Bin_Total = Base + Bin_L + Bin_W + Bin_P 
                
                if self.upper == 'Inf' :
                    Total_less_upper = True
                else:
                    if Bin_Total <= eval(self.upper) : Total_less_upper = True
                    else: Total_less_upper = False
                    
                if self.lower == '-Inf' :
                    Total_greater_lower = True
                else:
                    if Bin_Total >= eval(self.lower) : Total_greater_lower = True
                    else: Total_greater_lower = False
                
                if Total_less_upper & Total_greater_lower:
                    Pass = 1
                else:
                    Pass = 0
                Binlist.append({'Pass':Pass,
                                'Weff':Weff,
                                'Leff':Leff,
                                'Base':Base,
                                'Bin_L':Bin_L,
                                'Bin_W':Bin_W,
                                'Bin_P':Bin_P,
                                'Bin_Total':Bin_Total
                                })       
        return Binlist