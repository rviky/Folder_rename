import os
fileName = "viki" #name_of_the_file
fileExtension = ".jpg" #extension_of_the_file
base_path = 'C:\\path\\to\\your\\file\\directory' #base_folder_path.
folders = [folder for folder in os.listdir(".") if os.path.isdir(folder)]
for subfolder in folders:
    count = 1
    dir_path = '{}\\{}'.format(base_path, subfolder)
    os.chdir(dir_path)
    for file in os.listdir(os.getcwd()):
        oldName= file
        newName = '{}'.format(fileName+str(count)+fileExtension)
        print("Renaming files: {} to {}".format(oldName,newName))
        count+=1
        os.rename(oldName, newName)
print("\n\nRename done.")
        
    