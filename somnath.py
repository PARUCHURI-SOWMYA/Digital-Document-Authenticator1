import streamlit as st
from PIL import Image, ImageOps, ImageFilter
import os

# App Title
st.title("Forensic Scanner Identification Tool")

# File Upload Section
st.subheader("Upload Original Image")
original_image = st.file_uploader("Upload the original image to process", type=["jpg", "jpeg", "png"])

# Display and Process the Uploaded Image
if original_image is not None:
    st.write("### Original Image")
    
    # Open the uploaded image
    image = Image.open(original_image)
    st.image(image, caption="Original Image", use_column_width=True)

    # Display image details
    image_info = {
        "Image Type": original_image.type,
        "Image Format": image.format,
        "Image Size (in bytes)": len(original_image.getvalue()),
        "Image Dimensions (width x height)": f"{image.width} x {image.height}",
        "Image Mode": image.mode,
    }

    st.write("### Uploaded Image Details")
    for key, value in image_info.items():
        st.write(f"{key}: {value}")

    # Forensic Processing Options
    st.write("### Forensic Image Processing Options")
    process_type = st.selectbox("Select the type of forensic transformation:", 
                                ["Grayscale", "Edge Detection", "Invert Colors"])

    # Process the image based on the selected option
    if process_type == "Grayscale":
        forensic_image = ImageOps.grayscale(image)
    elif process_type == "Edge Detection":
        forensic_image = image.filter(ImageFilter.FIND_EDGES)
    elif process_type == "Invert Colors":
        forensic_image = ImageOps.invert(ImageOps.grayscale(image))

    # Display the forensic image
    st.write("### Forensic Image Output")
    st.image(forensic_image, caption="Forensic Output Image", use_column_width=True)

    # Display forensic image details
    forensic_image_info = {
        "Image Dimensions (width x height)": f"{forensic_image.width} x {forensic_image.height}",
        "Image Mode": forensic_image.mode,
    }
    
    st.write("### Forensic Image Details")
    for key, value in forensic_image_info.items():
        st.write(f"{key}: {value}")

    # Option to Download the Processed Image
    st.write("### Download Forensic Image")
    forensic_image.save("forensic_output.png")  # Save locally for download
    with open("forensic_output.png", "rb") as file:
        btn = st.download_button(
            label="Download Forensic Image",
            data=file,
            file_name="forensic_output.png",
            mime="image/png",
        )
else:
    st.warning("Please upload an original image to process.")

# Footer
st.markdown("---")
st.write("Built with Streamlit for forensic scanner identification.") 
