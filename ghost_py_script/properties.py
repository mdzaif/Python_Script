import os
import sys
import datetime
#import mimetypes
import magic
from PIL import Image
from moviepy.editor import VideoFileClip
from mutagen import File as AudioFile

def get_file_properties(file_path):

    # Get the MIME type of the file
    mime_type = magic.from_file(file_path)

    # Get file size in bytes and convert to MB
    file_size = os.path.getsize(file_path)
    file_size_mb = file_size / (1024 * 1024)
    file_created = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
    file_last_modified = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
    

    print(f"File: {file_path}")
    print(f"First Created: {file_created}")
    print(f"Last Modified: {file_last_modified}")
    print(f"Size: {file_size_mb:.2f} MB ({file_size} bytes)")
    print(f"Type: {mime_type}")
    

    # If the file is an image
    if mime_type and mime_type.startswith('image'):
        try:
            with Image.open(file_path) as img:
                width, height = img.size
                print(f"Image Dimensions: {width} x {height}")
                print(f"Image Format: {img.format}")
                print(f"Image Mode: {img.mode}")
                has_alpha = 'A' in img.mode
                print(f"Has Alpha Channel: {has_alpha}")
        except Exception as e:
            print(f"Error processing image: {e}")

    # If the file is a video
    elif mime_type and mime_type.startswith('video'):
        try:
            clip = VideoFileClip(file_path)
            width, height = clip.size
            print(f"Video Dimensions: {width} x {height}")
            print(f"Video Duration: {clip.duration:.2f} seconds")
        except Exception as e:
            print(f"Error processing video: {e}")

    # If the file is audio
    elif mime_type and mime_type.startswith('audio'):
        try:
            audio = AudioFile(file_path)
            duration = audio.info.length
            print(f"Audio Duration: {duration:.2f} seconds")
        except Exception as e:
            print(f"Error processing audio: {e}")

    # For any other file types (text, pdf, etc.)
    else:
        print(f"Unable to retrieve specific properties for this file type.")

    print('-' * 40)


# Main execution
if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("Usage: python properties.py <file-path>")
    else:
        file = sys.argv
        file.pop(0)
        for f in file:
            if os.path.isfile(f):
                get_file_properties(f)
            else:
                print(f"File not found: {f}")
