#!/usr/bin/env python3
"""
Resize images to have a maximum dimension of 300px while maintaining aspect ratio.
"""
from PIL import Image
import os
from pathlib import Path

def resize_image(image_path, max_dimension=300):
    """Resize image if either dimension exceeds max_dimension."""
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            
            # Check if resizing is needed
            if width <= max_dimension and height <= max_dimension:
                print(f"✓ {image_path.name} - No resize needed ({width}x{height})")
                return False
            
            # Calculate new dimensions maintaining aspect ratio
            if width > height:
                new_width = max_dimension
                new_height = int((max_dimension / width) * height)
            else:
                new_height = max_dimension
                new_width = int((max_dimension / height) * width)
            
            # Resize and save
            resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            resized_img.save(image_path, quality=95, optimize=True)
            
            print(f"✓ {image_path.name} - Resized from {width}x{height} to {new_width}x{new_height}")
            return True
            
    except Exception as e:
        print(f"✗ Error processing {image_path.name}: {e}")
        return False

def process_quiz_images(quiz_name):
    """Process all images in a quiz directory."""
    images_dir = Path(f"tests/{quiz_name}/images")
    
    if not images_dir.exists():
        print(f"Directory not found: {images_dir}")
        return
    
    print(f"\n{'='*60}")
    print(f"Processing {quiz_name}")
    print(f"{'='*60}")
    
    image_files = list(images_dir.glob("*.png")) + list(images_dir.glob("*.jpg"))
    
    if not image_files:
        print(f"No images found in {images_dir}")
        return
    
    resized_count = 0
    for image_path in sorted(image_files):
        if resize_image(image_path):
            resized_count += 1
    
    print(f"\nTotal: {len(image_files)} images, {resized_count} resized")

if __name__ == "__main__":
    os.chdir(Path(__file__).parent)
    
    # Process both quiz sets
    process_quiz_images("Quiz 2 V2")
    process_quiz_images("Quiz 2 V3")
    
    print(f"\n{'='*60}")
    print("✓ All images processed!")
    print(f"{'='*60}")
