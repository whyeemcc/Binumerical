from PyQt5 import QtWidgets

class Layout:
    def __init__(self): 
        self.wid = QtWidgets.QWidget()
        # self.setCentralWidget(wid)
        self.mainFrame = QtWidgets.QVBoxLayout()
        self.wid.setLayout(self.mainFrame)
        '''
                 ---------------
                |               |
                |               |
                |               | 
          wid   |   mainFrame   |
                |               |
                |               |
                |               |
                 ---------------    
        '''
        
        # define layout
        self.fileFrame = QtWidgets.QHBoxLayout()
        self.remainFrame = QtWidgets.QHBoxLayout()
        # load layout
        self.mainFrame.addLayout(self.fileFrame)
        self.mainFrame.addLayout(self.remainFrame)
        self.mainFrame.addStretch()        
        '''
                 ------------------
                |  --------------  |
                | |   fileFrame  | |
                |  --------------  |
                |  --------------  |
      mainFrame | |              | |         ^
                | |  remainFrame | |         |
                | |              | |
                | |              | |
                |  --------------  |
                 ------------------       
        '''     
        
        # define layout        
        self.leftFrame = QtWidgets.QVBoxLayout()
        self.middleFrame = QtWidgets.QVBoxLayout()
        self.rightFrame = QtWidgets.QVBoxLayout()
        # load layout        
        self.remainFrame.addLayout(self.leftFrame)
        self.remainFrame.addLayout(self.middleFrame)
        self.remainFrame.addLayout(self.rightFrame)
        self.remainFrame.setStretchFactor(self.leftFrame,2)
        self.remainFrame.setStretchFactor(self.middleFrame,2)
        self.remainFrame.setStretchFactor(self.rightFrame,7)
        '''
                 -------------------------------
                |  -------   -------   -------  |
                | |       | |       | |       | |
                | | left  | | middle| | right | |
    remainFrame | | Frame | | Frame | | Frame | |          <-
                | |       | |       | |       | |
                | |       | |       | |       | |
                | |       | |       | |       | |
                |  -------   -------   -------  |
                 ------------------------------- 
        '''      

        # define layouts in leftFrame
        self.searchFrame = QtWidgets.QHBoxLayout()   
        self.listFrame = QtWidgets.QHBoxLayout()   
        # load layouts in leftFrame 
        self.leftFrame.addLayout(self.searchFrame)   
        self.leftFrame.addLayout(self.listFrame)
        #self.leftFrame.addStretch()

        '''
                 ------------------
                |  --------------  |    
                | | searchFrame  | | 
                |  --------------  | 
                |  --------------  |              ^
      leftFrame | |              | |              |
                | |              | |              
                | |              | |              
                | |  listFrame   | |
                | |              | |
                | |              | |
                | |              | |
                | |              | |
                |  --------------  |       
                 ------------------  
        '''
        
        
        
        self.listFrame1 = QtWidgets.QVBoxLayout()  
        self.listFrame2 = QtWidgets.QVBoxLayout()  
        self.listFrame.addLayout(self.listFrame1)
        self.listFrame.addLayout(self.listFrame2)
        
        '''      -----------------------
                |  --------   --------  |
                | |        | |        | |
                | |        | |        | |
                | |        | |        | |
                | | list   | | list   | |
                | | Frame1 | | Frame2 | | 
                | |        | |        | |
    listFrame   | |        | |        | |            <-
                | |        | |        | |
                | |        | |        | |
                | |        | |        | |
                | |        | |        | |
                | |        | |        | |
                |  --------   --------  |
                 -----------------------
        '''        
        
        
        # define layouts in middleFrame        
        self.textFrame = QtWidgets.QVBoxLayout()  
        self.MDFrame = QtWidgets.QHBoxLayout()
        # load layouts in middleFrame
        self.middleFrame.addStretch()         
        self.middleFrame.addLayout(self.textFrame)  
        self.middleFrame.addStretch()         
        self.middleFrame.addLayout(self.MDFrame)  
        
        
        
        
        '''      --------------------
                |  ----------------  |
                | |                | |
                | |                | |
                | |   textFrame    | |
                | |                | |
                |  ----------------  |  
                |  ----------------  |         
   middleFrame  | |                | |  
                | |                | |
                | |                | |
                | |   parFrame     | |
                | |                | |
                | |                | |
                |  ----------------  |
                 --------------------
        '''          
        
        # define layouts in parFrame         
        self.boundFrame = QtWidgets.QVBoxLayout()
        self.parFrame = QtWidgets.QVBoxLayout()        
        # load layouts in parFrame        
        self.MDFrame.addLayout(self.boundFrame)  
        self.MDFrame.addLayout(self.parFrame)  
        self.MDFrame.setStretchFactor(self.boundFrame,1)
        self.MDFrame.setStretchFactor(self.parFrame,1)
        '''
                 --------------------- 
                |  -------   -------  |
                | |       | |       | |
     MDFrame    | | bound | |  par  | |
                | | Frame | | Frame | |
                | |       | |       | | 
                | |       | |       | | 
                | |       | |       | |
                |  -------   -------  |
                 ---------------------          
              
        '''        
        
        
        # define layouts in rightFrame 
        self.GoemetryFrame = QtWidgets.QVBoxLayout()     
        self.canvasFrame = QtWidgets.QVBoxLayout()     
        self.BinFrame = QtWidgets.QHBoxLayout() 
        # laod layout in rightFrame  
        self.rightFrame.addLayout(self.GoemetryFrame)
        self.rightFrame.addLayout(self.canvasFrame)
        self.rightFrame.addLayout(self.BinFrame)
        self.rightFrame.addStretch()
        '''
        
        
                 ------------------------------- 
                |  --------------------------   |
                | |       GoemetryFrame      |  |
                |  --------------------------   | 
                |  ---------------------------  |
                | |                           | |
     rightFrame | |                           | |
                | |        canvasFrame        | |       ^
                | |                           | |       |
                | |                           | | 
                | |                           | |
                |  ---------------------------  |
                |  ---------------------------  |
                | |                           | |
                | |                           | |
                | |        BinFrame           | |
                | |                           | |
                | |                           | |
                | |                           | |
                |  ---------------------------  |
                 -------------------------------
        
        '''
        # define layouts in GoemetryFrame 
        self.W_Label_Frame = QtWidgets.QHBoxLayout()
        self.W_Line_Frame = QtWidgets.QHBoxLayout()
        self.L_Label_Frame = QtWidgets.QHBoxLayout()
        self.L_Line_Frame = QtWidgets.QHBoxLayout()
        # layout load widgets              
        self.GoemetryFrame.addLayout(self.W_Label_Frame)
        self.GoemetryFrame.addLayout(self.W_Line_Frame)
        self.GoemetryFrame.addLayout(self.L_Label_Frame)
        self.GoemetryFrame.addLayout(self.L_Line_Frame)
        self.GoemetryFrame.addStretch()

        '''
                 ------------------------ 
                |  --------------------  |
                | | self.W_Label_Frame | | 
                |  --------------------  | 
                |  --------------------  |
 GoemetryFrame  | | self.W_Line_Frame |  | 
                |  --------------------  |        
                |  --------------------  |
                | | self.L_Label_Frame | |              ^
                |  --------------------  |              |
                |  --------------------  |
                | | self.L_Line_Frame  | |              
                |  --------------------  | 
                 ------------------------ 
                                    
        '''
        
        # define layouts in BinFrame 
        self.WmaxLmaxFrame = QtWidgets.QVBoxLayout()
        self.WmaxLminFrame = QtWidgets.QVBoxLayout()
        self.WminLmaxFrame = QtWidgets.QVBoxLayout()
        self.WminLminFrame = QtWidgets.QVBoxLayout()
        # layout load widgets in BinFrame 
        self.BinFrame.addStretch()
        self.BinFrame.addLayout(self.WmaxLmaxFrame)
        self.BinFrame.addStretch()         
        self.BinFrame.addLayout(self.WmaxLminFrame)
        self.BinFrame.addStretch()            
        self.BinFrame.addLayout(self.WminLmaxFrame) 
        self.BinFrame.addStretch()            
        self.BinFrame.addLayout(self.WminLminFrame)
        self.BinFrame.addStretch()        

        '''         
              ---------------------------------------------- 
             |  --------   --------   --------   --------   |
             | |        | |        | |        | |        |  |
             | |  Wmax  | |  Wmax  | |  Wmin  | |  Wmin  |  |
             | |  Lmax  | |  Lmin  | |  Lmax  | |  Lmin  |  |
 BinFrame    | |        | |        | |        | |        |  |
             | |        | |        | |        | |        |  |
             | |        | |        | |        | |        |  |
             | |        | |        | |        | |        |  |
             | |        | |        | |        | |        |  |
             |  --------   --------   --------   --------   |
              ---------------------------------------------- 
        '''
