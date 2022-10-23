import os

# create folder A, B, Charley in image_folder
NEWFOLDERS = ['A', 'B', 'Charley']

def ABCharely_folder(date_folder):
    
    os.chdir(date_folder)
    for image_folder in os.listdir():
        if os.path.isfile(image_folder): continue
        os.chdir(f"{date_folder}\{image_folder}")

        try:
            for newfolder in NEWFOLDERS:
                os.mkdir(f"{os.getcwd()}\{newfolder}")
        except OSError as error:
            print (f"folder A,B,Charley already created in {image_folder}")
        
        os.chdir(f"{date_folder}")

# test function
# folder_ABC_in(r"C:\Users\sivla\Desktop\Complete1")