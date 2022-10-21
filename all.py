import os
import sys
import shutil

def rename(dirName):

    os.chdir(dirName)

    for fileFolder in os.listdir():
        os.chdir(f"{dirName}\{fileFolder}")

        # rename file
        for file in os.listdir():
                # validation
                if (os.path.isdir(file)): continue

                if (file.lower().endswith('.nef') == False): 
                    os.remove(file)
                    continue
                
                # rename processing
                src=file
                dst=fileFolder+ '-' + src[-8:]
                os.rename(src, dst)
            
def removeNEF(dirName):

    os.chdir(dirName)

    for fileFolder in os.listdir():
        os.chdir(f"{dirName}\{fileFolder}")
	
        try:
            
            # remove NEF
            for file in os.listdir():
                # validation
                if (os.path.isdir(file)): continue
                if (file.lower().endswith('.nef') or file.lower().endswith('.dng')): 
                    os.remove(file)
                    continue
            
        except OSError as error:
            print (f'{error}')

def rm_lightExp(dirName):

    os.chdir(dirName)

    for fileFolder in os.listdir():
        os.chdir(f"{dirName}\{fileFolder}")

        try:
            shutil.rmtree('light.exp')
        except OSError as error:
            print (f'{error}')

def mkDirABC(dirName):

    os.chdir(dirName)

    for fileFolder in os.listdir():
        os.chdir(f"{dirName}\{fileFolder}")

        try:

            newFolder_list = ['A', 'B', 'Charley']
            for newFolder in newFolder_list:
                os.mkdir(f"{os.getcwd()}\{newFolder}")
        
        except OSError as error:
            print (f'{error}')

def countABC(dirName):

    os.chdir(dirName)

    Folder = os.listdir()
    Folder.sort(key=lambda s: tuple(int(n) for n in s.split('-')))

    subFolder_list = []
    ABC_result = []             # [[A, B, C], [A, B, C], ...]
    sum_jpg = []                # total jpg in each subFolder
    num_nef_list = []            # total nef in each subFolder

    for subFolder in Folder:
        os.chdir(f"{dirName}\{subFolder}")

        subFolder_list.append(subFolder)

        totalNEF = 0        # total .NEF in a subFolder
        totalJPG = []       # totalJPG = jpg_folderA + jpg_folderB + C + ... in a subFolder
        JPG = 0             # jpg in subFolder before moved

        for file in os.listdir():

            if (os.path.isdir(file) == True):
                os.chdir(f"{dirName}\{subFolder}\{file}")

                num_jpg = 0     # jpg in folderA or folderB or C

                for jpg in os.listdir():
                    if (jpg.lower().endswith('ok.jpg')): continue
                    elif (jpg.lower().endswith('.jpg') and (len(jpg) > 18) == True):
                        num_jpg +=1
                    else: continue

                totalJPG.append(num_jpg)
                os.chdir(f"{dirName}\{subFolder}")


            elif (file.lower().endswith('.nef') == True):
                totalNEF += 1

            elif (file.lower().endswith('.jpg') and (len(file) > 18) == True):
                JPG += 1

            else: continue

        ABC_result.append(totalJPG)
        sum_jpg.append(sum(totalJPG))
        num_nef_list.append(totalNEF)

        print(f"\n{subFolder} has JPEG files uploaded [{(sum(totalJPG) or JPG)}/{totalNEF}].")

        os.chdir(dirName)

    # --- A SUMMARY TABLE --- #
    print(f'\nThere are {sum(num_nef_list)} images in {len(Folder)} folders in "{os.getcwd()}".')
    print(f"\n-------------------------------------------")
    print(f"\nSubfolder     -- [A, B, C] -- JPG/NEF\n")

    for subfolder, result, NEF in zip(subFolder_list, ABC_result, num_nef_list):
        print(f"{subfolder} -- {result} -- {sum(result)}/{NEF}")

    A = []
    B = []
    C = []

    for row in ABC_result:
        if len(row) == 3:
            A.append(row[0])
            B.append(row[1])
            C.append(row[2])
        elif len(row) == 2:
            A.append(row[0])
            B.append(row[1])
            C.append(0)

    print(f"\n{len(Folder)} subfolders    [{sum(A)}, {sum(B)}, {sum(C)}] -- {sum(sum_jpg)}/{sum(num_nef_list)}")

    # --- FOR COPYING PART --- #
    print(f"\n------------------------------------------- \n")
    print(f"\nFor Copy 'Folder'")       # copy subFolder name
    for f in Folder:
        print(f)

    print(f"\nFor Copy 'A'")            # copy A result
    for a in ABC_result:
        print(a[0])

    print(f"\nFor Copy 'B'")            # copy B result
    for b in ABC_result:
        print(b[1])

# LET'S CALL THE FUNCTIONS

# rename()
# removeNEF()
# rm_lightExp()
# mkDirABC()
# countABC(r"C:\Users\sivla\Dropbox\Cambodia\2021\11月\11-29")
