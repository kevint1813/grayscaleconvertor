import streamlit as st
from PIL import Image


st.title("Capture image and get Grayscale version!")
st.subheader("webapp designed by Kevin T.")
# getting it under an expander.

with st.expander("Open Camera"):
    # creating the image
    x = st.camera_input("Camera")

if x:

    # creating pillow image
    pillow = Image.open(x)

    # making it bw
    bw = pillow.convert("L")

    # displaying in webapp
    st.write("**Success!!** your GrayScale image is below!")
    st.image(bw)
    st.write("thankyou for using my web app. cheers!")
