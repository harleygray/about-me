import streamlit as st
import base64
from constant import *

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")


# -----------------  loading assets  ----------------- #
with open("images/selfie.png", "rb") as image_file:
    image_data = base64.b64encode(image_file.read()).decode()
photo_html = f'<a href="https://www.linkedin.com/in/harleygray1996/"><img src="data:image/png;base64,{image_data}" width="250" alt="Profile" title="Profile"></a>'
st.sidebar.markdown(photo_html, unsafe_allow_html=True)

st.title("📝 Resume")

st.write("[Click here if it's blocked by your browser](https://drive.google.com/file/d/1yztCc5SYT4cZu02kO9WcWg8Kp9O06U0y/view?usp=sharing)")

with open("images/resume.pdf","rb") as f:
      base64_pdf = base64.b64encode(f.read()).decode('utf-8')
      pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1000mm" height="1000mm" type="application/pdf"></iframe>'
      st.markdown(pdf_display, unsafe_allow_html=True)
  
