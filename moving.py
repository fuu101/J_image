import os
import shutil
import creating

def JPG_from(source_folder, destination_folder):
    os.chdir(source_folder)

    for image_folder in os.listdir():
        if os.path.isfile(image_folder): continue
        os.chdir(f"{source_folder}\{image_folder}")

        for file in os.listdir():
            if os.path.isdir(file): continue
            elif file.lower().endswith(".jpg"):
                try:
                    shutil.copy(f"{source_folder}\{image_folder}\{file}", f"{destination_folder}\{image_folder}\{file}")
                except OSError as error:
                    print(f"Unable to move {file}.  -- [The folder {image_folder} does not exist]")

        os.chdir(f"{source_folder}")

    creating.folder_ABC_in(destination_folder)  

# Function test
# JPG_from(r"C:\Users\Dell\Desktop\test1", r"C:\Users\Dell\Desktop\test2")




