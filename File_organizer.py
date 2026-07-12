import os
import pathlib
import shutil

fileFormat = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
    "Video": [".mp4", ".avi", ".mkv", ".mov", ".flv", ".wmv"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".java", ".c", ".cpp", ".js", ".html", ".css"],
}

print("===== File Organizer Started =====\n")

# Scan all files in the current directory
for file in os.scandir():

    # Skip folders
    if file.is_dir():
        continue

    filePath = pathlib.Path(file.path)

    # File name and extension
    fileName = filePath.name
    extension = filePath.suffix.lower()

    # Show file details
    print(f"File Name : {fileName}")
    print(f"Extension : {extension}")

    destinationFolder = "Other"

    # Find the correct folder
    for folder, extensions in fileFormat.items():
        if extension in extensions:
            destinationFolder = folder
            break

    # Create folder if it doesn't exist
    os.makedirs(destinationFolder, exist_ok=True)

    source = file.path
    destination = os.path.join(destinationFolder, fileName)

    try:
        shutil.move(source, destination)
        print(f"Moved To : {destinationFolder}")
    except Exception as e:
        print(f"Error    : {e}")

    print("-" * 40)

print("\n===== File Organizer Completed =====")