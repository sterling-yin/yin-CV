from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Xing YIN, Ph.D."
PAGE_ICON = ":star:"
NAME = "Xing YIN (银星)"
DESCRIPTION = """
Doctor of Philosophy   
Postdoctoral Fellow at ***Zhejiang University***
"""
EMAIL = "yinxing@zju.edu.cn"
SOCIAL_MEDIA = {
    "ZJU Homepage": "https://person.zju.edu.cn/yinxing",
    "ResearchGate": "https://www.researchgate.net/profile/Xing-Yin-yinxing",
    "GitHub": "https://sterling-yin.github.io/",
    "ORCID": "https://orcid.org/0000-0001-9547-2681",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📃 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📧", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- Biography ---
st.write('\n')
st.subheader("Biography")
st.write("""
Dr. Yin was born in Baotou, Inner Mongolia, China. He received his BEng degree from the Ocean University of China in 2017. He pursued further study at the Zhejiang University under the supervision of academician Prof. Shilang Xu, and obtained his PhD degree in 2023.

His research focuses on ***Impact Dynamics***, and has authored/co-authored 16 papers from SCI journals such as *CCC*, *CCR*, *CS*, *ES*, *IJIE*, *IJMS*, *IJSS*, *EFM*, with two papers recognized as **ESI Highly Cited Papers**.
         """)

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Research Interests")
st.write(
    """
- 📌 Dynamic mechanics behaviours of engineering materials [e.g., dynamic compression, dynamic fracture, and spallation, etc.]
- 📌 Dynamic response of engineering structures [e.g., low-velocity impact, explosion, and penetration, etc.]
- 📌 Constitutive models of cementitious materials [e.g., KCC, CSC, and RHT, etc.]
- 📌 Advanced numerical approach [e.g., meshfree/particle method]
"""
)

# --- Education & Work ---
st.write('\n')
st.subheader("Education & Work")
st.write(
    """
    - ⭐ Postdoctoral Fellow, 2023.10-, College of Civil Engineering and Architecture, ***Zhejiang University*** (Supervisor: Prof. Qinghua Li)
    - ⭐ Ph.D, 2017.9-2023.9, Structural Engineering, ***Zhejiang University***, Hangzhou, China (Supervisor: **Academician Prof. Shilang Xu**) 
    - ⭐ BEng, 2013.8-2017.6, Civil Engineering, ***Ocean University of China***, Qingdao, China
"""
)

Publications1 = {
    "► Yin X, Li Q*, Chen B, Xu S. An improved calibration of Karagozian & Case concrete/cementitious model for strain-hardening fibre-reinforced cementitious composites under explosion and penetration loadings. Cement and Concrete Composites. 2023;137:104911.": "https://www.doi.org/10.1016/j.cemconcomp.2022.104911",
    "► Yin X, Li Q*, Xu X, Chen B, Guo K, Xu S. Investigation of continuous surface cap model (CSCM) for numerical simulation of strain-hardening fibre-reinforced cementitious composites against low-velocity impacts. Composite Structures. 2023;304:116424.": "https://www.doi.org/10.1016/j.compstruct.2022.116424",
}

Publications2 = {
    "► Yin X, Li Q*, Wang Q, Chen B, Shu C, Xu S. Mesoscale numerical investigation of dynamic spalling fracture in toughness concrete. International Journal of Mechanical Sciences. 2024;264:108826.": "https://www.doi.org/10.1016/j.ijmecsci.2023.108826",
    "► Yin X, Li Q*, Wang Q, Chen B, Xu S. Experimental and numerical investigations on the stress waves propagation in strain-hardening fiber-reinforced cementitious composites: Stochastic analysis using polynomial chaos expansions. Journal of Building Engineering. 2023;74:106902.": "https://www.doi.org/10.1016/j.jobe.2023.106902",
}

Publications3 = {
    "► Yin X, Li Q*, Wang Q, Reinhardt H-W, Xu S. The double-K fracture model: A state-of-the-art review. Engineering Fracture Mechanics. 2023;277:108988.": "https://www.doi.org/10.1016/j.engfracmech.2022.108988",
}

# --- Selected Publications ---
st.write('\n')
st.subheader("Selected Publications")
st.write("🌌", "***Concrete Constitutive Models***")
for article, link in Publications1.items():
    st.write(f"[{article}]({link})")
st.write("🌌", "***Dynamic Behaviour of Advanced Materials***")
for article, link in Publications2.items():
    st.write(f"[{article}]({link})")
st.write("🌌", "***Concrete Fracture Mechanics***")
for article, link in Publications3.items():
    st.write(f"[{article}]({link})")