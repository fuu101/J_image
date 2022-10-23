import os
import renaming, removing, creating, moving, printing2, submitting
# // pip install send2trash // before use

def remove_and_rename():
    removing.invoice(desktop)
    renaming.NEF_file(desktop)
    
user_path = os.path.expanduser("~")
desktop_copy = os.path.join(user_path, r"Desktop\Complete")
desktop = os.path.join(user_path, r"Desktop\10-13")
dropbox = os.path.join(user_path, r"Dropbox\Cambodia\2022\10-14")

# remove_and_rename() 

# removing.NEF_file(desktop_copy)
# removing.lightexp_folder(desktop)

# submitting.edited_image(desktop_copy, dropbox)
# submitting.edited_image(desktop, dropbox)

# printing2.result(dropbox) 




