import streamlit as st
from PIL import Image, ImageOps, ImageFilter
import os

# App Title
st.title("Digital Document Authentication and Verification Tool")

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

    # Document Authentication Processing Options
    st.write("### Authentication Image Processing Options")
    process_type = st.selectbox("Select the type of document authentication transformation:", 
                                ["Grayscale", "Edge Detection", "Invert Colors"])

    # Process the image based on the selected option
    if process_type == "Grayscale":
        auth_image = ImageOps.grayscale(image)
    elif process_type == "Edge Detection":
        auth_image = image.filter(ImageFilter.FIND_EDGES)
    elif process_type == "Invert Colors":
        auth_image = ImageOps.invert(ImageOps.grayscale(image))

    # Display the authenticated image
    st.write("### Authentication Image Output")
    st.image(auth_image, caption="Authenticated Output Image", use_column_width=True)

    # Display authenticated image details
    auth_image_info = {
        "Image Dimensions (width x height)": f"{auth_image.width} x {auth_image.height}",
        "Image Mode": auth_image.mode,
    }
    
    st.write("### Authentication Image Details")
    for key, value in auth_image_info.items():
        st.write(f"{key}: {value}")

    # Option to Download the Processed Image
    st.write("### Download Authentication Image")
    auth_image.save("auth_output.png")  # Save locally for download
    with open("auth_output.png", "rb") as file:
        btn = st.download_button(
            label="Download Authentication Image",
            data=file,
            file_name="auth_output.png",
            mime="image/png",
        )
else:
    st.warning("Please upload an original image to process.")

# Footer
st.markdown("---")
st.write("Built with Streamlit for digital document authentication.")
