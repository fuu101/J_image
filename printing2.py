import os

# count how many files there are in folderA, B, C and Charley
def result(date_folder):
    os.chdir(date_folder)
    Folder = os.listdir()
    Folder.sort(key=lambda s: tuple(int(n) for n in s.split('-')))

    OList = [0, 0, 0, 0, 0, 0,]     # [(0)image_folder, (1)A, (2)B, (3)C, (4)unrated, (5)NEF]
    data_table = []

    for image_folder in Folder:

        data_table.append(OList[:])
        data_table[-1][0] = image_folder
        os.chdir(f"{date_folder}\{image_folder}")

        for item_in_imagefolder in os.listdir():
            # count 1 NEF file
            if (item_in_imagefolder.lower().endswith('.nef')):
                data_table[-1][5] += 1

            elif (os.path.isdir(item_in_imagefolder)):
                os.chdir(f"{date_folder}\{image_folder}\{item_in_imagefolder}")
                
                # count 1 result
                for evaluated_image in os.listdir():
                    # validate evaluated_image
                    if evaluated_image.startswith(image_folder) and evaluated_image.lower().endswith('.jpg') and (len(evaluated_image.replace(" ", "")) == (len(image_folder) + 9)):
                        if item_in_imagefolder == 'A':
                            data_table[-1][1] += 1
                        elif item_in_imagefolder == 'B':
                            data_table[-1][2] += 1
                        elif item_in_imagefolder == 'Charley':
                            data_table[-1][3] += 1
                    else: continue

                os.chdir(f"{date_folder}\{image_folder}")

            # count 1 uploaded photo
            elif item_in_imagefolder.startswith(image_folder) and item_in_imagefolder.lower().endswith('.jpg') and (len(item_in_imagefolder.replace(" ", "")) == (len(image_folder) + 9)):
                data_table[-1][4] += 1
            else: continue 

        os.chdir(f"{date_folder}")

    # derive lists from data_table
    subfolder_id_list = [one_subfolder[0] for one_subfolder in data_table]
    A_list = [one_subfolder[1] for one_subfolder in data_table]
    B_list = [one_subfolder[2] for one_subfolder in data_table]
    C_list = [one_subfolder[3] for one_subfolder in data_table]
    jpg_list = [one_subfolder[1:5] for one_subfolder in data_table]
    unrated_list = [one_subfolder[4] for one_subfolder in data_table]
    nef_list = [one_subfolder[5] for one_subfolder in data_table]

    # -- SUMMARY TABLE -- #
    print("--------------")
    print(f"SUMMARY TABLE\n{date_folder}")
    print("--------------")
    # print header
    print("Subfolder    -- [A, B, C] unrated -- jpg/nef\n")
    # print A, B, C result
    for one_subfolder in data_table:
        print(f"{one_subfolder[0]} -- {one_subfolder[1:4]} {one_subfolder[4]} -- {sum(one_subfolder[1:5])}/{one_subfolder[-1]}")
    # print total
    print(f"\n{len(subfolder_id_list)} subfolders   -- [{sum(A_list)}, {sum(B_list)}, {sum(C_list)}] {sum(unrated_list)} -- {sum(sum(jpg_list, []))}/{sum(nef_list)}")
    print("------------------------------------------")

    # -- FOR COPYING -- #
    # copy subfolder
    print('copy subfolder\n')
    for subfolder_id in subfolder_id_list:
        print(subfolder_id)
    # copy A
    print('\ncopy A\n')
    for A in A_list:
        print(A)
    # copy B
    print('\ncopy B\n')
    for B in B_list:
        print(B)
    print('\n----------')







    



            

            



