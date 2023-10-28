import streamlit as st
import requests
from streamlit_lottie import st_lottie
from constant import *
from PIL import Image
import base64

st.set_page_config(page_icon='📡', page_title="harley", layout="centered")

name = info["Name"]

with st.sidebar:
    # -----------------  loading assets  ----------------- #
    with open("images/selfie.png", "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode()
    photo_html = f'<a href="https://www.linkedin.com/in/harleygray1996/"><img src="data:image/png;base64,{image_data}" width="250" alt="Profile" title="Profile"></a>'
    st.markdown(photo_html, unsafe_allow_html=True)

    # -----------------  contact  ----------------- #

    st.subheader("📨 Contact Me")
    contact_form = f"""
    <form action="https://formsubmit.co/{info["Email"]}" method="POST">
        <input type="hidden" name="_captcha value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")

# loading assets
lottie_gif = load_lottieurl("https://lottie.host/83434b7f-4428-4c3f-afe5-bfe1b37da0ec/LY4U6nsXkz.json")
python_lottie = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_2znxgjyt.json")
my_sql_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_w11f2rwn.json")
github_lottie = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_6HFXXE.json")
r_lottie = load_lottieurl("https://lottie.host/1d9e2f27-b7b8-4dba-aeba-e8b877d95a3a/mAnI1uaj7P.json")

# ----------------- info ----------------- #
def gradient(color1, color2, color3, content1, content2):
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
                f'<span style="color:{color3};">{content1}</span><br>'
                f'<span style="color:white;font-size:17px;">{content2}</span></h1>', 
                unsafe_allow_html=True)

with st.container():
    col1,col2 = st.columns([8,3])

full_name = info['Full_Name']
with col1:
    gradient('#FFD4DD','#000395','e0fbfc',f"{full_name}📡", info["Intro"])
    st.write("")
    st.write(info['About'])
    
with col2:
    st_lottie(lottie_gif, height=0, key="data")
        

# ----------------- skillset ----------------- #
with st.container():
    st.subheader('⚒️ Skills')
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        st_lottie(python_lottie, height=70,width=70, key="python", speed=2.5)
    with col2:
        st_lottie(github_lottie,height=50,width=50, key="github", speed=2.5)
    with col3:
        st_lottie(my_sql_lottie,height=80,width=80, key="mysql", speed=2.5)
    with col4:
        st_lottie(r_lottie, height=80,width=80, key="r", speed=2.5)
    
# ----------------- portfolio ----------------- #
with st.container():
    st.subheader("🪟 window into parliament 🪟")
    st.write("a live dashboard showing how each member of parliament voted in user-selected divisions.")
    st.markdown("""
    - parliamentary voting data retrieved using API requests
    - GitHub actions to auto-update member and division information daily
    - [Plotly](https://plotly.com/python/) for visualising data
    - data transformation and wrangling
    """)
    divisions = """
    <iframe
        src="https://your-library.streamlit.app/?embed=true"
        height="750"
        style="width:100%;border:none;"
    </iframe>
    """
    st.markdown(divisions, unsafe_allow_html=True)



