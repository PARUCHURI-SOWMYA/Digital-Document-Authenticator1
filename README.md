import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Function to simulate forensic image processing
def forensic_image_processing(image):
    # Convert to grayscale as an example forensic processing step
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Example forensic enhancement - using edge detection (you can replace this with any forensic technique)
    edges = cv2.Canny(gray_image, 100, 200)
    
    return edges

# Function to load and process the uploaded image
def process_uploaded_image(uploaded_file):
    # Open the image using PIL
    image = Image.open(uploaded_file)
    
    # Convert the PIL image to a NumPy array for OpenCV processing
    image = np.array(image)
    
    # Apply forensic image processing
    processed_image = forensic_image_processing(image)
    
    return processed_image

# Main function for the Streamlit app
def main():
    st.title("Forensic Image Processor")
    
    st.write("Upload a normal image, and we will process it to give you the forensic version.")
    
    # Image upload interface
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        # Display the uploaded image
        original_image = Image.open(uploaded_file)
        st.image(original_image, caption="Original Image", use_column_width=True)
        
        # Process the image
        processed_image = process_uploaded_image(uploaded_file)
        
        # Show the forensic image (processed image)
        st.image(processed_image, caption="Forensic Processed Image", use_column_width=True)
    
# Run the Streamlit app
if __name__ == "__main__":
    main()
