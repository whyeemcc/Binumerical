import sys,os
from PyQt5 import QtGui,QtCore,QtWidgets
from Ui import Interface
from Select import Select
from Hunter import Hunter
from Calculate import Cal
from Visualize import BinVisualize

class Main(Interface):

    def __init__(self,parent=None):
        super(Main, self).__init__(parent)
        self.stateCheck()
        self.initiate()        

    def initiate(self):
        # initial flags
        self.mode = 0
        self.binType_temp = '0'        
        self.binType = '1'
        # parse Parameters.json
        self.label_fileNow.setText('Parameters.json')
        self.Par_List1.clear()
        self.Par_List2.clear()
        # define an empty list prepare to load model's parameters
        self.Par_List1_tem = []
        self.Par_List2_tem = []          
        import json
        try:
            path = os.path.split(sys.argv[0])[0]
            with open(path + '/Parameters/Parameters.json', 'r') as f:
                self.data = json.load(f)
                
                geolist = ['Wmax','Wmin','XW','WINT','WL','WLN','WW','WWN','WWL','Lmax','Lmin','XL','LINT','LL','LLN','LW','LWN','LWL',
                        'DWJ','DLC','DWC','WLC','WWC','WWLC','LLC','LWC','LWLC']
                self.GeoDic = {x:self.data[x.lower()]['default'] for x in geolist}
                self.setGeo()
            
            for par in self.data:
                self.Par_List1.addItem(par)   
            self.reShow()
        except:
            self.fig.clear()
            QtWidgets.QMessageBox.critical(self,'Warning','Parameters.json 文件解析失败！')            
            exit()
            
    def geoName(self):
        if self.binType_temp == '1':
            return ['Wmax','Wmin','XW','WINT','WL','WLN','WW','WWN','WWL',
                    'Lmax','Lmin','XL','LINT','LL','LLN','LW','LWN','LWL']
        elif self.binType_temp == '2':
            return ['Wmax','Wmin','XW','DWJ','WLC','WLN','WWC','WWN','WWLC',
                    'Lmax','Lmin','XL','LINT','LL','LLN','LW','LWN','LWL']   
        elif self.binType_temp == '3':
            return ['Wmax','Wmin','XW','DWC','WLC','WLN','WWC','WWN','WWLC',
                    'Lmax','Lmin','XL','DLC','LLC','LLN','LWC','LWN','LWLC']
                    
    def setGeo(self):
        # set Geometry information both default json and particular model file
        if self.binType != self.binType_temp:
            
            self.binType_temp = self.binType  
            GeoName = self.geoName()

            GeoLabel = [self.label_Wmax,
                        self.label_Wmin,
                        self.label_XW,
                        self.label_WINT,
                        self.label_WL,
                        self.label_WLN,
                        self.label_WW,
                        self.label_WWN,
                        self.label_WWL,
                        self.label_Lmax,
                        self.label_Lmin,
                        self.label_XL,
                        self.label_LINT,
                        self.label_LL,
                        self.label_LLN,
                        self.label_LW,
                        self.label_LWN,
                        self.label_LWL]
                           
            GeoEdit  = [self.Edit_Wmax,
                        self.Edit_Wmin,
                        self.Edit_XW,
                        self.Edit_WINT,
                        self.Edit_WL,
                        self.Edit_WLN,
                        self.Edit_WW,
                        self.Edit_WWN,
                        self.Edit_WWL,
                        self.Edit_Lmax,
                        self.Edit_Lmin,
                        self.Edit_XL,
                        self.Edit_LINT,
                        self.Edit_LL,
                        self.Edit_LLN,
                        self.Edit_LW,
                        self.Edit_LWN,
                        self.Edit_LWL]
            
            for label,edit,name in zip(GeoLabel,GeoEdit,GeoName):
                label.setText(name)
                edit.setText(self.GeoDic[name])
        else:
            pass
            
    def justDoIt(self,listWidget):
        
        if listWidget.currentRow() == -1:
            # currenRow is -1 as the list is empty
            pass
        else:
            currentItem = listWidget.currentItem().text()
            dic = self.data[currentItem]
            self.label_bPar.setText(currentItem)
            self.label_upperPar.setText(dic['upper'])
            self.label_lowerPar.setText(dic['lower'])
            self.label_initial.setText(dic['default'])       
            
            if dic['binable'] == '1':
                self.label_binable.setText('Yes')
                self.binType = dic['binType']
                self.label_lPar.setText('l'+currentItem)
                self.label_wPar.setText('w'+currentItem)
                self.label_pPar.setText('p'+currentItem)
            else:
                self.label_binable.setText('No')  
                self.binType = '1'
                self.label_lPar.setText('')
                self.label_wPar.setText('')
                self.label_pPar.setText('')   

            self.setGeo()

            if self.mode == 0:
                self.Edit_bPar.setText(dic['default'])
                self.Edit_wPar.setText('')
                self.Edit_lPar.setText('')
                self.Edit_pPar.setText('')
            elif self.mode == 1:
                self.Edit_bPar.setText(self.hunter.catch(currentItem))            
                if dic['binable'] == '1':
                    self.Edit_lPar.setText(self.hunter.catch('l'+currentItem))
                    self.Edit_wPar.setText(self.hunter.catch('w'+currentItem))
                    self.Edit_pPar.setText(self.hunter.catch('p'+currentItem))            
                else:
                    self.Edit_lPar.setText('')
                    self.Edit_wPar.setText('')
                    self.Edit_pPar.setText('')                     
            self.Edit_Text.setText('● Abstract :\n%s\n\n'%dic['abstract']+
                                   '● Notice :\n%s'%dic['notice'])
            self.bin_cal()

    def bin_cal(self):
        list = self.collectGeo() + self.collectVal()
        cal = Cal(list)
       
        try:
            BinList = cal.result()
            
            pe1 = QtGui.QPalette()
            pe2 = QtGui.QPalette()
            pe1.setColor(QtGui.QPalette.WindowText,QtCore.Qt.blue)
            pe2.setColor(QtGui.QPalette.WindowText,QtCore.Qt.red)   

            for i,(Frame,Total) in enumerate([(self.WmaxLmaxResult,self.WmaxLmaxTotal),
                                              (self.WmaxLminResult,self.WmaxLminTotal),
                                              (self.WminLmaxResult,self.WminLmaxTotal),
                                              (self.WminLminResult,self.WminLminTotal)]):

                Frame.setText('Weff  = %s\n'%self.norm(BinList[i]['Weff'])  +
                              'Leff   = %s\n'%self.norm(BinList[i]['Leff']) +
                              'Base   = %s\n'%self.norm(BinList[i]['Base']) +
                              'Bin_L  = %s\n'%self.norm(BinList[i]['Bin_L'])+
                              'Bin_W = %s\n'%self.norm(BinList[i]['Bin_W']) +
                              'Bin_P  = %s'%self.norm(BinList[i]['Bin_P'])
                              )
                Total.setText('Bin_Total = ' + self.norm(BinList[i]['Bin_Total']))
                if BinList[i]['Pass'] == 1:
                    Total.setPalette(pe1)        
                else:
                    Total.setPalette(pe2)
            # draw the canvas
            self.showIt(BinList)
            
        except ZeroDivisionError:
            QtWidgets.QMessageBox.critical(self,'Warning','Weff or Leff 为 0！')


    def getVaule(self,lineEdit):
        if lineEdit == '':
            return 0
        else:
            try:
                return eval(lineEdit)
            except:
                QtWidgets.QMessageBox.critical(self,'Warning','%s 不可计算，返回 0'%lineEdit)
                return 0
    
    def collectGeo(self):
        # take the geometry numbers back to cal the effective values
        Wmax = self.getVaule(self.Edit_Wmax.text())
        Wmin = self.getVaule(self.Edit_Wmin.text())
        XW   = self.getVaule(self.Edit_XW.text())
        WINT = self.getVaule(self.Edit_WINT.text())
        WL   = self.getVaule(self.Edit_WL.text()) 
        WLN  = self.getVaule(self.Edit_WLN.text()) 
        WW   = self.getVaule(self.Edit_WW.text()) 
        WWN  = self.getVaule(self.Edit_WWN.text())
        WWL  = self.getVaule(self.Edit_WWL.text())
        Lmax = self.getVaule(self.Edit_Lmax.text())  
        Lmin = self.getVaule(self.Edit_Lmin.text())
        XL   = self.getVaule(self.Edit_XL.text())
        LINT = self.getVaule(self.Edit_LINT.text())
        LL   = self.getVaule(self.Edit_LL.text())
        LLN  = self.getVaule(self.Edit_LLN.text())
        LW   = self.getVaule(self.Edit_LW.text())
        LWN  = self.getVaule(self.Edit_LWN.text()) 
        LWL  = self.getVaule(self.Edit_LWL.text())
        return [Wmax,Wmin,XW,WINT,WL,WLN,WW,WWN,WWL,Lmax,Lmin,XL,LINT,LL,LLN,LW,LWN,LWL]
    
    def collectVal(self):
        # take the parameter numbers back to cal the effective values
        Base   = self.getVaule(self.Edit_bPar.text())
        if self.label_binable.text() == 'Yes':
            Lvalue = self.getVaule(self.Edit_lPar.text())
            Wvalue = self.getVaule(self.Edit_wPar.text())
            Pvalue = self.getVaule(self.Edit_pPar.text())
        else:
            Lvalue = 0 
            Wvalue = 0
            Pvalue = 0
            self.Edit_lPar.setText('')
            self.Edit_wPar.setText('')
            self.Edit_pPar.setText('')
        # consider the 'Inf/-Inf' instance, not use self.getVaule
        upper = self.label_upperPar.text()
        lower = self.label_lowerPar.text()        
        return [Base,Lvalue,Wvalue,Pvalue,upper,lower]

    def norm(self,value):
        # display regularly
        if abs(value) > 1e4 or 0 < abs(value) < 1e-3:
            return '%.2e'%value
        else:
            return str(round(value,4))            
            
    def showIt(self,binlist):
        self.thread = BinVisualize(self.ax,self.ax1,self.ax2,self.ax3,self.ax4,binlist)
        self.thread.finishSignal.connect(self.canvas.draw)
        self.thread.start()

    def openFile(self,fname):  
        if fname == '':
            # nothing opened
            pass
        else:
            try:
                slt = Select(fname)
                if slt.count == 0:
                    QtWidgets.QMessageBox.warning(self,'提示','该文件不包含 Mos Device.')            
                else:
                    if slt.count == 1:
                        dv_name = slt.dvc_list[0]
                        self.model = slt.extract(dv_name)
                        ok = True
                    else:
                        items = slt.dvc_list  
                        dv_name,ok = QtWidgets.QInputDialog.getItem(self,"选择","请选择 Device :", items,0,False) 
                        self.model = slt.extract(dv_name)
                    if ok == False:
                        pass
                    elif ok == True:
                        self.mode = 1
                        self.label_fileNow.setText(os.path.split(fname)[1] + '     当前 Device : ' + dv_name)
                        self.Edit_Search.setText('')  
                        self.hunter = Hunter(self.model)
                        self.GeoDic = self.hunter.geometry()
                        self.binType_temp = '0'
                        self.binType = '1'
                        self.scanPar(self.model)            
            except:
                QtWidgets.QMessageBox.critical(self,"Error","解析数据失败，请检查文件格式。")

    def scanPar(self,model):
        # only work in the condition of self.mode=1 
        self.Par_List1.clear()
        self.Par_List2.clear()        
        # refresh the list
        self.Par_List1_tem = []
        self.Par_List2_tem = []     
        
        self.setGeo()
        
        progress = QtWidgets.QProgressDialog(self)
        progress.setRange(0,len(self.data)-1)
        progress.setWindowTitle("Processing...")         
        progress.setMinimumDuration(4)
        progress.setWindowModality(QtCore.Qt.WindowModal)
        
        for i,par in enumerate(self.data):
        
            progress.setValue(i)
            if progress.wasCanceled():
                QtWidgets.QMessageBox.warning(self,"提示","操作失败") 
                break       
                
            Base = self.hunter.catch(par)
            if Base == '':
                # not found in the model file
                continue
            else:
                dic = self.data[par]
                
                Base = self.getVaule(Base)
                if dic['binable'] == '1':
                    self.binType_temp = dic['binType']
                    Lvalue = self.getVaule(self.hunter.catch('l'+par))
                    Wvalue = self.getVaule(self.hunter.catch('w'+par))
                    Pvalue = self.getVaule(self.hunter.catch('p'+par))
                else:
                    self.binType_temp = '1'
                    Lvalue = 0
                    Wvalue = 0
                    Pvalue = 0
                upper = dic['upper']
                lower = dic['lower']

                GeoName = self.geoName()
                half = [self.getVaule(self.GeoDic[x]) for x in GeoName]
                
                cal = Cal(half + [Base,Lvalue,Wvalue,Pvalue,upper,lower])        
                BinList = cal.result()
                
                if 0 in [x['Pass'] for x in BinList]:
                    # out of the boundary
                    self.Par_List2.addItem(par)
                    self.Par_List2_tem.append(par)
                else:
                    # in the boundary
                    self.Par_List1.addItem(par)
                    self.Par_List1_tem.append(par)
        self.reShow()
        
    def search(self):
        self.Par_List1.clear()
        self.Par_List2.clear()
        key = self.Edit_Search.text()
        if self.mode == 0:
            for par in self.data:
                if key in par : self.Par_List1.addItem(par)
        elif self.mode == 1:
            for par in self.Par_List1_tem:
                if key in par : self.Par_List1.addItem(par)
            for par in self.Par_List2_tem:
                if key in par : self.Par_List2.addItem(par)

    def reShow(self):
        self.Par_List1.setCurrentRow(0)
        self.justDoIt(self.Par_List1)

    def doIt1(self):
        self.justDoIt(self.Par_List1)

    def doIt2(self):
        self.justDoIt(self.Par_List2)

    def stateCheck(self):
        # signals and slots
        self.Edit_Search.textChanged.connect(self.search)
        self.Edit_Search.returnPressed.connect(self.reShow)
        self.Par_List1.clicked.connect(self.doIt1)                
        self.Par_List2.clicked.connect(self.doIt2)
        self.Par_List1.itemActivated.connect(self.doIt1)        
        self.Par_List2.itemActivated.connect(self.doIt2)        
        self.Button_Cal.clicked.connect(self.bin_cal)
        for edit in [self.Edit_Wmax,self.Edit_Wmin,
                     self.Edit_XW,self.Edit_WINT,
                     self.Edit_WL,self.Edit_WLN,
                     self.Edit_WW,self.Edit_WWN,
                     self.Edit_WWL,
                     self.Edit_Lmax,self.Edit_Lmin,
                     self.Edit_XL,self.Edit_LINT,
                     self.Edit_LL,self.Edit_LLN,
                     self.Edit_LW,self.Edit_LWN,
                     self.Edit_LWL,
                     self.Edit_bPar,self.Edit_wPar,
                     self.Edit_lPar,self.Edit_pPar
                    ]:
            edit.returnPressed.connect(self.bin_cal)
       
       
if __name__ == '__main__':       
    app = QtWidgets.QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())