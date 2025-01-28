import streamlit as st
from PIL import Image
import os

st.title("Forensic Scanner Identification Tool")

uploaded_file = st.file_uploader("Upload a scanned document", type=["jpg", "jpeg", "png", "pdf"])

if uploaded_file is not None:
    file_details = {"filename": uploaded_file.name, "filetype": uploaded_file.type, "filesize": uploaded_file.size}
    st.write("File Details:", file_details)

    if uploaded_file.type in ["image/jpeg", "image/png"]:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        metadata = image.info
        st.write("Image Metadata:")
        if metadata:
            for key, value in metadata.items():
                st.write(f"{key}: {value}")
        else:
            st.write("No metadata found.")
    elif uploaded_file.type == "application/pdf":
        with open(os.path.join("temp", uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.write("PDF file saved. Further processing can be implemented.")

st.markdown("---")
st.write("Built with Streamlit for forensic scanner identification.")
