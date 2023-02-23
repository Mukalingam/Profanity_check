import spacy
from profanity_filter import ProfanityFilter
import streamlit as st
import spacy.cli 
spacy.cli.download("en_core_web_md")
import subprocess
subprocess.run(f"python -m spacy download en")


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
background-size: 100%;
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

st.write("""
                # Profanity Check on the Text
        """
        )
text_message = st.text_area("Please enter the text data below...","")
st.markdown(f"Your given input is : {text_message}")
#st.markdown("How does the mdeol Work? 🧐")
#st.image("https://storage.googleapis.com/micada-dev-public/text_module.gif",width=800)



if st.button("Get Results"):
    nlp = spacy.load('en_core_web_md')
    profanity_filter = ProfanityFilter(nlps={'en': nlp})
    nlp.add_pipe(profanity_filter.spacy_component, last=True)
    res = len(text_message.split())
    doc = nlp(text_message)
    count_of_profanity_words = 0
    profanity_percent = 0
    if res<= 1000:
        for token in doc:
            value =  token._.is_profane
            word = token._.original_profane_word
            if value == True:
                count_of_profanity_words += 1
            profanity_percent = ((count_of_profanity_words/res)*100)
            profanity_percent = int(profanity_percent)
        if profanity_percent == 0:
            st.write("There is no profanity content in the given text.") 
        elif profanity_percent in range(1,40):
            st.write("We say that the above given content have the profanity with an accuracy of 70%")
        elif profanity_percent in range(40,70):
            st.write("We say that the above given content have the profanity with an accuracy of 80%") 
        elif profanity_percent in range(70,90):
            st.write("We say that the above given content have the profanity with an accuracy of 90%") 
        elif profanity_percent in range(90,100):
            st.write("We say that the above given content have the profanity with an accuracy of 100%")
        else:
            st.write("Please enter the text input correctly")                                
    else:
        st.write("You have reached the maximum limit of the words for texting the application")

