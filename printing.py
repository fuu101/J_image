# count how many files there are in folderA, B, C and Charley

import os

def ABC_result_of(dirName):
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

        totalNEF = 0                # total .NEF in a subFolder
        sub_ABC_result = []         # [A, B, C] in a subFolder
        JPG = 0                     # jpg in subFolder before moved

        # change directory into A, B, C folder
        for file in os.listdir():
            # skip counting invoice
            if file == subFolder + ".jpg": continue
            # count 1 NEF file
            if (file.lower().endswith('.nef')):
                totalNEF += 1
            if (os.path.isdir(file)):
                os.chdir(f"{dirName}\{subFolder}\{file}")

                # uploaded photos in a
                num_jpg = 0    
                
                # count 1 result
                for jpg in os.listdir():
                    if jpg.startswith(subFolder) and jpg.lower().endswith('.jpg') and len(jpg) == (len(subFolder) + 9):
                        num_jpg += 1
                    else: continue

                    # if (jpg.lower().endswith('ok.jpg')): continue
                    # elif (jpg.lower().endswith('.jpg') and (len(jpg) > 18)):
                    #     num_jpg +=1
                    # else: continue

                sub_ABC_result.append(num_jpg)
                os.chdir(f"{dirName}\{subFolder}")

            # count 1 uploaded photo
            if file.startswith(subFolder) and file.lower().endswith('.jpg') and len(file) == (len(subFolder) + 9):
                JPG += 1
                
            else: continue

        ABC_result.append(sub_ABC_result)
        sum_jpg.append(sum(sub_ABC_result))
        num_nef_list.append(totalNEF)

        print(f"\n{subFolder} has JPEG files uploaded [{(sum(sub_ABC_result) or JPG)}/{totalNEF}].")

        os.chdir(dirName)

    # --- A SUMMARY TABLE --- #
    print(f'\nThere are {sum(num_nef_list)} images in {len(Folder)} folders in "{os.getcwd()}".')
    print(f"\n-------------------------------------")
    print(f"\nSubfolder     -- [A, B, C] -- JPG/NEF\n")

    for subfolder, result, NEF in zip(subFolder_list, ABC_result, num_nef_list):
        print(f"{subfolder} -- {result} -- {sum(result)}/{NEF}")

    A, B, C = [], [], []

    for row in ABC_result:
        if len(row) == 3:
            A.append(row[0])
            B.append(row[1])
            C.append(row[2])
        elif len(row) == 2:
            A.append(row[0])
            B.append(row[1])
            C.append(0)
        elif len(row) == 0:
            for i in (A, B, C):
                i.append(0)

    print(f"\n{len(Folder)} subfolders    [{sum(A)}, {sum(B)}, {sum(C)}] -- {sum(sum_jpg)}/{sum(num_nef_list)}")

    # --- FOR COPYING PART --- #
    print(f"\n-------------------------------------\n")
    print(f"\nFor Copy 'Folder'")       # copy subFolder name
    for f in Folder:
        print(f)
    print(f"\nFor Copy 'A'")            # copy A result
    for a in A:
        print(a)
    print(f"\nFor Copy 'B'")            # copy B result
    for b in B:
        print(b)





    



            

            


