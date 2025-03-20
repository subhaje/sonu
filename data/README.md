# Dataset Structure for Dent Detection

This directory contains the training dataset for the mechanical panel dent detection system.

## Directory Structure

```
data/
├── dent/         # Images of panels with dents
└── no_dent/      # Images of panels without dents
```

## Image Requirements

- Format: JPG, JPEG, or PNG
- Resolution: Minimum 224x224 pixels (images will be resized during training)
- Lighting: Well-lit images with minimal glare
- Focus: Clear, sharp images
- Background: Consistent, neutral background when possible

## Dataset Guidelines

1. Each subdirectory should contain at least 100 images for better model training
2. Images should cover various:
   - Dent sizes
   - Dent shapes
   - Panel materials
   - Lighting conditions
   - Viewing angles

## Data Collection Tips

1. Capture images from multiple angles
2. Include both shallow and deep dents
3. Vary the distance from the panel
4. Use consistent lighting when possible
5. Include images with different panel colors and textures