import splitfolders  # or import split_folders
import os

dr = r'C:\Users\xxcbj\Desktop\Sign_language_detection\Data'
output_dir = r'C:\Users\xxcbj\Desktop\Sign_language_detection\Data'

if os.path.exists(dr):
    splitfolders.ratio(dr, output_dir, ratio=(0.8, 0.2))
else:
    print(f"The provided input folder '{dr}' does not exist.")
