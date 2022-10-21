import os
import shutil
from send2trash import send2trash

# Remove invoice 
def invoice_in(date_folder):
    os.chdir(date_folder)

    for image_folder in os.listdir():
        if os.path.isfile(image_folder): continue
        os.chdir(f"{date_folder}\{image_folder}")
        
        try:
            for item_in_imagefolder in os.listdir():                
                if item_in_imagefolder.startswith(image_folder) and (item_in_imagefolder.lower().endswith('.jpg')): 
                    send2trash(item_in_imagefolder)
                else: continue
        except OSError as error:
            print (f'{error}')

# Remove NEF files 
def NEF_in(date_folder):
    os.chdir(date_folder)

    for image_folder in os.listdir():
        if os.path.isfile(image_folder): continue
        os.chdir(f"{date_folder}\{image_folder}")

        try:
            # remove NEF
            for item_in_imagefolder in os.listdir():
                if (item_in_imagefolder.lower().endswith('.nef') or item_in_imagefolder.lower().endswith('.dng')): 
                    send2trash(item_in_imagefolder)
                else: continue
        except OSError as error:
            print (f'{error}')

# Remove light.exp folder
def folder_lightExp_in(date_folder):
    os.chdir(date_folder)
    
    for image_folder in os.listdir():
        if os.path.isfile(image_folder): continue
        os.chdir(f"{date_folder}\{image_folder}")
        
        try:
            send2trash("light.exp")
        except OSError as error:
            print (f'{error}')

# Remove A, B , C folders
def folder_ABCharley_in(date_folder):
    os.chdir(date_folder)

    for image_folder in os.listdir():
        os.chdir(f"{date_folder}\{image_folder}")

        try:
            send2trash("A")
            send2trash("B")
            send2trash("Charley")
        except OSError as error:
            print (f'{error}')

# Function Test
# folder_ABCharley_in(r"C:\Users\Dell\Desktop\test2")