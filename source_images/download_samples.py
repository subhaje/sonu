import os
import requests
from PIL import Image
from io import BytesIO

# Sample image URLs (mix of dented and non-dented panels)
SAMPLE_IMAGES = [
    # Dented panels
    "https://raw.githubusercontent.com/openimages/dataset/main/images/car_dent_1.jpg",
    "https://raw.githubusercontent.com/openimages/dataset/main/images/car_dent_2.jpg",
    "https://raw.githubusercontent.com/openimages/dataset/main/images/car_dent_3.jpg",
    # Non-dented panels
    "https://raw.githubusercontent.com/openimages/dataset/main/images/car_panel_1.jpg",
    "https://raw.githubusercontent.com/openimages/dataset/main/images/car_panel_2.jpg",
    "https://raw.githubusercontent.com/openimages/dataset/main/images/car_panel_3.jpg",
]

def download_image(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        # Verify image and size
        img = Image.open(BytesIO(response.content))
        width, height = img.size
        
        if width >= 224 and height >= 224:
            img.save(save_path)
            print(f"Downloaded: {save_path}")
            return True
        else:
            print(f"Image too small: {width}x{height}")
            return False
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")
        return False

def main():
    # Create source_images directory if it doesn't exist
    os.makedirs('source_images', exist_ok=True)
    
    # Download sample images
    for i, url in enumerate(SAMPLE_IMAGES, 1):
        save_path = os.path.join('source_images', f'sample_{i}.jpg')
        download_image(url, save_path)

if __name__ == '__main__':
    main()
    print("\nDownload complete! You can now run prepare_dataset.py to organize the images.")