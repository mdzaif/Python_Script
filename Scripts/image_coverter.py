from PIL import Image
import argparse
import os
# Set up argument parser
parser = argparse.ArgumentParser()
parser.add_argument('--image', type=str, help="/path/to/image/file")
parser.add_argument('--format', type=str, help='png/jpg/tiff/bmp/webp/ico')
parser.add_argument('--output', type=str, help ='path/where/to/save/don\'t/ use the file name(use "" if space occured)')
args = parser.parse_args()

image = args.image.strip()
format = args.format.lower().strip()  # Make sure the format is in lowercase for easier handling
output = args.output.strip()[:-1]
print(f"Image: {image}")
print(f"Format: {format}")
print(f"Output path: {output}")
# Open the image file
with Image.open(image) as img:
    # Check the image mode and convert to 'RGB' if necessary for certain formats
    if img.mode not in ['RGB', 'L'] and format in ['jpg', 'bmp', 'webp', 'ico']:
        img = img.convert('RGB')
    
    # Determine the correct filename for saving
    if image.lower().endswith('.png'):
        if format == 'jpg':
            convert_img = f"{os.path.splitext(os.path.basename(image))[0]}.jpg"
            img.save(f"{output}/{convert_img}", format='JPEG')
        elif format == 'tiff':
            convert_img = f"{os.path.splitext(os.path.basename(image))[0]}.tiff"
            img.save(f"{output}/{convert_img}", format='TIFF')
        elif format == 'bmp':
            convert_img = f"{os.path.splitext(os.path.basename(image))[0]}.bmp"
            img.save(f"{output}/{convert_img}", format='BMP')
        elif format == 'webp':
            convert_img = f"{os.path.splitext(os.path.basename(image))[0]}.webp"
            img.save(f"{output}/{convert_img}", format='WEBP')
        elif format == 'ico':
            convert_img = f"{os.path.splitext(os.path.basename(image))[0]}.ico"
            img.save(f"{output}/{convert_img}", format='ICO')
        else:
            print("Unsupported format or same as older file format!")
    elif image.lower().endswith('.jpg'):
        if format == 'png':
            convert_img = f"{os.path.splitext(os.path.basename(image))[0]}.png"
            img.save(f"{output}/{convert_img}", format='PNG')
        elif format == 'tiff':
            convert_img = f"{os.path.splitext(os.path.basename(image))[0]}.tiff"
            img.save(f"{output}/{convert_img}", format='TIFF')
        elif format == 'bmp':
            convert_img = f"{os.path.splitext(os.path.basename(image))[0]}.bmp"
            img.save(f"{output}/{convert_img}", format='BMP')
        elif format == 'webp':
            convert_img = f"{os.path.splitext(os.path.basename(image))[0]}.webp"
            img.save(f"{output}/{convert_img}", format='WEBP')
        elif format == 'ico':
            convert_img = f"{os.path.splitext(os.path.basename(image))[0]}.ico"
            img.save(f"{output}/{convert_img}", format='ICO')
        else:
            print("Unsupported format or same as older file format!")
    elif image.lower().endswith('.tiff'):
        if format == 'jpg':
            convert_img = f"{os.path.splitext(os.path.basename(image))[0]}.jpg"
            img.save(f"{output}/{convert_img}", format='JPEG')
        elif format == 'png':
            convert_img = f"{os.path.splitext(os.path.basename(image))[0]}.png"
            img.save(f"{output}/{convert_img}", format='PNG')
        elif format == 'bmp':
            convert_img = f"{os.path.splitext(os.path.basename(image))[0]}.bmp"
            img.save(f"{output}/{convert_img}", format='BMP')
        elif format == 'webp':
            convert_img = f"{os.path.splitext(os.path.basename(image))[0]}.webp"
            img.save(f"{output}/{convert_img}", format='WEBP')
        elif format == 'ico':
            convert_img = f"{os.path.splitext(os.path.basename(image))[0]}.ico"
            img.save(f"{output}/{convert_img}", format='ICO')
        else:
            print("Unsupported format or same as older file format!")
    elif image.lower().endswith('.bmp'):
        if format == 'jpg':
            convert_img = f"{os.path.splitext(os.path.basename(image))[0]}.jpg"
            img.save(f"{output}/{convert_img}", format='JPEG')
        elif format == 'png':
            convert_img = f"{os.path.splitext(os.path.basename(image))[0]}.png"
            img.save(f"{output}/{convert_img}", format='PNG')
        elif format == 'tiff':
            convert_img = f"{os.path.splitext(os.path.basename(image))[0]}.tiff"
            img.save(f"{output}/{convert_img}", format='TIFF')
        elif format == 'webp':
            convert_img = f"{os.path.splitext(os.path.basename(image))[0]}.webp"
            img.save(f"{output}/{convert_img}", format='WEBP')
        elif format == 'ico':
            convert_img = f"{os.path.splitext(os.path.basename(image))[0]}.ico"
            img.save(f"{output}/{convert_img}", format='ICO')
        else:
            print("Unsupported format or same as older file format!")
    elif image.lower().endswith('.webp'):
        if format == 'jpg':
            convert_img = f"{os.path.splitext(os.path.basename(image))[0]}.jpg"
            img.save(f"{output}/{convert_img}", format='JPEG')
        elif format == 'png':
            convert_img = f"{os.path.splitext(os.path.basename(image))[0]}.png"
            img.save(f"{output}/{convert_img}", format='PNG')
        elif format == 'tiff':
            convert_img = f"{os.path.splitext(os.path.basename(image))[0]}.tiff"
            img.save(f"{output}/{convert_img}", format='TIFF')
        elif format == 'bmp':
            convert_img = f"{os.path.splitext(os.path.basename(image))[0]}.bmp"
            img.save(f"{output}/{convert_img}", format='BMP')
        elif format == 'ico':
            convert_img = f"{os.path.splitext(os.path.basename(image))[0]}.ico"
            img.save(f"{output}/{convert_img}", format='ICO')
        else:
            print("Unsupported format or same as older file format!")
    elif image.lower().endswith('ico'):
        if format == 'jpg':
            convert_img = f"{os.path.splitext(os.path.basename(image))[0]}.jpg"
            img.save(f"{output}/{convert_img}", format='JPEG')
        elif format == 'png':
            convert_img = f"{os.path.splitext(os.path.basename(image))[0]}.png"
            img.save(f"{output}/{convert_img}", format='PNG')
        elif format == 'tiff':
            convert_img = f"{os.path.splitext(os.path.basename(image))[0]}.tiff"
            img.save(f"{output}/{convert_img}", format='TIFF')
        elif format == 'bmp':
            convert_img = f"{os.path.splitext(os.path.basename(image))[0]}.bmp"
            img.save(f"{output}/{convert_img}", format='BMP')
        elif format == 'webp':
            convert_img = f"{os.path.splitext(os.path.basename(image))[0]}.webp"
            img.save(f"{output}/{convert_img}", format='WEBP')
        else:
            print("Unsupported format or same as older file format!")
if os.path.exists(f"{output}/{convert_img}"):
    print(f"file saved on: {output}/{convert_img}")
else:
    print("Faild to save the file!")