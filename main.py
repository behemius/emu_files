import os
import shutil
import sys

files_dir=input('Provide files directory: ')
#files_dir=r'H:\temp'

# Moving all files from subdirectories to working directory and removing empty subfolders
for root,subdirs,files in os.walk(files_dir) :
 if root!=files_dir :
     for file in files:
         path = os.path.join(root,file)
         shutil.move(path,files_dir)
     os.rmdir(root)

# Moving files + creation subdirectories
for root,subdirs,files in os.walk(files_dir) :
    for file in files :
        first_char=file[0].lower()
        if first_char.isdigit() : first_char='0'
        path2 = os.path.join(files_dir,first_char)
        if not os.path.exists(path2) : os.mkdir(path2) 
        path = os.path.join(files_dir,file)
        new_path = os.path.join(files_dir,first_char)
        shutil.move(path,new_path)








