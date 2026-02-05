import os

def rename_files(folder_path, prefix):
    files = os.listdir(folder_path)

    count = 1
    for file in files:
        old_path = os.path.join(folder_path, file)

        if os.path.isfile(old_path):
            extension = os.path.splitext(file)[1]
            new_name = f"{prefix}_{count}{extension}"
            new_path = os.path.join(folder_path, new_name)

            os.rename(old_path, new_path)
            count += 1

    print("Done renaming files.")

def main():
    folder = input("Enter folder path: ")
    prefix = input("Enter prefix name: ")

    rename_files(folder, prefix)

if __name__ == "__main__":
    main()
