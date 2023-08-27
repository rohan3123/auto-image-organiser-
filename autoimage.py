import os
import shutil

# Path to your Downloads folder
downloads_folder = "C:\Users\false\Downloads"
meme_folder = "C:\Users\false\Downloads\meme"

# Ensure the meme folder exists
if not os.path.exists(meme_folder):
    os.makedirs(meme_folder)
    
# List all files in the downloads folder
downloaded_files = os.listdir(downloads_folder)

# List of image file extensions
image_extensions = ['.jpg', '.jpeg', '.png', '.gif']