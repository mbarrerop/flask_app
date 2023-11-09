import os

def val_existing_file(path: str):
    file_name = None
    exists = os.path.isfile(path)
    
    if exists:
        file_name = os.path.basename(path)
        file_name = file_name.replace(' ', '_')
        
    return exists, file_name