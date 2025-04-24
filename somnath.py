import streamlit as st
from PIL import Image, ImageOps, ImageFilter

# App Title
st.title("Digital Document Authentication and Verification Tool")

# File Upload Section
st.subheader("Upload Original Image")
original_image = st.file_uploader("Upload the original image to process", type=["jpg", "jpeg", "png"])

# Display and Process the Uploaded Image
if original_image is not None:
    st.write("### Original Image")

    # Open the uploaded image
    image = Image.open(original_image).convert("RGB")  # Ensure RGB format
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

    # Processed Images
    st.write("### Authentication Image Outputs")

    grayscale_img = ImageOps.grayscale(image)
    edge_img = image.filter(ImageFilter.FIND_EDGES)
    inverted_img = ImageOps.invert(grayscale_img)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(grayscale_img, caption="Grayscale", use_container_width=True)
    with col2:
        st.image(edge_img, caption="Edge Detection", use_container_width=True)
    with col3:
        st.image(inverted_img, caption="Inverted Colors", use_container_width=True)

    # Download Buttons
    st.write("### Download Processed Images")

    grayscale_img.save("grayscale_output.png")
    edge_img.save("edge_output.png")
    inverted_img.save("invert_output.png")

    col1, col2, col3 = st.columns(3)
    with col1:
        with open("grayscale_output.png", "rb") as f:
            st.download_button("Download Grayscale", f, "grayscale_output.png", "image/png")
    with col2:
        with open("edge_output.png", "rb") as f:
            st.download_button("Download Edge Detection", f, "edge_output.png", "image/png")
    with col3:
        with open("invert_output.png", "rb") as f:
            st.download_button("Download Inverted Colors", f, "invert_output.png", "image/png")

else:
    st.warning("Please upload an original image to process.")

# Footer
st.markdown("---")
st.write("Built with Streamlit for digital document authentication.")
