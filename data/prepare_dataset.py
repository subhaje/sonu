import os
import shutil
from pathlib import Path
import cv2
from PIL import Image

def validate_image(image_path):
    """Validate if the image meets the requirements"""
    try:
        # Check if image can be opened
        img = Image.open(image_path)
        
        # Check format
        if img.format not in ['JPEG', 'JPG', 'PNG']:
            return False, f"Invalid format: {img.format}"
        
        # Check resolution
        width, height = img.size
        if width < 224 or height < 224:
            return False, f"Image too small: {width}x{height}"
        
        return True, "Image valid"
    except Exception as e:
        return False, str(e)

def organize_dataset(source_dir, target_dir):
    """Organize and validate images for the dataset"""
    # Create target directories if they don't exist
    dent_dir = Path(target_dir) / 'dent'
    no_dent_dir = Path(target_dir) / 'no_dent'
    dent_dir.mkdir(parents=True, exist_ok=True)
    no_dent_dir.mkdir(parents=True, exist_ok=True)
    
    # Statistics
    stats = {'processed': 0, 'invalid': 0, 'dent': 0, 'no_dent': 0}
    
    # Process each image
    source_path = Path(source_dir)
    for img_path in source_path.glob('**/*'):
        if img_path.suffix.lower() in ['.jpg', '.jpeg', '.png']:
            is_valid, message = validate_image(img_path)
            
            if is_valid:
                # Ask user to classify the image
                print(f"\nProcessing: {img_path.name}")
                img = cv2.imread(str(img_path))
                cv2.imshow('Image', img)
                key = cv2.waitKey(0)
                cv2.destroyAllWindows()
                
                # 'd' for dent, 'n' for no dent, 'q' to quit
                if key == ord('d'):
                    target = dent_dir / img_path.name
                    shutil.copy2(img_path, target)
                    stats['dent'] += 1
                elif key == ord('n'):
                    target = no_dent_dir / img_path.name
                    shutil.copy2(img_path, target)
                    stats['no_dent'] += 1
                elif key == ord('q'):
                    break
                
                stats['processed'] += 1
            else:
                print(f"Invalid image {img_path.name}: {message}")
                stats['invalid'] += 1
    
    return stats

def main():
    print("Dent Detection Dataset Preparation Tool")
    print("=====================================\n")
    print("Instructions:")
    print("1. Press 'd' if the image shows a dent")
    print("2. Press 'n' if the image has no dent")
    print("3. Press 'q' to quit\n")
    
    source_dir = input("Enter the source directory containing images: ")
    target_dir = input("Enter the target directory (or press Enter for 'data'): ") or 'data'
    
    stats = organize_dataset(source_dir, target_dir)
    
    print("\nProcessing Complete!")
    print(f"Processed: {stats['processed']} images")
    print(f"Invalid: {stats['invalid']} images")
    print(f"Dent: {stats['dent']} images")
    print(f"No Dent: {stats['no_dent']} images")

if __name__ == '__main__':
    main()