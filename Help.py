class Help:
    about = '''
为了对 Mos 晶体管更精准地建模，Bsim4 采用了三套模型来计算等效的 Gate length 和 width (BinType1/2/3)。

对应每一个 Gate 尺寸，都需要经过计算得到 leff 和 weff 引入到后续的仿真中，同样对于 binnable 的参数，它的有效值也是由其 binning parameters 和 leff/weff 计算而来，例如 :

u0_binned = u0 + lu0/leff + wu0/weff + pu0/(leff · weff)

本软件通过自定义的参数库，来筛选 Mos 晶体管模型中限定尺寸范围内所有参数的有效值情况，提供可视化的结论，并支持调试运算，以此来帮助建立更加稳定和健壮的晶体管模型。

仅支持 Hspice Format & Bsim4 的模型。

如有Bug，请联系：
Author: whyeemcc
Mail: whyeemcc@gmail.com
'''

    BinType1 = '''
对于大多数的情形，使用该等效形式。

Wphysical = Ldesigned/NF + XW   (default NF = 1)
Lphysical  = Ldesigned + XL

δW = WINT + 
         WL/(Lphysical^WLN) + 
         WW/(Wphysical^WWN) + 
         WWL/(Lphysical^WLN · Wphysical^WWN)
      
δL = LINT + 
        LL/(Lphysical^LLN) + 
        LW/(Wphysical^LWN) + 
        LWL/(Lphysical^LLN · Wphysical^LWN)

Weff = Wphysical - 2 · δW
Leff  = Lphysical - 2 · δL

u0_binned = u0 + lu0/Leff + wu0/Weff + pu0/(Leff · Weff)
'''

    BinType2 = '''
对于 Mos 的 GIDL/GISL 电流模型以及二极管的 IV/CV 模型，使用该等效形式。

Wphysical = Ldesigned/NF + XW   (default NF = 1)
Lphysical  = Ldesigned + XL

δWjct = DWJ + 
             WLC/(Lphysical^WLN) + 
             WWC/(Wphysical^WWN) + 
             WWLC/(Lphysical^WLN · Wphysical^WWN)
      
δL = LINT + 
        LL/(Lphysical^LLN) + 
        LW/(Wphysical^LWN) + 
        LWL/(Lphysical^LLN · Wphysical^LWN)

Weffjct = Wphysical - 2 · δWjct
Leff      = Lphysical - 2 · δL

u0_binned = u0 + lu0/Leff + wu0/Weffjct + pu0/(Leff · Weffjct)
'''

    BinType3 = '''
对于 Mos 晶体管的本征和交叠电容模型，使用该等效形式。    
    
Wphysical = Ldesigned/NF + XW   (default NF = 1)
Lphysical  = Ldesigned + XL

δWcv = DWC + 
            WLC/(Lphysical^WLN) + 
            WWC/(Wphysical^WWN) + 
            WWLC/(Lphysical^WLN · Wphysical^WWN)
      
δLcv = DLC + 
           LLC/(Lphysical^LLN) + 
           LWC/(Wphysical^LWN) + 
           LWLC/(Lphysical^LLN · Wphysical^LWN)

Weffcv = Wphysical - 2 · δWcv
Leffcv  = Lphysical - 2 · δLcv

u0_binned = u0 + lu0/Leffcv + wu0/Weffcv + pu0/(Leffcv · Weffcv)
'''