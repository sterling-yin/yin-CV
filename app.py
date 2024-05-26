from pathlib import Path

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.jpg"
map = current_dir / "assets" / "map.png"
lineage = current_dir / "assets" / "lineage.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "CV | Xing YIN, PhD"
PAGE_ICON = ":star:"
NAME = "Xing YIN  银星"
DESCRIPTION = """
Doctor of Philosophy  工学博士     
Postdoctoral Fellow at ***Zhejiang University***      
浙江大学建筑工程学院博士后、助理研究员          
**Member of Academician Shilang Xu's Lab**             
浙江大学高性能结构研究所徐世烺院士团队成员

> *Looking for a Postdoctoral / Visiting Scholar Position ...*
"""
EMAIL = "yinxing@zju.edu.cn"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=300)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write("📧", EMAIL)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["🌟Introduction", "🎖️Featured Publications", "📑Publications List", "🏛️Academic Lineage", "🗄️Codes"])

with tab1:
# --- Biography ---
   st.write('\n')
   st.subheader("Biography")
   st.write("""
I was born in Baotou, Inner Mongolia, China. I received my BEng degree from the *Ocean University of China* in 2017. I pursued further study at the *Zhejiang University* under the supervision of academician Prof. Shilang Xu, and obtained my PhD degree in 2023.

My research focuses on ***Impact Dynamics***, and I have authored/co-authored 16 papers from SCI journals such as *CCC*, *CCR*, *CS*, *ES*, *IJIE*, *IJMS*, *IJSS*, *EFM*, with two papers recognized as ESI Highly Cited Papers.

银星，1995年9月出生于内蒙古自治区包头市。长期专注于先进建筑结构与材料**冲击动力学**研究，在工程材料领域的Cem. Concr. Compos.、Cem. Concr. Res.，结构工程领域的Compos. Struct.、Eng. Struct.，力学领域的Int. J. Mech. Sci.、Int. J. Solids Struct.、Eng. Fract. Mech.、Int. J. Impact Eng.等期刊发表高水平SCI论文16篇，其中2篇曾入选ESI高被引论文。    
""")

# --- EXPERIENCE & QUALIFICATIONS ---
   st.write('\n')
   st.subheader("Research Interests")
   st.write(
    """
📌 Dynamic mechanics behaviours of engineering materials [e.g., dynamic compression, dynamic fracture, and spallation, etc.]        
工程材料的动态力学行为，如动态压缩、动态断裂、层裂等    

📌 Dynamic response of engineering structures [e.g., low-velocity impact, explosion, and penetration, etc.]        
工程结构的动态力学响应，如低速冲击、爆炸、侵彻等      

📌 Constitutive models of cementitious materials [e.g., KCC, CSC, and RHT, etc.]      
水泥基材料本构关系，如KCC、CSC、RHT等        

📌 Advanced numerical approach [e.g., meshfree/particle method]      
先进高保真数值分析方法，如无网格法/粒子法
"""
)

# --- Education & Work ---
   st.write('\n')
   st.subheader("Education & Work")
   st.write(
    """
⭐ Postdoctoral Fellow, 2023.10-, College of Civil Engineering and Architecture, ***Zhejiang University*** (Supervisor: Prof. Qinghua Li)      
博士后、助理研究员，2023.10-，浙江大学，建筑工程学院，合作导师为国家杰青李庆华教授    

⭐ PhD, 2017.9-2023.9, Structural Engineering, ***Zhejiang University***, Hangzhou, China (Supervisor: Academician Prof. Shilang Xu)       
博士研究生，2017.9-2023.9，浙江大学，结构工程专业，导师为中国科学院院士徐世烺教授  

⭐ BEng, 2013.8-2017.6, Civil Engineering, ***Ocean University of China***, Qingdao, China          
本科，2013.8-2017.6，中国海洋大学，土木工程专业    
"""
)

# --- Publication trend ---
   st.write('\n')
   st.subheader("Publication Trend")
   data = {
       'Year': [2021, 2022, 2023, 2024],
       'Publication': [3, 4, 7, 3]
   }
   df = pd.DataFrame(data)
   df.set_index('Year', inplace=True)
   st.bar_chart(df, y = "Publication")

# ---  Geographic Citation Map ---
   map = Image.open(map)
   st.write('\n')
   st.subheader("Geographic Citation Map")
   st.image(map)

with tab2:
# --- Selected Publications ---

   Publications1 = {
    "► An improved calibration of Karagozian & Case concrete/cementitious model for strain-hardening fibre-reinforced cementitious composites under explosion and penetration loadings. Cement and Concrete Composites. 2023;137:104911.": "https://www.doi.org/10.1016/j.cemconcomp.2022.104911",
    "► Investigation of continuous surface cap model (CSCM) for numerical simulation of strain-hardening fibre-reinforced cementitious composites against low-velocity impacts. Composite Structures. 2023;304:116424.": "https://www.doi.org/10.1016/j.compstruct.2022.116424",
}

   Publications2 = {
    "► Mesoscale numerical investigation of dynamic spalling fracture in toughness concrete. International Journal of Mechanical Sciences. 2024;264:108826.": "https://www.doi.org/10.1016/j.ijmecsci.2023.108826",
}

   Publications3 = {
    "► The double-K fracture model: A state-of-the-art review. Engineering Fracture Mechanics. 2023;277:108988.": "https://www.doi.org/10.1016/j.engfracmech.2022.108988",
}

   Publications4 = {
    "► Experimental and numerical investigations on the stress waves propagation in strain-hardening fiber-reinforced cementitious composites: Stochastic analysis using polynomial chaos expansions. Journal of Building Engineering. 2023;74:106902.": "https://www.doi.org/10.1016/j.jobe.2023.106902",
}

   st.write('\n')
   st.subheader("Selected Publications")
   st.write("🌌", "***Concrete Constitutive Models***")
   for article, link in Publications1.items():
       st.write(f"[{article}]({link})")
   st.write("---")
   st.write("🌌", "***Dynamic Behaviour of Advanced Materials***")
   for article, link in Publications2.items():
       st.write(f"[{article}]({link})")
   st.write("---")
   st.write("🌌", "***Stress Wave Propagation***")
   for article, link in Publications4.items():
       st.write(f"[{article}]({link})")
   st.write("---")
   st.write("🌌", "***Concrete Fracture Mechanics***")
   for article, link in Publications3.items():
       st.write(f"[{article}]({link})")
   st.write("---")

with tab3:
# --- Complete List of Publications ---
   st.write('\n')
   st.subheader("Complete List of Publications")

# --- 2024
   st.write("🏗️", "**2024 | Zhejiang University | 浙江大学**")
   st.write(
    """
- 📑 [017] Wang Q, Li Q\*, **Yin X**, Xu S. Structural size effect in the mode I and mixed mode I/II fracture of strain-hardening cementitious composites (SHCC). *International Journal of Solids and Structures*. 2024;288:112628.                        
- 📑 [016] Li Q\*, Luo A, Hong C, Wang G, **Yin X**, Xu S. Fatigue behavior of short-headed studs embedded in Ultra-high Toughness Cementitious Composites (UHTCC). *Engineering Structures*. 2024;300:117194.                        
- 📑 [015] **Yin X**, Li Q\*, Wang Q, Chen B, Shu C, Xu S. Mesoscale numerical investigation of dynamic spalling fracture in toughness concrete. *International Journal of Mechanical Sciences*. 2024;264:108826.                        
"""
   )

# --- 2023
   st.write("✨", "**2023 | Zhejiang University | 浙江大学**")
   st.write(
    """
- 📑 [014] **Yin X**, Li Q\*, Wang Q, Chen B, Xu S. Experimental and numerical investigations on the stress waves propagation in strain-hardening fiber-reinforced cementitious composites: Stochastic analysis using polynomial chaos expansions. *Journal of Building Engineering*. 2023;74:106902.                        
- 📑 [013] Jiang X, Li Q\*, **Yin X**, Xu S. Investigation on triaxial compressive mechanical properties of ultra high toughness cementitious composites with high strain capacity. *Cement and Concrete Research*. 2023;170:107185.                        
- 📑 [012] Jiang X, Li Q\*, **Yin X**, Xu S. Effect of steel fiber and target thickness on the penetration resistance of UHPC under high velocity small projectile impact loading. *Cement and Concrete Composites*. 2023;140:105064.                        
- 📑 [011] Wang Q, Li Q\*, **Yin X**, Xu S, Xie H, Su Z. Fracture behavior and size effect of UHPFRC: Experimental and mesoscale numerical investigation. *Engineering Fracture Mechanics*. 2023;283:109197.                        
- 📑 [010] **Yin X**, Li Q\*, Chen B, Xu S. An improved calibration of Karagozian & Case concrete/cementitious model for strain-hardening fibre-reinforced cementitious composites under explosion and penetration loadings. *Cement and Concrete Composites*. 2023;137:104911.                        
- 📑 [009] **Yin X**, Li Q\*, Wang Q, Reinhardt H-W, Xu S. The double-K fracture model: A state-of-the-art review. *Engineering Fracture Mechanics*. 2023;277:108988.                        
- 📑 [008] **Yin X**, Li Q\*, Xu X, Chen B, Guo K, Xu S. Investigation of continuous surface cap model (CSCM) for numerical simulation of strain-hardening fibre-reinforced cementitious composites against low-velocity impacts. *Composite Structures*. 2023;304:116424.                        
"""
   )

# --- 2022
   st.write("✨", "**2022 | Zhejiang University | 浙江大学**")
   st.write(
    """
- 📑 [007] 李庆华, **银星**, 郭康安, 徐世烺\*. 超高韧性水泥基复合材料与活性粉末混凝土界面剪切强度试验研究. *工程力学*. 2022;39(08):232-244.                        
- 📑 [006] Li Q, **Yin X**, Huang B\*, Zhang Y, Xu S. Strengthening of the concrete face slabs of dams using sprayable strain-hardening fiber-reinforced cementitious composites. *Frontiers of Structural and Civil Engineering*. 2022;16(2):145-60.                        
- 📑 [005] Xu S, Chen B, Li Q*, Zhou F, **Yin X**, Jiang X, et al. Experimental and numerical investigations on ultra-high toughness cementitious composite slabs subjected to close-in blast loadings. *Cement and Concrete Composites*. 2022;126:104339.                        
- 📑 [004] Li Q, Chen B, Xu S*, Zhou F, **Yin X**, Jiang X, et al. Experiment and numerical investigations of ultra-high toughness cementitious composite slabs under contact explosions. *International Journal of Impact Engineering*. 2022;159:104033.                        
"""
   )

# --- 2021
   st.write("✨", "**2021 | Zhejiang University | 浙江大学**")
   st.write(
    """
- 📑 [003] Xu S, Guo K, Li Q\*, **Yin X**, Huang B. Shear fracture performance of the interface between ultra-high toughness cementitious composites and reactive powder concrete. *Composite Structures*. 2021;275:114403.                        
- 📑 [002] Li Q-H, **Yin X**, Huang B-T\*, Luo A-M, Lyu Y, Sun C-J, et al. Shear interfacial fracture of strain-hardening fiber-reinforced cementitious composites and concrete: A novel approach. *Engineering Fracture Mechanics*. 2021;253:107849.                        
- 📑 [001] Xu S\*, Zhou F, Li Q, Chen B, Jiang X, **Yin X**, et al. Comparative study on performance of UHTCC and RPC thick panels under hard projectile impact loading. *Cement and Concrete Composites*. 2021;122:104134.                        
"""
   )

with tab4:
# --- Academic Lineage ---
   lineage = Image.open(lineage)
   st.write('\n')
   st.subheader("Academic Lineage")
   st.image(lineage, channels="BGR")

with tab5:
# --- Codes ---
   st.write('\n')
   st.subheader("Calibration of KCC Model for ECC/SHCC")
   st.write(
    """
The ultra-high tensile capacity of strain-hardening fibre-reinforced cementitious composites makes them promising for impact dynamics applications, however, there is a lack of reference for taking the parameters of the constitutive model of materials in numerical simulations. In this study, the Karagozian & Case concrete/cementitious model parameters for strain-hardening fibre-reinforced cementitious composites were comprehensively and systematically calibrated. Multiaxial behaviour, crack-bridging constitutive relations, strain-rate effects, regularization of damage evolution parameters, and parameters scaling method for wide-range strength of materials were all considered and carefully discussed. The calibrated parameters were validated using low-velocity drop-weight impact tests, near-field explosion tests, and high-speed penetration tests. In this study, the traditional element erosion method and meshless/particle methods of Smoothed Particle Galerkin (SPG) method were used for failure analysis in penetration and explosion models. The results show that the calibrated parameters accurately predict the cratering and scabbing diameters and failure modes of explosion tests with the element erosion method. Furthermore, the residual velocity of the projectile and crack patterns of targets were also predicted with good precision with both element erosion and SPG methods. However, in the simulations of low-velocity impact tests, the predictions of maximum deflection were acceptable, and the errors in residual deflection were significant due to the inherent weakness of the material constitutive model.

Please Cite: **Yin et al. (2023)**
    """
    )
   st.caption('X. Yin, Q. Li, B. Chen, S. Xu, An improved calibration of Karagozian & Case concrete/cementitious model for strain-hardening fibre-reinforced cementitious composites under explosion and penetration loadings, Cem. Concr. Compos. 137 (2023) 104911.')

   st.text('''
*KEYWORD
*COMMENT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|      Karagozian & Case Concrete/Cementitious Model Parameters for UHTCC      |
|                        Only for Finite Element Method                        |
|                                  kg - m - s                                  |
|           Calibrated by YIN Xing - Zhejiang University (Dec, 2022)           |
|                         Contact: yinxing@zju.edu.cn                          |
| Reference                                                                    |
|    Yin X, Li Q, Chen B, Xu S. An improved calibration of Karagozian & Case   |
|        concrete/cementitious model for strain-hardening fibre-reinforced     |
|        cementitious composites under explosion and penetration loadings.     |
|        Cem Concr Compos 2023;137:104911.                                     |
|            doi: 10.1016/j.cemconcomp.2022.104911                             |
| Note: MAT ID is 72001, DIF ID is 72, EOS ID is 72                            |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
$--------------------------------Input Paramters--------------------------------
$ le      Element Size (m)
$ fc      Unconfined Uniaxial Compressive Strength (MPa)
$ ft      Unconfined Uniaxial Tensile Strength (Pa)
$ ro      Mass Density (kg/m^3)
$ pr      Poisson’s Ratio
$ omega   Associativity Parameter (ω), and ω = 1 and 0 represent the associated 
$         and non-associated flow rule. Do not change the calibrated value of
$         0.75 unless there are confinement.
$-------------------------------------------------------------------------------
*KEYWORD
*PARAMETER_EXPRESSION
$#    prmr                                                            expression
Rle       0.0025
Rfc       50.00
Rft       5.0e+6
Rro       2000.0
Rpr       0.255
Romega    0.75
$-------------------------------------------------------------------------------
$*                           Parameters Calculation                            *
$-------------------------------------------------------------------------------
Rb1       1.0
Rb2       2.68*log(&le*1000)-14.05
Rb3       0.05
RLW       0.8*&le
RSle      &le/0.01
$----------------------------------ETA-LAMBDA-----------------------------------
$----------------------------------LAMBDA (λ)-----------------------------------
Rlambda02 1.00E-04
Rlambda03 3.00E-04
Rlambda04 5.00E-04
Rlambda05 6.50E-04
Rref      &lambda05
Rlambda06 &lambda05+(7.00E-04-&lambda05)*&Sle
Rlambda07 &lambda05+(8.00E-04-&lambda05)*&Sle
Rlambda08 &lambda05+(1.00E-03-&lambda05)*&Sle
Rlambda09 &lambda05+(1.25E-03-&lambda05)*&Sle
Rlambda10 &lambda05+(1.75E-03-&lambda05)*&Sle
Rlambda11 &lambda05+(3.00E-03-&lambda05)*&Sle
$-----------------------------------LAMBDA->1-----------------------------------
Rl02      &lambda02/&ref
Rl03      &lambda03/&ref
Rl04      &lambda04/&ref
Rl05      &lambda05/&ref
Rl06      &lambda06/&ref
Rl07      &lambda07/&ref
Rl08      &lambda08/&ref
Rl09      &lambda09/&ref
Rl10      &lambda10/&ref
Rl11      &lambda11/&ref
$------------------------------------ETA (η)------------------------------------
Reta02    0.51
Reta03    0.88
Reta04    0.98
Reta05    1.00
Reta06    0.81
Reta07    0.55
Reta08    0.32
Reta09    0.22
Reta10    0.13
Reta11    0.06
$----------------------------Equation of State (EOS)----------------------------
RSs       (&fc/50.00)**0.638
Rc2       1.856895e+07*&Ss
Rc3       4.048031e+07*&Ss
Rc4       6.499132e+07*&Ss
Rc5       1.234835e+08*&Ss
Rc6       1.862465e+08*&Ss
Rc7       2.642361e+08*&Ss
Rc8       4.042460e+08*&Ss
Rc9       2.360113e+09*&Ss
Rc10      3.609804e+09*&Ss
Rk1       1.237930e+10*&Ss
Rk2       1.237930e+10*&Ss
Rk3       1.255261e+10*&Ss
Rk4       1.318395e+10*&Ss
Rk5       1.568457e+10*&Ss
Rk6       1.819757e+10*&Ss
Rk7       2.069819e+10*&Ss
Rk8       2.259222e+10*&Ss
Rk9       5.082940e+10*&Ss
Rk10      6.189650e+10*&Ss
$-------------------K&C strength surface parameters for UHTCC-------------------
Ra0m      0.50927*&fc*10**6
Ra1m      0.65165
Ra2m      0.08228/&fc/10**6
Ra0y      0.33365*&fc*10**6
Ra1y      1.17451
Ra2y      0.20506/&fc/10**6
Ra1r      0.60586
Ra2r      0.07977/&fc/10**6
*DEFINE_CURVE_TITLE
DIF_UHTCC
$#    lcid      sidr       sfa       sfo      offa      offo    dattyp     lcint
        72         0       1.0       1.0       0.0       0.0         0         0
$#                a1                  o1  
   -3.0000000000e+07            9.948667
            -3000000            9.841416
           -300000.0            9.522056
            -30000.0            8.657233
             -3000.0            6.812797
              -300.0            4.315611
              -100.0            3.276448
               -30.0            2.414954
               -10.0            1.879336
                -3.0            1.506715
                -1.0            1.301248
                -0.1             1.09859
               -0.01            1.031767
              -0.001            1.010184
   -9.9999997474e-05             1.00326
   -9.9999997474e-06            1.001043
                 0.0                 1.0
    9.9999997474e-06                 1.0
    9.9999997474e-05            1.000003
               0.001             1.00002
                0.01            1.000143
                 0.1            1.001015
                 1.0            1.007186
                 3.0            1.018205
                10.0             1.04992
                30.0            1.122447
               100.0            1.307575
               300.0             1.63294
              3000.0            2.533467
             30000.0            2.917814
            300000.0               2.988
             3000000            2.998301
    3.0000000000e+07             2.99976
*MAT_CONCRETE_DAMAGE_REL3_TITLE
KCC_UHTCC_FE
$#     mid        ro        pr  
     72001&ro       &pr       
$       ft        A0        A1        A2        B1     OMEGA       A1F
$#      ft        a0        a1        a2        b1     omega       a1f   
&ft       &a0m      &a1m      &a2m      &b1       &omega    &a1r      
$  sLambda      NOUT     EDROP     RSIZE       UCF    LCRate  LocWidth      NPTS
$# slambda      nout     edrop     rsize       ucf    lcrate  locwidth      npts
       0.0       2.0       1.0     39.371.45000E-4        72&lw             13.0
$ Lambda01  Lambda02  Lambda03  Lambda04  Lambda05  Lambda06  Lambda07  Lambda08
$# lambda1   lambda2   lambda3   lambda4   lambda5   lambda6   lambda7   lambda8
       0.0&lambda02 &lambda03 &lambda04 &lambda05 &lambda06 &lambda07 &lambda08 
$ Lambda09  Lambda10  Lambda11  Lambda12  Lambda13        B3       A0Y       A1Y
$#lambda09  lambda10  lambda11  lambda12  lambda13        b3       a0y       a1y
&lambda09 &lambda10 &lambda11       0.011.00000E10&b3       &a0y      &a1y      
$    Eta01     Eta02     Eta03     Eta04     Eta05     Eta06     Eta07     Eta08
$#    eta1      eta2      eta3      eta4      eta5      eta6      eta7      eta8
       0.0&eta02    &eta03    &eta04    &eta05    &eta06    &eta07    &eta08    
$    Eta09     Eta10     Eta11    Eta012     Eta13        B2       A2F       A2Y
$#   eta09     eta10     eta11     eta12     eta13        b2       a2f       a2y
&eta09    &eta10    &eta11           0.0       0.0&b2       &a2r      &a2y      
*EOS_TABULATED_COMPACTION
$    EOSID     Gamma        E0      Vol0
$#   eosid      gama        e0        vo       lcc       lct       lck      lcid
        72       0.0       0.0       1.0         0         0         0         0
$    VolStrain01     VolStrain02     VolStrain03     VolStrain04     VolStrain05
$#           ev1             ev2             ev3             ev4             ev5
             0.0         -0.0015         -0.0043         -0.0101         -0.0305
$    VolStrain06     VolStrain07     VolStrain08     VolStrain09     VolStrain10
$#           ev6             ev7             ev8             ev9            ev10
         -0.0513         -0.0726         -0.0943          -0.174          -0.208
$     Pressure01      Pressure02      Pressure03      Pressure04      Pressure05
$#            c1              c2              c3              c4              c5
             0.0&c2             &c3             &c4             &c5             
$     Pressure06      Pressure07      Pressure08      Pressure09      Pressure10
$#            c6              c7              c8              c9             c10
&c6             &c7             &c8             &c9             &c10            
$            Multipliers of Gamma*E
$#            t1              t2              t3              t4              t5
             0.0             0.0             0.0             0.0             0.0
$#            t6              t7              t8              t9             t10
             0.0             0.0             0.0             0.0             0.0
$     BulkUnld01      BulkUnld02      BulkUnld03      BulkUnld04      BulkUnld05
$#            k1              k2              k3              k4              k5
&k1             &k2             &k3             &k4             &k5             
$     BulkUnld06      BulkUnld07      BulkUnld08      BulkUnld09      BulkUnld10
$#            k6              k7              k8              k9             k10
&k6             &k7             &k8             &k9             &k10            
*END
''')
