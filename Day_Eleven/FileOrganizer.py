import os
import shutil

# File type categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov", ".wmv"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".java", ".cpp", ".js", ".html", ".css"],
    "Exe_Files": [".msi", ".exe"],
    "DLL_Files": [".dll"],
    "ARDUINO SCRIPTS": [".ino"],
    "Fritzing_Files": [".fzp", ".fzpz"]
}

def organize_files(directory):
    if not os.path.exists(directory):
        print("Error: Directory does not exist.")
        return
    
    # Create category folders if they don't exist
    for category in FILE_CATEGORIES.keys():
        folder_path = os.path.join(directory, category)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    
    # Move files to respective folders
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        if os.path.isfile(file_path):  # Ignore folders
            file_ext = os.path.splitext(filename)[1].lower()
            for category, extensions in FILE_CATEGORIES.items():
                if file_ext in extensions:
                    shutil.move(file_path, os.path.join(directory, category, filename))
                    print(f"Moved: {filename} → {category}")
                    break
    
    # Remove empty folders
    remove_empty_folders(directory)
    print("✅ File organization complete!")

def remove_empty_folders(directory):
    for folder in os.listdir(directory):
        folder_path = os.path.join(directory, folder)
        if os.path.isdir(folder_path) and not os.listdir(folder_path):
            os.rmdir(folder_path)
            print(f"Removed empty folder: {folder}")

if __name__ == "__main__":
    dir_path = input("Enter the directory path to organize: ")
    organize_files(dir_path)
