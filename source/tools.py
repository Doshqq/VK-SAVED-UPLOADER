import re
import os
import sys


def resource_path(relative_path: str = ""):
    """
    Returns the absolute path of the resource file depended on the launch method.
    """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path).replace("_internal/", "")

def find_photos():
    """
    Finds the last 5 photos sorted by date of change in the current directory.
    
    Returns
    -------
    list
        A list of photo file names.
    """
    base_path = resource_path()
    valid_extensions = (".jpg", ".jpeg", ".png", ".heic")
    return sorted(
        [file for file in os.listdir(base_path) if file.lower().endswith(valid_extensions)],
        key=lambda f: os.path.getmtime(os.path.join(base_path, f)),
        reverse=True
    )[:5]

def extract_token_and_owner_id(url):
    token_pattern = r"access_token=([^&]+)"
    owner_id_pattern = r"user_id=(\d+)"
    
    token_match = re.search(token_pattern, url)
    owner_id_match = re.search(owner_id_pattern, url)
    
    if token_match and owner_id_match:
        access_token = token_match.group(1)
        owner_id = owner_id_match.group(1)
        return access_token, owner_id
    else:
        return None, None

def save_to_config(token, owner_id):
    filename = "config.env"
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        lines = []

    token_found = False
    owner_id_found = False

    with open(filename, "w") as file:
        for line in lines:
            if line.startswith("TOKEN = "):
                file.write(f"TOKEN = {token}\n")
                token_found = True
            elif line.startswith("OWNER_ID = "):
                file.write(f"OWNER_ID = {owner_id}\n")
                owner_id_found = True
            else:
                file.write(line)

        if not token_found:
            file.write(f"TOKEN = {token}\n")
        if not owner_id_found:
            file.write(f"OWNER_ID = {owner_id}\n")

    print("\n--- Данные успешно обновлены в файле config.env. ---")
