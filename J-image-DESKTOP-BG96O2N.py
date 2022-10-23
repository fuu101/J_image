import os
import renaming, removing, creating, moving, printing2, submitting

def remove_and_rename():
    removing.invoice_in(desktop)
    renaming.NEF_in(desktop)
    
user_path = os.path.expanduser("~")
desktop_newF = os.path.join(user_path, r"Desktop\MewF14")
desktop = os.path.join(user_path, r"Desktop\10-14")
dropbox = os.path.join(user_path, r"Dropbox\Cambodia\2022\10-14")

# remove_and_rename() 

# removing.NEF_in(desktop_newF)
# removing.folder_lightExp_in(desktop)

# moving.JPG_from(desktop, dropbox)
# moving.JPG_from(desktop_newF, dropbox)

# copying.JPG_from(desktop_newF, dropbox)
# copying.JPG_from(desktop, dropbox)

printing2.ABC_result_of(dropbox) 




