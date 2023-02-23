import tensorflow as tf
from tensorflow.keras.models import Model, load_model
import numpy as np
from PIL import Image, ImageOps
import streamlit as st

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


@st.cache(allow_output_mutation=True)
def load():
  model=load_model('pages/profanity_image_classification.h5')
  return model
with st.spinner('Model is being loaded..'):
  model=load()

st.write("""
                 # Profanity Check on the Images
         """
         )

file = st.file_uploader("Upload the image to be classified \U0001F447", type=["jpg", "png","jpeg"])


st.set_option('deprecation.showfileUploaderEncoding', False)
def upload_predict(upload_image, model):
    
        size = (180,180)  
        img_height = 180
        img_width = 180  
        image = ImageOps.fit(upload_image, size, Image.ANTIALIAS)
        img_array = tf.keras.utils.img_to_array(image)
        img_array = tf.expand_dims(img_array, 0)
        predictions = model.predict(img_array)
        maping = {0 : "Accident", 1 : "Adult", 2 : "Drawings", 3 : "Hentai", 4 : "Neutral", 5 : "Nudity"}
        new_ans = np.argmax(predictions[0])
        score = tf.nn.softmax(predictions[0])
        confidence = 100 * np.max(score)
        confidence = int(confidence)
        pred_class = maping[new_ans]
        
        return pred_class,confidence
if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    #st.image(image, use_column_width=True)
    predictions = upload_predict(image, model)
    image_class = predictions[0]
    score=predictions[1]
    st.write("The image is classified as",image_class)
    st.write("The similarity score is approximately",score)
    print("The image is classified as ",image_class, "with a similarity score of",score)
