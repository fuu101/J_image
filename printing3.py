# count how many files there are in folderA, B, C and Charley

import os

def ABC_result_of(dirName):

    class DataTable:
        
        def __init__(self, name, A, B, C, unrated, NEF):
            self.name = name
            self.A = 0
            self.B = 0
            self.C = 0
            self.unrated = 0
            self.NEF = 0

        def getTotalJpeg(self):
            """The total number of photos edited in a subfolder. It includes A, B, C and unrated photos"""
            self.jpg = self.A + self.B + self.C + self.unrated 
            return self.jpg 

    os.chdir(dirName)
    Folder = os.listdir()
    Folder.sort(key=lambda s: tuple(int(n) for n in s.split('-')))

    for subFolder in Folder:

        subFolder = DataTable()

        os.chdir(f"{dirName}\{subFolder}")

        # change directory into A, B, C folder
        for itemInSubfolder in os.listdir():
            # skip counting invoice.jpg
            if itemInSubfolder == subFolder + ".jpg": continue
            # count 1 NEF file
            if (itemInSubfolder.lower().endswith('.nef')):
                subFolder.NEF += 1
            if (os.path.isdir(itemInSubfolder)):
                os.chdir(f"{dirName}\{subFolder}\{itemInSubfolder}")
                
                # count 1 result
                for subResult in os.listdir():
                    if subResult.startswith(subFolder) and subResult.lower().endswith('.jpg') and len(subResult) == (len(subFolder) + 9):
                        if itemInSubfolder == 'A':
                            subFolder.A += 1
                        if itemInSubfolder == 'B':
                            subFolder.B += 1
                        if itemInSubfolder == 'Charley':
                            subFolder.C += 1
                    else: continue

                os.chdir(f"{dirName}\{subFolder}")

            # count 1 unrated photo
            if itemInSubfolder.startswith(subFolder) and itemInSubfolder.lower().endswith('.jpg') and len(itemInSubfolder) == (len(subFolder) + 9):
                subFolder.unrated += 1

        os.chdir(f"{dirName}")






    



            

            


