import os


def delete_content(folderpath):
    if not os.path.exists(folderpath):
        print("There is no such folder: " + folderpath)
        return False

    for itemname in os.listdir(folderpath):
        itempath = os.path.join(folderpath, itemname)
        if os.path.isfile(itempath):
            with open(itempath, "w") as f:
                pass
        elif os.path.isdir(itempath):
            delete_content(itempath)    
    
    return True


if __name__ == "__main__":
    current_dir = os.getcwd()
    print("Current directory: " + current_dir)
    folder_name = input("Write folder to clear:  ")
    folder_to_clear = os.path.join(current_dir, folder_name)
    print("Folder to clear: " + folder_to_clear)
    
    if delete_content(folder_to_clear):
        print(f"Folder: {folder_to_clear} cleared")
