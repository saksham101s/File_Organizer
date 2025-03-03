import os
import shutil
import sys
def organize_files(target_dir):
    # Define file categories and their extensions
    file_categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
        "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".md", ".csv"],
        "Audio": [".mp3", ".wav", ".flac", ".aac"],
        "Video": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv"],
        "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"]
    }

    # Validate target directory
    if not os.path.isdir(target_dir):
        print(f"Error: Directory '{target_dir}' does not exist.")
        return

    # Process files in target directory
    for filename in os.listdir(target_dir):
        file_path = os.path.join(target_dir, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get file extension and determine category
        _, ext = os.path.splitext(filename)
        ext = ext.lower()
        category = "Others"
        
        for cat, exts in file_categories.items():
            if ext in exts:
                category = cat
                break

        # Create category directory if needed
        dest_dir = os.path.join(target_dir, category)
        os.makedirs(dest_dir, exist_ok=True)

        # Move file to category directory
        try:
            shutil.move(file_path, dest_dir)
            print(f"Moved '{filename}' to '{category}' folder")
        except Exception as e:
            print(f"Error moving '{filename}': {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python organize_files.py <target_directory>")
        sys.exit(1)
    
    target_directory = sys.argv[1]
    organize_files(target_directory)