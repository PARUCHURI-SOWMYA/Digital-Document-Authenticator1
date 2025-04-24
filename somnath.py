import streamlit as st
from PIL import Image, ImageOps, ImageFilter
import warnings

# Suppress deprecation warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# App Title
st.title("Digital Document Authentication and Verification Tool")

# File Upload Section
st.subheader("Upload Original Image")
original_image = st.file_uploader("Upload the original image to process", type=["jpg", "jpeg", "png"])

if original_image is not None:
    st.write("### Original Image")

    # Open and convert the image to RGB for consistency
    image = Image.open(original_image).convert("RGB")
    st.image(image, caption="Original Image", use_container_width=True)

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

    # Select the type of transformation to apply
    st.write("### Select Authentication Transformation")
    transformation = st.selectbox("Choose a transformation:", 
                                  ["Grayscale", "Edge Detection", "Invert Colors"])

    # Process the image based on selection
    if transformation == "Grayscale":
        processed_image = ImageOps.grayscale(image)
        file_name = "grayscale_output.png"
    elif transformation == "Edge Detection":
        processed_image = image.filter(ImageFilter.FIND_EDGES)
        file_name = "edge_output.png"
    elif transformation == "Invert Colors":
        processed_image = ImageOps.invert(ImageOps.grayscale(image))
        file_name = "invert_output.png"

    # Display the processed image
    st.write("### Authentication Image Output")
    st.image(processed_image, caption=f"{transformation} Image", use_container_width=True)

    # Save and provide download button
    processed_image.save(file_name)
    with open(file_name, "rb") as f:
        st.download_button(
            label=f"Download {transformation} Image",
            data=f,
            file_name=file_name,
            mime="image/png"
        )

else:
    st.warning("Please upload an original image to process.")

# Footer
st.markdown("---")
st.write("Built with Streamlit for digital document authentication.")
