import os
import shutil

# change this to any folder you want to organize
FOLDER = "."

FILE_TYPES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "PDFs": [".pdf"],
    "Videos": [".mp4", ".mkv"],
    "Archives": [".zip", ".rar"],
    "Code": [".py", ".js", ".html", ".css"],
}


def organize_folder():
    for filename in os.listdir(FOLDER):
        file_path = os.path.join(FOLDER, filename)

        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()

            for folder_name, extensions in FILE_TYPES.items():
                if ext in extensions:
                    dest_folder = os.path.join(FOLDER, folder_name)

                    os.makedirs(dest_folder, exist_ok=True)

                    shutil.move(file_path, os.path.join(dest_folder, filename))
                    print(f"Moved {filename} → {folder_name}")
                    break


if __name__ == "__main__":
    organize_folder()
