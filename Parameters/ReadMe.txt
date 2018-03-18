注：
    1. 支持读取包含多颗 Mos 模型的文件。识别 .model xxx n/pmos(Hspice Format)。

    2. 遍历所有的 Bsim4 默认参数时，若当前参数在 Model Card 文件中未能找到，则会略过，所以当你的模型文件中缺少某个重要参数时，此软件不会提示。
    
    3. Model 文件中的参数数值可以是纯数值，也可是字符串表达式，但在表达式中，数值必须在其他所有字符串的左边：

        以下情形都可被识别出数值 0.03：                以下情形无法识别出数值 0.03：
        u0 = 0.03                                      u0 = 0.15*2
        u0 = '0.03+du0'                                u0 = '0.15*2' 
        u0 = '0.03*(1+du0)'                            u0 = 'du0+0.03'  
        u0 = '(0.03+du0)*lpeu0'
        u0 = '((0.03)+du0)*lpeu0'

        
    4. 你可以对 /Parameters/Parameters.json 的内容进行增查删改，定制你自己习惯的一套参数集合，但必须严格符合 json 文件的格式，若格式错误，打开软件时
       即会提醒该 json 文件无法解析。
       
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
        
    5. 每个参数的 binType 取决于 Bsim4 Manual 中的定义，已总结至 /参数备份/References/Parameters.xlsx。
    
    6. 所有的输入框都支持四则运算，在计算 corner 参数是否过界时，可直接在已有值的后面添加入偏移量，如“主界面.png”截图所示。
    
    7. 四对 W/L 组合成的尺寸边角，会先进行 Weff/Leff 的计算，再以此进行各 bin 参数有效值的计算。
    
    8. 饼图各部分为相对应有效值的绝对值之间的比例关系，可表征各 bin 参数是否过量。
    
发现任何 Bug 或错误请联系：Grothendieck_Yu@smics.com      