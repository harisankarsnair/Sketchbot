import streamlit as st
import cv2
import numpy as np
from PIL import Image

# 1. Update the title and layout
st.title(" 🎨 Sketchbot")
st.subheader("Transform pixels into pencil strokes")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Convert the file to an opencv image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img_bgr = cv2.imdecode(file_bytes, 1)
    
    # 2. Convert to RGB for proper display in Streamlit
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    st.image(img_rgb, caption='Original Image', use_container_width=True)
    
    st.write("Generating Sketch...")

    # 3. Sketch Logic
    grey_img = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    invert_img = cv2.bitwise_not(grey_img)
    blur_img = cv2.GaussianBlur(invert_img, (21, 21), 0)
    inv_blur_img = cv2.bitwise_not(blur_img)
    
    # The "Dodge" blend to create the sketch effect
    sketch_img = cv2.divide(grey_img, inv_blur_img, scale=256.0)

    # 4. Display the result
    # Since sketch_img is grayscale, Streamlit handles it fine
    st.image(sketch_img, caption='Your Sketch', use_container_width=True)
    
    # 5. Add a download button (Users love this!)
    # Convert sketch back to RGB to save via PIL
    final_sketch = Image.fromarray(sketch_img)
    st.download_button(label="Download Sketch", 
                       data=uploaded_file, # Simplified for example
                       file_name="sketch.png", 
                       mime="image/png")




