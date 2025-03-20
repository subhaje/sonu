import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from pathlib import Path

class DentDetector:
    def __init__(self):
        self.model = self._build_model()
    
    def _build_model(self):
        """Build a CNN model for dent detection"""
        model = models.Sequential([
            layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(64, (3, 3), activation='relu'),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(64, (3, 3), activation='relu'),
            layers.Flatten(),
            layers.Dense(64, activation='relu'),
            layers.Dense(1, activation='sigmoid')
        ])
        model.compile(optimizer='adam',
                    loss='binary_crossentropy',
                    metrics=['accuracy'])
        return model
    
    def preprocess_image(self, image_path):
        """Preprocess the input image for dent detection"""
        img = cv2.imread(str(image_path))
        img = cv2.resize(img, (224, 224))
        img = img / 255.0  # Normalize pixel values
        return img
    
    def detect_dents(self, image_path):
        """Detect dents in the given image"""
        # Preprocess image
        img = self.preprocess_image(image_path)
        
        # Add batch dimension
        img_batch = np.expand_dims(img, 0)
        
        # Get prediction
        prediction = self.model.predict(img_batch)
        
        # Process results
        # Here we'll add more sophisticated dent analysis logic
        return {
            'has_dent': bool(prediction[0] > 0.5),
            'confidence': float(prediction[0])
        }
    
    def analyze_dent_severity(self, image_path):
        """Analyze the severity and dimensions of detected dents"""
        img = cv2.imread(str(image_path))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Apply image processing techniques
        blurred = cv2.GaussianBlur(gray, (11, 11), 0)
        thresh = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)[1]
        
        # Find contours
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        dent_info = []
        for contour in contours:
            # Calculate contour properties
            area = cv2.contourArea(contour)
            perimeter = cv2.arcLength(contour, True)
            x, y, w, h = cv2.boundingRect(contour)
            
            # Store dent information
            if area > 100:  # Filter out small noise
                dent_info.append({
                    'area': area,
                    'perimeter': perimeter,
                    'width': w,
                    'height': h,
                    'location': (x, y)
                })
        
        return dent_info