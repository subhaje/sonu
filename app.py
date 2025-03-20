import streamlit as st
import cv2
import numpy as np
from pathlib import Path
from dent_detection import DentDetector

st.set_page_config(page_title="Dent Detection System", layout="wide")

st.title("Mechanical Panel Dent Detection System")

# Initialize the dent detector
dent_detector = DentDetector()

# File uploader
uploaded_file = st.file_uploader("Upload an image of the panel", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Create columns for layout
    col1, col2 = st.columns(2)
    
    # Save the uploaded file temporarily
    temp_path = Path("temp_image.jpg")
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Read and display the original image
    image = cv2.imread(str(temp_path))
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    with col1:
        st.subheader("Original Image")
        st.image(image_rgb, use_column_width=True)
    
    # Perform dent detection
    detection_result = dent_detector.detect_dents(temp_path)
    severity_info = dent_detector.analyze_dent_severity(temp_path)
    
    with col2:
        st.subheader("Detection Results")
        st.write(f"Dent Detected: {'Yes' if detection_result['has_dent'] else 'No'}")
        st.write(f"Confidence: {detection_result['confidence']:.2f}")
        
        if detection_result['has_dent']:
            st.subheader("Dent Analysis")
            for idx, dent in enumerate(severity_info, 1):
                st.write(f"Dent #{idx}:")
                st.write(f"- Area: {dent['area']:.2f} pixels²")
                st.write(f"- Width: {dent['width']} pixels")
                st.write(f"- Height: {dent['height']} pixels")
                st.write(f"- Location: (x={dent['location'][0]}, y={dent['location'][1]})")
    
    # Clean up
    temp_path.unlink()

# Instructions
st.sidebar.title("Instructions")
st.sidebar.write("""
1. Upload an image of the mechanical panel
2. The system will automatically detect dents
3. View detection results and measurements
4. For best results:
   - Ensure good lighting
   - Capture clear, focused images
   - Avoid reflections
""")