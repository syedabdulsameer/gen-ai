import streamlit as st
from PIL import Image
from caption_generator import generate_caption
from caption_enhancer import enhance_caption

st.set_page_config(page_title="Image Caption Generator", layout="centered")
st.title("🖼️ AI Image-to-Caption Generator")
st.write("Upload an image to generate a descriptive caption using AI.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Generate Caption"):
        with st.spinner("Generating caption..."):
            caption = generate_caption(image)
            enhanced_caption = enhance_caption(caption)
            st.success("Generated Caption:")
            st.markdown(f"**{enhanced_caption}**")