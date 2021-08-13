import os

# nt => "windows" || posix => "linux" 
def get_path_mode_on_so():
    character = ''
    so_name = os.name 
    if so_name == "nt":
        character = '\\'
    elif so_name == "posix":
        character = '/'
    return character