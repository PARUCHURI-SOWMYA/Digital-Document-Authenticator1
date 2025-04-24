import streamlit as st
from PIL import Image, ImageOps, ImageFilter

# App Title
st.title("Digital Document Authentication and Verification Tool")

# File Upload Section
st.subheader("Upload Original Image")
original_image = st.file_uploader("Upload the original image to process", type=["jpg", "jpeg", "png"])

if original_image is not None:
    st.markdown("### Original Image")

    # Open and convert the image to RGB for consistency
    image = Image.open(original_image).convert("RGB")
    
    # Display original image
    st.image(image, caption="Original Image", use_container_width=True)

    # Show image details
    image_info = {
        "Image Type": original_image.type,
        "Image Format": image.format,
        "Image Size (bytes)": len(original_image.getvalue()),
        "Image Dimensions": f"{image.width} x {image.height}",
        "Image Mode": image.mode,
    }

    st.markdown("### Uploaded Image Details")
    for key, value in image_info.items():
        st.write(f"**{key}**: {value}")

    # Image transformation selection
    st.markdown("### Select Authentication Transformation")
    transformation = st.selectbox(
        "Choose a transformation:",
        ["Grayscale", "Edge Detection", "Invert Colors"]
    )

    # Apply transformation
    if transformation == "Grayscale":
        processed_image = ImageOps.grayscale(image)
        file_name = "grayscale_output.png"
    elif transformation == "Edge Detection":
        processed_image = image.filter(ImageFilter.FIND_EDGES)
        file_name = "edge_output.png"
    elif transformation == "Invert Colors":
        processed_image = ImageOps.invert(ImageOps.grayscale(image))
        file_name = "invert_output.png"

    # Show processed image
    st.markdown("### Authentication Image Output")
    st.image(processed_image, caption=f"{transformation} Image", use_container_width=True)

    # Save and download
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
