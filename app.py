import rembg
import numpy as np
import streamlit as st
from PIL import Image
import requests

st.set_page_config(
    page_title="Remove Background from Images",
    page_icon="icon.jpeg",
    menu_items={
        "About":"Instantly remove backgrounds from any image with Clear BG. Upload your photos, remove the unwanted backdrop, and download the result in seconds."
    }
)

st.write("<h2 style='color:#F7C23C;'>Instantly Remove Image Backgrounds.</h2>",unsafe_allow_html=True)

opt=st.radio("Choose Upload Option",["Upload Image", "Via URL"])

if opt=="Upload Image":
    file=st.file_uploader("Upload Image",type=["jpg","png"])
else:
    url=st.text_input("Enter URL",placeholder="Image URL")

btn=st.button("Remove")
if btn:
    try:
        if opt=="Via URL" and len(opt)>=5:
            with open("upload.jpg","wb") as img:
                img.write(requests.get(url).content)
                input_image = Image.open("upload.jpg")
        else:
            input_image = Image.open(file)

        input_array = np.array(input_image)
        output_array = rembg.remove(input_array)
        output_image = Image.fromarray(output_array)
        output_image = output_image.convert("RGB")
        output_image.save('remove.png')
        st.image("remove.png")
        with open("remove.png","rb") as img:
            st.download_button("Download",img,"remove.png")
    except:
        st.error("Something Went Wrong!")