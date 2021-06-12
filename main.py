import cv2
import numpy as np
from PIL import Image
import streamlit as st

st.title("Image to Pencil Sketch App :camera:")
uploaded_file = st.file_uploader("Choose an image for conversion")
if uploaded_file is not None :
    img = Image.open(uploaded_file)
    #image = np.array(img)
    #input = cv2.imwrite('input.jpg',image)
    img.save('input.jpg')
    st.image(img,caption="Uploaded Image",use_column_width=None)

if st.button("Sketch Image"):
    img1 = cv2.imread('input.jpg')  # reading the image file

    gray_image = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)  # converting the image to gray scale

    inverted_gray_image = 255 - gray_image  # converting the gray scale to inverted gray scale/negative value of gray scale

    blurred_img = cv2.GaussianBlur(inverted_gray_image,(21,21),0)  # Converting the inverted gray scale to blurred image

    inverted_blurred_img = 255 - blurred_img  # converting the blurred image to its inverted image

    pencil_sketch = cv2.divide(gray_image,inverted_blurred_img,scale=256.0)  # Dividing the gray scale by the inverted blurred image to create the pencil sketch

    output = Image.open(pencil_sketch)

    st.image(output,"Sketch Image",use_column_width=None)




