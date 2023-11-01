import os

ROOT_FOLDER= "/Users/jeffry/Downloads"
BASE_FOLDERS= ["/pdf", "/img", "/xls", "/ppt", "/doc" , "/zip" ,"/mov"]
BASE_FOLDERS_DICT= {
    'pdf': ['.pdf'],
    'img': ['.jpg', '.jpeg', '.png', '.gif', '.bmp','.tiff' ,'.svg'],
    'xls': ['.xls', '.xlsx', '.xlsm' ,'.xlsb','.csv'],
    'ppt': ['.ppt', '.pptx','.pps','.ppsx','.pptm','.key'],
    'doc': ['value5', 'value6'],
    'zip': ['value5', 'value6'],
    'mov': ['value5', 'value6'],

    
}

IGNORE_FOLDERS= ["$RECYCLE.BIN"]

def scan_files(root_dir) -> list[str]:
    file_list = []
    for root, dirs, files in os.walk(root_dir):
        if dirs in IGNORE_FOLDERS:
            continue
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path+file)
    return file_list

def create_base_folders(root_dir):
    for dir in BASE_FOLDERS:
        try:
            os.mkdir(root_dir + dir)
        except (FileExistsError):
            pass
        
def move_files(root_dir, base_folders, file_list):
    pass
        
file_list = scan_files(ROOT_FOLDER)
create_base_folders(ROOT_FOLDER)
print(file_list)
