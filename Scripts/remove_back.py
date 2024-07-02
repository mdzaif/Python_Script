#!/usr/bin/env python3
# Description: Remove the background of a signature for official documents.
# Python version: 3.x

import tkinter as tk
from tkinter import filedialog
import rembg
from PIL import Image
import cv2
import numpy as np
import os


def fetch_file():
    root = tk.Tk()
    root.geometry("1200x750")
    root.withdraw()
    file = filedialog.askopenfilename(
        parent = root,
        title = 'Choose Files'
    )
    return file

def fetch_output():
    r = tk.Tk()
    r.geometry("1200x750")
    r.withdraw()
    p = filedialog.askdirectory(
        parent = r,
        title = 'Choose Output\'s File Path'
    )
    return p


file_path = str(fetch_file())
select_output_path = str(fetch_output())
output_file = input("Enter the new file name: ")
output_file = output_file.strip()
os_type = os.name
if os_type == 'posix': #Linux
    path = select_output_path +'/'+ output_file
elif os_type == 'nt': # windows
    path = select_output_path + '\\' + output_file

gray_image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
# Apply histogram equalization
equalized_image = cv2.equalizeHist(gray_image)
cv2.imwrite(path, equalized_image)

#open file
into = Image.open(path)
# remove background
out = rembg.remove(into)
# save the output
out.save(path)
print("File saved in %s" %path)
