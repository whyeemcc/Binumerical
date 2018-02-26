import sys
from PyQt5 import QtGui,QtCore,QtWidgets
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from Layout import Layout
from Help import Help
import images_qr

class Interface(QtWidgets.QMainWindow):

    def __init__(self,parent=None):
        super(Interface, self).__init__(parent)
        self.setupUi() 
        
    def setupUi(self):
        self.widget()
        self.value()
        self.draw()
        self.menu()
        self.layout()    
        self.setAcceptDrops(True)
        # x,y,width,length
        self.setGeometry(200, 100, 1100, 650)
        self.setWindowTitle('Binumerical')
        self.setWindowIcon(QtGui.QIcon(':/images/logo.png')) 
        self.show()

    def widget(self):       
        self.Par_List1   = QtWidgets.QListWidget(self)
        self.Par_List2   = QtWidgets.QListWidget(self)
        self.Edit_Search = QtWidgets.QLineEdit(self)
        self.Edit_Text   = QtWidgets.QTextEdit(self)
        self.Button_Cal  = QtWidgets.QPushButton("计算")
        # set list style
        self.setStyleSheet("QWidget{font-family:Microsoft YaHei}")
        self.Par_List1.setFont(QtGui.QFont('Microsoft YaHei',9, QtGui.QFont.Bold))
        self.Par_List2.setFont(QtGui.QFont('Microsoft YaHei',9, QtGui.QFont.Bold))

    def value(self):
        # W related input box
        self.Edit_Wmax = QtWidgets.QLineEdit(self)
        self.Edit_Wmin = QtWidgets.QLineEdit(self)
        self.Edit_XW   = QtWidgets.QLineEdit(self)
        self.Edit_WINT = QtWidgets.QLineEdit(self)
        self.Edit_WL   = QtWidgets.QLineEdit(self)
        self.Edit_WLN  = QtWidgets.QLineEdit(self)
        self.Edit_WW   = QtWidgets.QLineEdit(self)
        self.Edit_WWN  = QtWidgets.QLineEdit(self)
        self.Edit_WWL  = QtWidgets.QLineEdit(self)
        # L related input box
        self.Edit_Lmax = QtWidgets.QLineEdit(self)
        self.Edit_Lmin = QtWidgets.QLineEdit(self)
        self.Edit_XL   = QtWidgets.QLineEdit(self)
        self.Edit_LINT = QtWidgets.QLineEdit(self)
        self.Edit_LL   = QtWidgets.QLineEdit(self)
        self.Edit_LLN  = QtWidgets.QLineEdit(self)
        self.Edit_LW   = QtWidgets.QLineEdit(self)
        self.Edit_LWN  = QtWidgets.QLineEdit(self)
        self.Edit_LWL  = QtWidgets.QLineEdit(self)
        # base and l/w/p term parameters value box 
        self.Edit_bPar = QtWidgets.QLineEdit(self)
        self.Edit_lPar = QtWidgets.QLineEdit(self)
        self.Edit_wPar = QtWidgets.QLineEdit(self)
        self.Edit_pPar = QtWidgets.QLineEdit(self)
        # parameter name
        self.label_bPar = QtWidgets.QLabel("")     
        self.label_lPar = QtWidgets.QLabel("")     
        self.label_wPar = QtWidgets.QLabel("")     
        self.label_pPar = QtWidgets.QLabel("") 
        self.label_bPar.setFont(QtGui.QFont('Microsoft YaHei',12))
        self.label_lPar.setFont(QtGui.QFont('Microsoft YaHei',12))
        self.label_wPar.setFont(QtGui.QFont('Microsoft YaHei',12))
        self.label_pPar.setFont(QtGui.QFont('Microsoft YaHei',12))
        self.label_bPar.setAlignment(QtCore.Qt.AlignCenter)
        self.label_lPar.setAlignment(QtCore.Qt.AlignCenter)
        self.label_wPar.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pPar.setAlignment(QtCore.Qt.AlignCenter)        
        # calculated value
        self.label_fileNow   = QtWidgets.QLabel("")
        self.label_binable   = QtWidgets.QLabel("")
        self.label_upperPar  = QtWidgets.QLabel("")
        self.label_lowerPar  = QtWidgets.QLabel("")
        self.label_initial   = QtWidgets.QLabel("")
        self.label_binable.setFont(QtGui.QFont('Microsoft YaHei',10))
        self.label_upperPar.setFont(QtGui.QFont('Microsoft YaHei',10))
        self.label_lowerPar.setFont(QtGui.QFont('Microsoft YaHei',10))
        self.label_initial.setFont(QtGui.QFont('Microsoft YaHei',10))
        self.label_binable.setAlignment(QtCore.Qt.AlignCenter)
        self.label_upperPar.setAlignment(QtCore.Qt.AlignCenter)
        self.label_lowerPar.setAlignment(QtCore.Qt.AlignCenter)
        self.label_initial.setAlignment(QtCore.Qt.AlignCenter)
        
        self.label_Wmax  = QtWidgets.QLabel("Wmax")
        self.label_Wmin  = QtWidgets.QLabel("Wmin")
        self.label_XW    = QtWidgets.QLabel("XW")
        self.label_WINT  = QtWidgets.QLabel("WINT")
        self.label_WL    = QtWidgets.QLabel("WL")
        self.label_WLN   = QtWidgets.QLabel("WLN")
        self.label_WW    = QtWidgets.QLabel("WW")
        self.label_WWN   = QtWidgets.QLabel("WWN")
        self.label_WWL   = QtWidgets.QLabel("WWL")

        self.label_Lmax  = QtWidgets.QLabel("Lmax")
        self.label_Lmin  = QtWidgets.QLabel("Lmin")
        self.label_XL    = QtWidgets.QLabel("XL")
        self.label_LINT  = QtWidgets.QLabel("LINT")
        self.label_LL    = QtWidgets.QLabel("LL")
        self.label_LLN   = QtWidgets.QLabel("LLN")
        self.label_LW    = QtWidgets.QLabel("LW")
        self.label_LWN   = QtWidgets.QLabel("LWN")
        self.label_LWL   = QtWidgets.QLabel("LWL")
        
    def draw(self):        
        self.fig = plt.figure(facecolor=('none'))
        self.fig.subplots_adjust(wspace=0.5,hspace=0.8,top=0.95,left=0.05,right=0.95)
        gs = gridspec.GridSpec(3,4)
        self.ax  = self.fig.add_subplot(gs[:2,:])
        self.ax1 = self.fig.add_subplot(gs[2,0])
        self.ax2 = self.fig.add_subplot(gs[2,1])
        self.ax3 = self.fig.add_subplot(gs[2,2])
        self.ax4 = self.fig.add_subplot(gs[2,3]) 
        self.ax.invert_xaxis()
        self.ax.yaxis.tick_right()         
        self.canvas = FigureCanvas(self.fig)      

    def layout(self):
        layout = Layout()
        self.setCentralWidget(layout.wid)
        
        layout.fileFrame.addWidget(QtWidgets.QLabel("当前文件 : "))
        layout.fileFrame.addWidget(self.label_fileNow)
        layout.fileFrame.addStretch()
        layout.searchFrame.addWidget(QtWidgets.QLabel("搜索 :"))
        layout.searchFrame.addWidget(self.Edit_Search)
        # load list 
        layout.listFrame1.addWidget(QtWidgets.QLabel("界内参数 :"))
        layout.listFrame1.addWidget(self.Par_List1)
        layout.listFrame2.addWidget(QtWidgets.QLabel("出界参数 :"))
        layout.listFrame2.addWidget(self.Par_List2)
        # load textEdit
        layout.textFrame.addWidget(self.Edit_Text)
        # load upper and lower bounder
        layout.boundFrame.addStretch()
        for w in [
                  QtWidgets.QLabel("Binable :"),
                  self.label_binable,
                  QtWidgets.QLabel("上限 :"),
                  self.label_upperPar,
                  QtWidgets.QLabel("初始 :"),
                  self.label_initial,
                  QtWidgets.QLabel("下限 :"),
                  self.label_lowerPar
                 ]:
            layout.boundFrame.addWidget(w)
        layout.boundFrame.addStretch()
        layout.boundFrame.setSpacing(20) 
        # load parameter name and value  
        layout.parFrame.addStretch()   
        for w in [
                  self.label_bPar,
                  self.Edit_bPar,
                  self.label_lPar,
                  self.Edit_lPar,
                  self.label_wPar,
                  self.Edit_wPar,
                  self.label_pPar,
                  self.Edit_pPar,
                  self.Button_Cal
                 ]:
            layout.parFrame.addWidget(w)
        layout.parFrame.addStretch()
        #layout.parFrame.setSpacing(20)
        # load w related label
        for w in [
                  self.label_Wmax,
                  self.label_Wmin,
                  self.label_XW,
                  self.label_WINT,
                  self.label_WL,
                  self.label_WLN,
                  self.label_WW,
                  self.label_WWN,
                  self.label_WWL
                 ]:
            layout.W_Label_Frame.addWidget(w)
        # load w related input box     
        for w in [
                  self.Edit_Wmax,
                  self.Edit_Wmin,
                  self.Edit_XW,
                  self.Edit_WINT,
                  self.Edit_WL,
                  self.Edit_WLN,
                  self.Edit_WW,
                  self.Edit_WWN,
                  self.Edit_WWL
                 ]:
            layout.W_Line_Frame.addWidget(w)
        # load l related label    
        for w in [
                  self.label_Lmax,
                  self.label_Lmin,
                  self.label_XL,
                  self.label_LINT,
                  self.label_LL,
                  self.label_LLN,
                  self.label_LW,
                  self.label_LWN,
                  self.label_LWL
                 ]:
            layout.L_Label_Frame.addWidget(w)        
        # load l related input box
        for w in [
                  self.Edit_Lmax,
                  self.Edit_Lmin,
                  self.Edit_XL,
                  self.Edit_LINT,
                  self.Edit_LL,
                  self.Edit_LLN,
                  self.Edit_LW,
                  self.Edit_LWN,
                  self.Edit_LWL
                 ]:
            layout.L_Line_Frame.addWidget(w)          
        # load canvas in canvasFrame
        layout.canvasFrame.addWidget(self.canvas)
        # load bin label in BinFrame
        self.WmaxLmaxResult = QtWidgets.QLabel("")
        self.WmaxLminResult = QtWidgets.QLabel("")
        self.WminLmaxResult = QtWidgets.QLabel("")
        self.WminLminResult = QtWidgets.QLabel("")
        self.WmaxLmaxTotal = QtWidgets.QLabel("")
        self.WmaxLminTotal = QtWidgets.QLabel("")
        self.WminLmaxTotal = QtWidgets.QLabel("")
        self.WminLminTotal = QtWidgets.QLabel("")
        layout.WmaxLmaxFrame.addWidget(self.WmaxLmaxResult)
        layout.WmaxLmaxFrame.addWidget(self.WmaxLmaxTotal)
        layout.WmaxLminFrame.addWidget(self.WmaxLminResult)
        layout.WmaxLminFrame.addWidget(self.WmaxLminTotal)
        layout.WminLmaxFrame.addWidget(self.WminLmaxResult)
        layout.WminLmaxFrame.addWidget(self.WminLmaxTotal)
        layout.WminLminFrame.addWidget(self.WminLminResult)
        layout.WminLminFrame.addWidget(self.WminLminTotal)
        
    def menu(self):
        # add menubar
        menubar = self.menuBar()
        fileMenu    = menubar.addMenu('File')
        #viewMenu    = menubar.addMenu('View')
        aboutMenu   = menubar.addMenu('Help')         
        
        openModel   = QtWidgets.QAction('Load Model File', self)
        openJson    = QtWidgets.QAction('Load Parameters.json', self)
        exitAction  = QtWidgets.QAction('Exit', self)          
        #DrawMode    = QtWidgets.QAction('无图/有图模式切换', self)        
        aboutAction = QtWidgets.QAction('About', self)         
        bin1Action  = QtWidgets.QAction('BinType1', self)         
        bin2Action  = QtWidgets.QAction('BinType2', self)         
        bin3Action  = QtWidgets.QAction('BinType3', self)         

        fileMenu.addAction(openModel)
        fileMenu.addAction(openJson)     
        fileMenu.addAction(exitAction)         
        #viewMenu.addAction(DrawMode) 
        aboutMenu.addAction(aboutAction)  
        aboutMenu.addAction(bin1Action)  
        aboutMenu.addAction(bin2Action)  
        aboutMenu.addAction(bin3Action)  
        
        openModel.triggered.connect(self.showDialog)
        openJson.triggered.connect(self.initiate) 
        exitAction.triggered.connect(QtWidgets.qApp.quit)          
        #DrawMode.triggered.connect(self.DrawMode)   
        aboutAction.triggered.connect(self.about)         
        bin1Action.triggered.connect(self.bin1)  
        bin2Action.triggered.connect(self.bin2)  
        bin3Action.triggered.connect(self.bin3)  
          
    def about(self):
        QtWidgets.QMessageBox.about(self,"About",Help.about)
    def bin1(self):
        QtWidgets.QMessageBox.about(self,"BinType1",Help.BinType1)        
    def bin2(self):
        QtWidgets.QMessageBox.about(self,"BinType2",Help.BinType2)        
    def bin3(self):
        QtWidgets.QMessageBox.about(self,"BinType3",Help.BinType3)        

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self,'Message',"确认要退出吗?", 
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    # drag the file to mainwindow ---start
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super(Interface, self).dragEnterEvent(event)

    def dragMoveEvent(self, event):
        super(Interface, self).dragMoveEvent(event)

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            # event.mimeData().urls() is a list contain all file that dragged in
            fname = event.mimeData().urls()[0].toLocalFile()
            self.openFile(fname)
            event.acceptProposedAction()
        else:
            super(Interface,self).dropEvent(event)  
    # drag the file to mainwindow ---end

    def showDialog(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self,'载入模型文件','/.pm')[0]
        self.openFile(fname)

    def initiate(self):
        # re-write in subclass 
        pass

    def DrawMode(self):
        # re-write in subclass 
        pass

    def openFile(self,fname):
        # re-write in subclass
        pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Interface()
    sys.exit(app.exec_())