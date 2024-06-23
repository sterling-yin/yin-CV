from pathlib import Path

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV-YINXING.pdf"
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
Recipient of the National Postdoctoral Program for Innovative Talents (China)          
入选博士后创新人才支持计划（博新计划）
"""
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, 'rb') as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
st.title(NAME)
st.write(DESCRIPTION)
st.write("""> *Looking for a Visiting Scholar Position ...*""")
col3, col4, col5 = st.columns(3, gap="small")

with col3:
    st.download_button(
        label='📄 Download Resume',
        data=PDFbyte,
        file_name=resume_file.name,
        mime='application/octet-stream',
    )

with col4:
    st.write("""
    📧 yinxing@zju.edu.cn        
    """)

with col5:
    st.write("""
    💬 WeChat: Sterling_YIN
    """)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["🌟Introduction", "🎖️Featured Publications", "📑Publications List", "🏛️Academic Lineage", "🗄️Codes"])

with tab1:
# --- Biography ---
   st.write('\n')
   st.subheader("Biography")
   st.write("""  
<div style="text-align: justify">  
            
I was born in Baotou, Inner Mongolia, China. I received my BEng degree from the *Ocean University of China* in 2017. 
I pursued further study at the *Zhejiang University* under the supervision of academician Prof. Shilang Xu, and obtained my PhD degree in 2023.

My research focuses on ***Impact Dynamics***, and I have authored/co-authored 17 papers from SCI journals such as *Cem. Concr. Compos.*(4), 
*Cem. Concr. Res.*(1), *Compos. Struct.*(2), *Eng. Struct.*(1), *Int. J. Impact Eng.*(2), *Int. J. Mech. Sci.*(1), *Eng. Fract. Mech.*(3), 
*Int. J. Solids Struct.*(1), with two papers recognized as ESI Highly Cited Papers.

银星，1995年9月出生于内蒙古自治区包头市。长期专注于先进建筑结构与材料**冲击动力学**研究，在工程材料领域的*Cem. Concr. Compos.*(4)、*Cem. Concr. Res.*(1)，
结构工程领域的*Compos. Struct.*(2)、*Eng. Struct.*(1)，固体力学领域的*Int. J. Mech. Sci.*(1)、*Int. J. Solids Struct.*(1)，
冲击动力学领域的*Int. J. Impact Eng.*(2)，断裂力学领域的*Eng. Fract. Mech.*(3)等期刊发表高水平SCI论文17篇，其中2篇曾入选ESI高被引论文。    
</div>  
""", unsafe_allow_html=True)  


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
""") 

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
""") 

# --- Publication trend ---
   st.write('\n')
   st.subheader("Publication Trend")
   data = {
       'Year': [2021, 2022, 2023, 2024],
       'Publication': [3, 4, 7, 4]
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
    "► Near range explosion resistance of UHPFRC panels in wide scaled distances: Experimental study and stochastic numerical modelling. International Journal of Impact Engineering. 2024;192:105028": "https://www.doi.org/10.1016/j.ijimpeng.2024.105028",
}

   Publications4 = {
    "► Experimental and numerical investigations on the stress waves propagation in strain-hardening fiber-reinforced cementitious composites: Stochastic analysis using polynomial chaos expansions. Journal of Building Engineering. 2023;74:106902.": "https://www.doi.org/10.1016/j.jobe.2023.106902",
}

   Publications5 = {
    "► The double-K fracture model: A state-of-the-art review. Engineering Fracture Mechanics. 2023;277:108988.": "https://www.doi.org/10.1016/j.engfracmech.2022.108988",
}

   st.write('\n')
   st.subheader('🌌 Concrete Constitutive Models')
   for article, link in Publications1.items():
       st.write(f"[{article}]({link})")

   st.subheader('🌌 Dynamic Behaviour of Advanced Materials')
   for article, link in Publications2.items():
       st.write(f"[{article}]({link})")

   st.subheader('🌌 Dynamic Response of Engineering Structures')
   for article, link in Publications3.items():
       st.write(f"[{article}]({link})")

   st.subheader('🌌 Stress Wave Propagation')
   for article, link in Publications4.items():
       st.write(f"[{article}]({link})")

   st.subheader('🌌 Concrete Fracture Mechanics')
   for article, link in Publications5.items():
       st.write(f"[{article}]({link})")

with tab3:
# --- Complete List of Publications ---

# --- Work in Process 
   st.subheader('🏗️ Work in Process')
   st.write(
    """
- 📑 [020] Xu H, Li Q\*, Quan G, **Yin X**, Xu S. Dynamic splitting tensile properties of high-strength ultrahigh-toughness cementitious composites (HS-UHTCCs). Submitted to the *Construction and Building Materials*. (Under Review)                        
- 📑 [019] Wang Q, Li Q\*, **Yin X**, Xu S. Fracture and multiple-cracking modelling of strain-hardening cementitious composites. Submitted to the *International Journal of Mechanical Sciences*. (Under Review)                        
""") 

# --- 2024
   st.subheader('✨ 2024 | Zhejiang University')
   st.write(
    """
- 📑 [018] **Yin X**, Li Q\*, Wang Q, Chen B, Xu S. Near range explosion resistance of UHPFRC panels in wide scaled distances: Experimental study and stochastic numerical modelling. *International Journal of Impact Engineering*. 2024;192:105028.                               
- 📑 [017] Wang Q, Li Q\*, **Yin X**, Xu S. Structural size effect in the mode I and mixed mode I/II fracture of strain-hardening cementitious composites (SHCC). *International Journal of Solids and Structures*. 2024;288:112628.                        
- 📑 [016] Li Q\*, Luo A, Hong C, Wang G, **Yin X**, Xu S. Fatigue behavior of short-headed studs embedded in Ultra-high Toughness Cementitious Composites (UHTCC). *Engineering Structures*. 2024;300:117194.                        
- 📑 [015] **Yin X**, Li Q\*, Wang Q, Chen B, Shu C, Xu S. Mesoscale numerical investigation of dynamic spalling fracture in toughness concrete. *International Journal of Mechanical Sciences*. 2024;264:108826.                        
""") 

# --- 2023
   st.subheader('✨ 2023 | Zhejiang University')
   st.write(
    """
- 📑 [014] **Yin X**, Li Q\*, Wang Q, Chen B, Xu S. Experimental and numerical investigations on the stress waves propagation in strain-hardening fiber-reinforced cementitious composites: Stochastic analysis using polynomial chaos expansions. *Journal of Building Engineering*. 2023;74:106902.                        
- 📑 [013] Jiang X, Li Q\*, **Yin X**, Xu S. Investigation on triaxial compressive mechanical properties of ultra high toughness cementitious composites with high strain capacity. *Cement and Concrete Research*. 2023;170:107185.                        
- 📑 [012] Jiang X, Li Q\*, **Yin X**, Xu S. Effect of steel fiber and target thickness on the penetration resistance of UHPC under high velocity small projectile impact loading. *Cement and Concrete Composites*. 2023;140:105064.                        
- 📑 [011] Wang Q, Li Q\*, **Yin X**, Xu S, Xie H, Su Z. Fracture behavior and size effect of UHPFRC: Experimental and mesoscale numerical investigation. *Engineering Fracture Mechanics*. 2023;283:109197.                        
- 📑 [010] **Yin X**, Li Q\*, Chen B, Xu S. An improved calibration of Karagozian & Case concrete/cementitious model for strain-hardening fibre-reinforced cementitious composites under explosion and penetration loadings. *Cement and Concrete Composites*. 2023;137:104911.                        
- 📑 [009] **Yin X**, Li Q\*, Wang Q, Reinhardt H-W, Xu S. The double-K fracture model: A state-of-the-art review. *Engineering Fracture Mechanics*. 2023;277:108988.                        
- 📑 [008] **Yin X**, Li Q\*, Xu X, Chen B, Guo K, Xu S. Investigation of continuous surface cap model (CSCM) for numerical simulation of strain-hardening fibre-reinforced cementitious composites against low-velocity impacts. *Composite Structures*. 2023;304:116424.                        
""") 

# --- 2022
   st.subheader('✨ 2022 | Zhejiang University')
   st.write(
    """
- 📑 [007] 李庆华, **银星**, 郭康安, 徐世烺\*. 超高韧性水泥基复合材料与活性粉末混凝土界面剪切强度试验研究. *工程力学*. 2022;39(08):232-244.                        
- 📑 [006] Li Q, **Yin X**, Huang B\*, Zhang Y, Xu S. Strengthening of the concrete face slabs of dams using sprayable strain-hardening fiber-reinforced cementitious composites. *Frontiers of Structural and Civil Engineering*. 2022;16(2):145-60.                        
- 📑 [005] Xu S, Chen B, Li Q*, Zhou F, **Yin X**, Jiang X, et al. Experimental and numerical investigations on ultra-high toughness cementitious composite slabs subjected to close-in blast loadings. *Cement and Concrete Composites*. 2022;126:104339.                        
- 📑 [004] Li Q, Chen B, Xu S*, Zhou F, **Yin X**, Jiang X, et al. Experiment and numerical investigations of ultra-high toughness cementitious composite slabs under contact explosions. *International Journal of Impact Engineering*. 2022;159:104033.                        
""") 

# --- 2021
   st.subheader('✨ 2021 | Zhejiang University')
   st.write(
    """
- 📑 [003] Xu S, Guo K, Li Q\*, **Yin X**, Huang B. Shear fracture performance of the interface between ultra-high toughness cementitious composites and reactive powder concrete. *Composite Structures*. 2021;275:114403.                        
- 📑 [002] Li Q-H, **Yin X**, Huang B-T\*, Luo A-M, Lyu Y, Sun C-J, et al. Shear interfacial fracture of strain-hardening fiber-reinforced cementitious composites and concrete: A novel approach. *Engineering Fracture Mechanics*. 2021;253:107849.                        
- 📑 [001] Xu S\*, Zhou F, Li Q, Chen B, Jiang X, **Yin X**, et al. Comparative study on performance of UHTCC and RPC thick panels under hard projectile impact loading. *Cement and Concrete Composites*. 2021;122:104134.                        
""") 

with tab4:
# --- Academic Lineage ---
   lineage = Image.open(lineage)
   st.image(lineage, channels="BGR")

with tab5:
# --- Codes ---
   st.write('\n')
   st.subheader("KCC Model for ECC/SHCC (LS-DYNA)")
   st.caption('X. Yin, Q. Li, B. Chen, S. Xu, An improved calibration of Karagozian & Case concrete/cementitious model for strain-hardening fibre-reinforced cementitious composites under explosion and penetration loadings, Cem. Concr. Compos. 137 (2023) 104911.')
   kc_file = current_dir / "assets" / "KC.k"
   with open(kc_file, "rb") as file:
        file_content = file.read()
   st.download_button(
        label="📄 Download MAT_072R3 KCC Material Card for ECC/SHCC",
        data=file_content,
        file_name="KC.k",
        mime='application/octet-stream',
   )
   st.write('\n')

   st.subheader("Strength Surface of KCC Model (MATLAB)")
   st.caption('X. Yin, Q. Li, B. Chen, S. Xu, An improved calibration of Karagozian & Case concrete/cementitious model for strain-hardening fibre-reinforced cementitious composites under explosion and penetration loadings, Cem. Concr. Compos. 137 (2023) 104911.')
   kc_strength_surface_file = current_dir / "assets" / "KCC_Strength_Surface.m"
   with open(kc_strength_surface_file, "rb") as file:
        file_content = file.read()
   st.download_button(
        label="📄 Download Strength Surface of KCC Model",
        data=file_content,
        file_name="KCC_Strength_Surface.m",
        mime='application/octet-stream',
   )
   st.write('\n')

   st.subheader("RHT Model for UHPFRC/UHPC/RPC (LS-DYNA)")
   st.caption('X. Yin, Q. Li, Q. Wang, B. Chen, S. Xu, Near range explosion resistance of UHPFRC panels in wide scaled distances : Experimental study and stochastic numerical modelling, Int. J. Impact Eng. 192 (2024) 105028.')
   rht_file = current_dir / "assets" / "RHT.k"
   with open(rht_file, "rb") as file:
        file_content = file.read()
   st.download_button(
        label="📄 Download MAT_272 RHT Material Card for UHPFRC/UHPC/RPC",
        data=file_content,
        file_name="RHT.k",
        mime='application/octet-stream',
   )
