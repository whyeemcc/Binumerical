# Binumerical

![select](/images/logo.png)

为了对 Mos 晶体管更精准地建模，Bsim4 采用了三套模型来计算等效的 Gate length 和 width (BinType1/2/3)。

对应每一个 Gate 尺寸，都需要经过计算得到 leff 和 weff 引入到后续的仿真中，同样对于 binnable 的参数，它的有效值也是由其 binning parameters 和 leff/weff 计算而来，例如 :

u0_binned = u0 + lu0/leff + wu0/weff + pu0/(leff · weff)

本软件通过自定义的参数库，来筛选 Mos 晶体管模型中限定尺寸范围内所有参数的有效值情况，提供可视化的结论，并支持调试运算，以此来帮助建立更加稳定和健壮的晶体管模型。

仅支持 Hspice Format & Bsim4 的模型。

** 主界面

![Interface](/images/Interface.png)


# 功能与特性

1. 支持读取包含多颗 Mos 模型的文件：识别 .model xxx n/pmos(Hspice Format) 字符串。

![select](/images/select_model.png)

2. 遍历 Parameters.json 中所有的 Bsim4 默认参数时，若当前参数在 Model Card 文件中未能找到，则会略过，所以当一个模型文件中缺少某个重要参数时，此软件不会提示，但重新载入到参数列表中的参数将不会包含此项。

3. 四对 W/L 组合成的尺寸边角，会先进行 Weff/Leff 的计算，再以此进行各 bin 参数有效值的计算。Bsim4 的三种 bin 模型如下：

* BinType1

对于大多数的情形，使用该等效形式。

        Wphysical = Ldesigned/NF + XW   (default NF = 1)

        Lphysical = Ldesigned + XL

        δW = WINT + WL/(Lphysical^WLN) + WW/(Wphysical^WWN) + WWL/(Lphysical^WLN · Wphysical^WWN)
        
        δL = LINT + LL/(Lphysical^LLN) + LW/(Wphysical^LWN) + LWL/(Lphysical^LLN · Wphysical^LWN)

        Weff = Wphysical - 2 · δW

        Leff = Lphysical - 2 · δL

        u0_binned = u0 + lu0/Leff + wu0/Weff + pu0/(Leff · Weff)


* BinType2

对于 Mos 的 GIDL/GISL 电流模型以及二极管的 IV/CV 模型，使用该等效形式。

        Wphysical = Ldesigned/NF + XW   (default NF = 1)

        Lphysical = Ldesigned + XL

        δWjct = DWJ + WLC/(Lphysical^WLN) + WWC/(Wphysical^WWN) + WWLC/(Lphysical^WLN · Wphysical^WWN)
        
        δL = LINT + LL/(Lphysical^LLN) + LW/(Wphysical^LWN) + LWL/(Lphysical^LLN · Wphysical^LWN)

        Weffjct = Wphysical - 2 · δWjct

        Leff = Lphysical - 2 · δL

        u0_binned = u0 + lu0/Leff + wu0/Weffjct + pu0/(Leff · Weffjct)


* BinType3

对于 Mos 晶体管的本征和交叠电容模型，使用该等效形式。    
    
        Wphysical = Ldesigned/NF + XW   (default NF = 1)

        Lphysical = Ldesigned + XL

        δWcv = DWC + WLC/(Lphysical^WLN) + WWC/(Wphysical^WWN) + WWLC/(Lphysical^WLN · Wphysical^WWN)
        
        δLcv = DLC + LLC/(Lphysical^LLN) + LWC/(Wphysical^LWN) + LWLC/(Lphysical^LLN · Wphysical^LWN)

        Weffcv = Wphysical - 2 · δWcv

        Leffcv = Lphysical - 2 · δLcv

        u0_binned = u0 + lu0/Leffcv + wu0/Weffcv + pu0/(Leffcv · Weffcv)

4. Model 文件中的参数数值可以是纯数值，也可是字符串表达式，但在表达式中，数值必须在其他所有字符串的左边：

        以下情形都可被识别出数值 0.03：                以下情形无法识别出数值 0.03：
        u0 = 0.03                                      u0 = 0.15*2
        u0 = '0.03+du0'                                u0 = '0.15*2' 
        u0 = '0.03*(1+du0)'                            u0 = 'du0+0.03'  
        u0 = '(0.03+du0)*lpeu0'
        u0 = '((0.03)+du0)*lpeu0'

        
5. 你可以对 /Parameters/Parameters.json 的内容进行增查删改，定制你自己习惯的一套参数集合，但必须严格符合 json 文件的格式，若格式错误，打开软件时即会提醒该 json 文件无法解析。
       
        - 所有字符串必须以 "" 引住。
        - 参数未设定固定的数值上限或数值下限时，必须以 "Inf" 或 "-Inf" 表示（大小写区分）。
        - 若某参数不具有 bin 特性，则 "binable" 和 "binType" 都设置为 "0"，否则 "binable" 设为 "1", "binType" 设为相对应的 "1"/"2"/"3"。
        - 相邻两个参数块之间必须以','间隔。  
        
        例如：
        {
        "level":
                {
                "binable" : "0",
                "binType" : "0",
                "lower" : "54",
                "upper" : "54",
                "default" : "54",
                "abstract" : "Mos model level selector, set to 54 for HSPICE model. together with the keyword NMOS or PMOS specified in the model cards",
                "notice" : ""
                },        
                
                ...
                
        "tcjswg":
                {
                "binable" : "0",
                "binType" : "0",
                "lower" : "-0.004",
                "upper" : "0.004",
                "default" : "0",
                "abstract" : "Temperature-dependence coefficient for CJSWGS and CJSWGD. Default = 0.0 in [V/K].",
                "notice" : ""
                }
        }        
        
    
6. 所有的输入框都支持四则运算，在计算 corner 参数是否过界时，可直接在已有值的后面添加入偏移量，如截图所示。
    
![value_shift](/images/value_shift.png)
    
7. 饼图各部分为相对应有效值的绝对值之间的比例关系，可表征各 bin 参数是否过量。        