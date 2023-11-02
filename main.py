import os
import shutil
from datetime import datetime, timedelta

BASE_FOLDERS = {
    "pdf": [".pdf"],
    "img": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"],
    "xls": [".xls", ".xlsx", ".xlsm", ".xlsb", ".csv"],
    "ppt": [".ppt", ".pptx", ".pps", ".ppsx", ".pptm", ".key"],
    "doc": [".doc", ".docx", ".docm", ".rtf"],
    "zip": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
    "mov": [
        ".mp4",
        ".avi",
        ".mkv",
        ".mov",
        ".wmv",
        ".flv",
        ".m4v",
        ".mpg",
        ".mpeg",
        ".rm",
        ".vob",
        ".webm",
        ".3gp",
    ],
    "others": [],
}

def get_downloads_path():
    """Returns the path to the Downloads folder for the current user."""
    if os.name == "nt":
        # Windows
        return os.path.join(os.environ["USERPROFILE"], "Downloads")
    else:
        # macOS and Linux
        return os.path.join(os.path.expanduser("~"), "Downloads")


DOWNLOAD_FOLDER = get_downloads_path()


def get_full_extension(filename):
    # Split the extension from the path and normalise it to lowercase.
    root, ext1 = os.path.splitext(filename)

    # Check if the part before the extension also ends with a known double extension
    double_extensions = [".tar", ".tar", ".user"]
    for double_ext in double_extensions:
        if root.lower().endswith(double_ext):
            ext2 = double_ext
            return (ext2 + ext1).lower()

    return ext1.lower()


def scan_files(root_dir) -> list[dict]:
    file_list = []
    one_day_ago = datetime.now() - timedelta(days=1)
    with os.scandir(root_dir) as entries:
        for entry in entries:
            if entry.is_file():  # Check if it's a file
                file_mod_time = datetime.fromtimestamp(entry.stat().st_mtime)
                if file_mod_time < one_day_ago:
                    file_path = entry.path
                    root, ext = os.path.splitext(entry.name)
                    file_dict = {
                        "name": entry.name,
                        "path": file_path,
                        "extension": ext.lower(),
                    }
                    file_list.append(file_dict)
    return file_list


def create_base_folders(root_dir):
    for key in BASE_FOLDERS:
        try:
            os.mkdir(root_dir + "/" + key)
        except FileExistsError:
            pass


def move_file(root_dir, base_folders, file):
    for key, values in BASE_FOLDERS.items():
        if file["extension"] in values:
            break
    print(file["extension"])
    src = file["path"]
    print(src)
    dst = f"{root_dir}/{key}/{file["name"]}"
    print(dst)
    try:
        shutil.move(src, dst)
        print(f"File moved successfully to {dst}")
    except IOError as e:
        print(f"Unable to move file. {e}")


def move_files(root_dir, base_folders, file_list):
    for file in file_list:
        move_file(root_dir, base_folders, file)


file_list = scan_files(DOWNLOAD_FOLDER)
create_base_folders(DOWNLOAD_FOLDER)
move_files(DOWNLOAD_FOLDER, BASE_FOLDERS, file_list)
