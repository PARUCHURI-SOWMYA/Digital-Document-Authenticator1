import streamlit as st
from PIL import Image

# Try to import matplotlib, handle errors if not available
try:
    import matplotlib.pyplot as plt
    matplotlib_available = True
except ImportError:
    matplotlib_available = False
    st.error("Matplotlib is not installed. Please install it using 'pip install matplotlib' to view the graphs.")

# App Title
st.title("Forensic Scanner Identification Tool")

# File Upload Section
st.subheader("Upload Images")
uploaded_image = st.file_uploader("Upload the image to be analyzed", type=["jpg", "jpeg", "png"])
forensic_image = st.file_uploader("Upload the forensic reference image", type=["jpg", "jpeg", "png"])

# Display Uploaded Images
if uploaded_image is not None and forensic_image is not None:
    st.write("### Uploaded Images")

    # Open the images
    image1 = Image.open(uploaded_image)
    image2 = Image.open(forensic_image)

    # Display side by side
    col1, col2 = st.columns(2)
    with col1:
        st.image(image1, caption="Uploaded Image", use_column_width=True)
    with col2:
        st.image(image2, caption="Forensic Reference Image", use_column_width=True)

    # Extract Metadata
    st.write("### Metadata and Comparison")

    # Get file size (in KB)
    image1_size = len(uploaded_image.getbuffer()) / 1024
    image2_size = len(forensic_image.getbuffer()) / 1024

    # Get image resolution
    image1_resolution = image1.size  # (width, height)
    image2_resolution = image2.size

    st.write(f"**Uploaded Image File Size:** {image1_size:.2f} KB, Resolution: {image1_resolution}")
    st.write(f"**Forensic Image File Size:** {image2_size:.2f} KB, Resolution: {image2_resolution}")

    # Visualization: File Size and Resolution (only if matplotlib is available)
    if matplotlib_available:
        st.write("### Graphical Analysis")

        # Plot file sizes
        fig, ax = plt.subplots()
        ax.bar(["Uploaded Image", "Forensic Image"], [image1_size, image2_size], color=["blue", "green"])
        ax.set_title("File Size Comparison")
        ax.set_ylabel("File Size (KB)")
        st.pyplot(fig)

        # Plot resolution (width x height)
        fig, ax = plt.subplots()
        ax.bar(
            ["Uploaded Image Width", "Forensic Image Width"],
            [image1_resolution[0], image2_resolution[0]],
            color="orange",
        )
        ax.bar(
            ["Uploaded Image Height", "Forensic Image Height"],
            [image1_resolution[1], image2_resolution[1]],
            color="purple",
        )
        ax.set_title("Image Resolution Comparison")
        ax.set_ylabel("Pixels")
        st.pyplot(fig)

elif uploaded_image or forensic_image:
    st.warning("Please upload both images to display, analyze, and visualize them.")

# Footer
st.markdown("---")
st.write("Built with Streamlit for forensic scanner identification.")
