import os

def rename_files():
    # get file names from a folder
    os.chdir(r"./prank");
    file_list = os.listdir(r".");
    #print(file_list)

    # for each file, rename filename
    for file_name in file_list:
        print("Old name: " + file_name)
        print("New name: " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))

rename_files()
