import os

def NEF_in(date_folder):
    # e.g. date_folder = 9-30
    os.chdir(date_folder)

    # e.g. image_folder = 10-1-2022-0491
    for image_folder in os.listdir():    
        if os.path.isfile(image_folder): continue                                  
        os.chdir(f"{date_folder}\{image_folder}")
        
        try:
            for item_in_subfolder in os.listdir():
                if(os.path.isdir(item_in_subfolder)): continue
                elif item_in_subfolder.lower().endswith(".jpg"): continue
                
                # rename processing
                original_name = item_in_subfolder
                new_name = image_folder+ '-' + original_name[-8:]
                os.rename(original_name, new_name)

        except OSError as error:
            print (error)
            print (f'{error}')