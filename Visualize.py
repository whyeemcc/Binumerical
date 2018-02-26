from PyQt5 import QtCore
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.patches import Circle,Rectangle
        
class BinVisualize(QtCore.QThread):
    # return a signal as self.run is over
    finishSignal  = QtCore.pyqtSignal()
    
    def __init__(self,ax,ax1,ax2,ax3,ax4,BinList,parent=None):
        super(BinVisualize, self).__init__(parent)
        ax.clear()
        ax1.clear()
        ax2.clear()
        ax3.clear()
        ax4.clear()  
        self.ax  = ax
        self.ax1 = ax1
        self.ax2 = ax2
        self.ax3 = ax3
        self.ax4 = ax4       
        self.BinList = BinList

    def __del__(self):
        self.exiting = True
        self.wait()

    def run(self):    
        Wmax,Wmin,Lmax,Lmin = 5,1,3,1  
        self.ax.add_patch(Rectangle((1, 1),4,2,fill=False))      
        color = {1:'blue',0:'red'}
        labels = 'B', 'W', 'L', 'P'
        for i,(x,W,L) in enumerate([(self.ax1,Wmax,Lmax),
                                    (self.ax2,Wmax,Lmin),
                                    (self.ax3,Wmin,Lmax),
                                    (self.ax4,Wmin,Lmin)]):
            dic = self.BinList[i]
            Pass = dic['Pass']
            self.ax.add_patch(Circle(xy = (W,L), radius=0.15, color=color[Pass]))
            B = abs(dic['Base'])
            W = abs(dic['Bin_W'])
            L = abs(dic['Bin_L'])
            P = abs(dic['Bin_P'])
            Sum = B+W+L+P
            if Sum == 0:
                B,W,L,P = 1/4,1/4,1/4,1/4
            else:
                B,W,L,P = B/Sum,W/Sum,L/Sum,P/Sum
            x.pie(x=[B,W,L,P],colors=('orange','dodgerblue', 'red','forestgreen' ),labels=labels,startangle = 90)
            x.set_xlabel(('Wmax,Lmax','Wmax,Lmin','Wmin,Lmax','Wmin,Lmin')[i])
            x.axis('scaled')
        
        self.style()
        self.finishSignal.emit()

    def style(self):
        self.ax.patch.set_facecolor("none")
        self.ax.spines['right'].set_visible(False)
        self.ax.spines['left'].set_visible(False)
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['bottom'].set_visible(False)
        self.ax.axis('scaled')
        try:
            #self.ax.set_xticks((5,1))  
            #self.ax.set_yticks((1,3))  
            self.ax.set_xticklabels(('','Wmin','','','','Wmax'))  
            self.ax.set_yticklabels(('','Lmin','','','','Lmax'))  
        except:
            pass