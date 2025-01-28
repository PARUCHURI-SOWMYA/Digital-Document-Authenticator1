import streamlit as st
from PIL import Image
import os
import filetype

# App Title
st.title("Forensic Scanner Identification Tool")

# File Upload Section
uploaded_file = st.file_uploader("Upload a scanned document", type=["jpg", "jpeg", "png", "pdf"])

if uploaded_file is not None:
    file_details = {"filename": uploaded_file.name, "filetype": uploaded_file.type, "filesize": uploaded_file.size}
    st.write("File Details:", file_details)

    # Check file type
    kind = filetype.guess(uploaded_file)
    if kind:
        st.write(f"Detected file type: {kind.mime}")
    else:
        st.write("Unable to determine the file type.")

    # Display the image if it's a valid image file
    if uploaded_file.type in ["image/jpeg", "image/png"]:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Example metadata extraction
        metadata = image.info
        st.write("Image Metadata:")
        if metadata:
            for key, value in metadata.items():
                st.write(f"{key}: {value}")
        else:
            st.write("No metadata found.")

    # Additional functionality for PDFs
    elif uploaded_file.type == "application/pdf":
        with open(os.path.join("temp", uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.write("PDF file saved. Further processing can be implemented.")

# Footer
st.markdown("---")
st.write("Built with Streamlit for forensic scanner identification.")
