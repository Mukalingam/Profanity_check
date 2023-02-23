import streamlit as st


st.set_page_config(
    page_title="Profanity Check",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded",
)

import base64

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("cover.jpg")
img1 = get_img_as_base64("menu.jpg")
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/jpg;base64,{img}");
background-size: 170%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img1}");
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
# hide_st_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             header {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_st_style, unsafe_allow_html=True)
st.title('Profanity check Application for Images and Text Data')

st.markdown('''
This is an amazing AI based Application to check the Profanity Score of the Text, Image and other data types
''')
st.markdown("<p style='text-align: left; color: rgb(249 243 243);'>In today’s digital age, it’s becoming increasingly difficult to monitor and moderate content on the internet. Social media platforms, messaging apps, and forums are rife with hate speech, profanity, and other offensive material that can be harmful to users. Fortunately, advances in artificial intelligence (AI) have made it possible to develop tools that can automatically detect and flag inappropriate content, making it easier for moderators to take action.</p>", unsafe_allow_html=True)

st.markdown("<p style='text-align: left; color: rgb(249 243 243);'>The accuracy of the Profanity Check application has been thoroughly tested. The model was evaluated using different metrics, and its performance was compared to other similar tools that are currently available. The application’s accuracy on real-time data is around 92–96%, which is a significant improvement over other similar tools.</p>", unsafe_allow_html=True)

st.image("sample.jpg",use_column_width=True)

if st.button("Read my post on Medium"):
    st.markdown(f"[Click here](https://medium.com/@utlamuka/say-goodbye-to-offensive-content-a-closer-look-at-profanity-checks-ai-based-text-and-image-411015a6cf51/) to read my latest post!")
