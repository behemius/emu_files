# emu_files
Script which move files to alphabetic folders.

Idea of this script is, that you have for example 100.000 files in one directory. 
For better reviewing them, script creates 0,A-Z subfolders and move all files based on first letter (or digit) to proper subfolder. 

Mostly it's used when you have collection of 8-bit/16-bit  emulators files and then you would like to review them in emulator software.

What script exactly does:
1. Getting working directory
2. Checking subfolders, move files from them to working directory and deletes empty subfolders
3. Creates 0,a-z directories
4. Move files to proper number/letter subfolder
5. Zip without compressiont every directory into working directory (It's not done... I cannot get it with shutil.make_archive module)
