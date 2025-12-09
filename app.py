import streamlit as st
import cv2
import numpy as np
import tempfile

st.set_page_config(page_title="Lane Detection", layout="wide")

st.title("🚗 Lane Detection using LaneNet")
st.markdown("Upload a road image and the model will detect lanes.")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Save uploaded image
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(uploaded_file.read())

    # Read image with OpenCV
    image = cv2.imread(temp_file.name)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    st.subheader("✅ Original Image")
    st.image(image_rgb, use_container_width=True)

    # ----------------------------
    # ✅ FAKE LANE DETECTION TEST
    # ----------------------------
    output = image_rgb.copy()
    h, w, _ = output.shape

    # Draw two green "lane" lines
    cv2.line(output, (w // 2 - 120, h), (w // 2 - 50, h // 2), (0, 255, 0), 6)
    cv2.line(output, (w // 2 + 120, h), (w // 2 + 50, h // 2), (0, 255, 0), 6)

    st.subheader("✅ Lane Detection Output (System Test)")
    st.image(output, use_container_width=True)
