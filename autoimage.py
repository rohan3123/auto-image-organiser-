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

# Move image files to the meme folder
for filename in downloaded_files:
    if any(filename.lower().endswith(ext) for ext in image_extensions):
        source_path = os.path.join(downloads_folder, filename)
        destination_path = os.path.join(meme_folder, filename)
        
        # Check if the file already exists in the destination folder
        if os.path.exists(destination_path):
            print(f"File '{filename}' already exists in the meme folder.")
        else:
            shutil.move(source_path, destination_path)
            print(f"Moved '{filename}' to meme folder.")

print("Image moving process completed!")