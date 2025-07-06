import os
import shutil

folder_path = r"E:\ULTIMATE DATA SCIENCE\DATA-SCIENCE-PROJECTS\Python\UnOrganised_folder"

file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Videos': ['.mp4', '.mov', '.mkv'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Music': ['.mp3', '.wav']
}

for folder in file_types:
    path = os.path.join(folder_path, folder)
    if not os.path.exists(path):
        os.makedirs(path)

for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if os.path.isdir(file_path):
        continue

    _, ext = os.path.splitext(file)
    moved = False

    for category, extensions in file_types.items():
        if ext.lower() in extensions:
            dest_path = os.path.join(folder_path, category, file)
            shutil.move(file_path, dest_path)
            print(f"Moved {file} to {category}")
            moved = True
            break

    if not moved:
        other_path = os.path.join(folder_path, 'Others')
        if not os.path.exists(other_path):
            os.makedirs(other_path)
        shutil.move(file_path, os.path.join(other_path, file))
        print(f"Moved {file} to Others")
