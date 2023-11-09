import os

def val_existing_file(path: str):
    """
    Function to validate if a file exists in a directory.

    Args:
        path (str): File path to valid existence.

    Returns:
        (bool, str):    tuple with the boolean value if the file exists
                        or not and the file name
    """

    file_name = None
    exists = os.path.isfile(path)
    
    if exists:
        file_name = os.path.basename(path)
        file_name = file_name.replace(' ', '_')
        
    return exists, file_name