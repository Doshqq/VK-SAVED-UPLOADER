import sys
import time
from vk_api import VkUpload
from vk_api import VkApi


class SaveVKPhoto:
    """
    A class to handle uploading and saving photos to a VK profile.

    Parameters
    ----------
    token : str
        The VK API access token.
    owner_id : str
        The ID of the VK profile where photos will be saved.
    files : str | list | tuple
        Path(s) to the photo(s) to upload.
    exec : bool


    Attributes
    ----------
    photos : list
        A list of opened file objects for the provided photo files.
    filenames : str | list
        Original file paths provided during initialization.
    vk : vk_api.VkApi.method
        VK API session object.

    Methods
    -------
    upload_on_server()
        Uploads the photo(s) to the VK API server.
    save_photo()
        Saves the uploaded photo(s) to the VK profile.
    """
    def __init__(self, token, owner_id, files: str | list | tuple, exec: bool = True):
        self.owner_id = owner_id
        self.filenames = files
        if isinstance(files, str):
            try:
                photos = [open(resource_path(files), 'rb')]
            except Exception as e:
                raise ValueError(f"--- ERROR WITH OPENING FILE: {e} ---")
            
        elif isinstance(files, list):
            photos = []
            for i in range(len(files)):
                try:
                    photos.append(open(resource_path(files[i]), 'rb'))
                except Exception as e:
                    print(f"--- ERROR WITH OPENING FILE: {e}\nSKIPPING... ---")
        else:
            raise ValueError("--- INVALID INPUT TYPE FOR FILES ---")
        
        if not photos:
            raise ValueError("--- NO VALID PHOTOS TO UPLOAD ---")
        
        self.photos = photos

        vk_session = VkApi(token=token)
        self.vk = vk_session.get_api()
        if exec:
            self.save_photo()

    def upload_on_server(self):
        """
        Upload photo(s) on the VK API server.
   
        Returns
        -------
        list
            A list of dictionaries containing uploaded photo information.
        """
        uploader = VkUpload(self.vk)
        return uploader.photo_messages(photos=self.photos)
    
    def _get_attrs(self, photo_data, photo_index):
            """
            Extracting attributes of photo(s) from VK API data structure.

            Parameters
            ----------
            photo_data : list
                List of photos data.
            photo_index : int, optional
                Index of the photo in the data list.

            Returns
            -------
            dict
                A dictionary containing attributes of the single photo.
            """

            if not photo_data:
                return {}
            
            photo = photo_data[photo_index]

            attributes = {
                "album_id": photo.get("album_id"),
                "date": photo.get("date"),
                "id": photo.get("id"),
                "owner_id": photo.get("owner_id"),
                "access_key": photo.get("access_key"),
                "text": photo.get("text"),
                "web_view_token": photo.get("web_view_token"),
            }

            sizes = photo.get("sizes", [])
            if sizes:
                attributes["sizes"] = [{
                    "type": size.get("type"),
                    "url": size.get("url"),
                    "width": size.get("width"),
                    "height": size.get("height")
                } for size in sizes]

            orig_photo = photo.get("orig_photo")
            if orig_photo:
                attributes["orig_photo"] = {
                    "url": orig_photo.get("url"),
                    "width": orig_photo.get("width"),
                    "height": orig_photo.get("height")
                }

            return attributes
    
    def save_photo(self):
        """
        Save the uploaded photo(s) to the VK profile.
        """
        try:
            photo_object = self.upload_on_server()
        except Exception as e:
            print("--- ERROR WITH UPLOADING ON THE VK API SERVER ---", e)
            return
            
        for i, photo in enumerate(self.photos):
            try:
                attrs = self._get_attrs(photo_object, i)
                photo_id = attrs.get("id")
                owner_id = attrs.get("owner_id")
                access_key = attrs.get("access_key")

                if photo_id and owner_id:
                    self.vk.photos.copy(owner_id=owner_id, photo_id=photo_id, access_key=access_key)
                    print(f"[PHOTO {self.filenames[i]} SUCCESSFULLY SAVED]")
                else:
                    print(f"--- MISSING ATTRIBUTES FOR PHOTO {self.filenames[i]} ---")

                time.sleep(0.2)  # Throttle requests
            except Exception as e:
                print(f"--- ERROR SAVING PHOTO {self.filenames[i]}: {e} ---")

        print(f"{'+' + 60 * '-' + '+'}\n| {'Photo(s) are succesfully saved in your VK profile!'.center(58)} |\n{'+' + 60 * '-' + '+'}\n")


def resource_path(relative_path: str = ""):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path).replace("_internal/", "")

def find_photos():
    base_path = resource_path()
    valid_extensions = (".jpg", ".jpeg", ".png", ".heic")
    return sorted(
        [file for file in os.listdir(base_path) if file.lower().endswith(valid_extensions)],
        key=lambda f: os.path.getmtime(os.path.join(base_path, f)),
        reverse=True
    )[:5]




if __name__ == "__main__":
    try:
        import os
        from dotenv import load_dotenv

        current_dir = resource_path()
        dotenv_path = os.path.join(current_dir, "config.env")

        load_dotenv(dotenv_path=dotenv_path)
        TOKEN = os.getenv("TOKEN")
        OWNER_ID = os.getenv("OWNER_ID")

        if not os.path.isfile(dotenv_path):
            raise FileNotFoundError(f"Config file 'config.env' not found at {dotenv_path}")

        if not TOKEN or not OWNER_ID:
            raise ValueError("Variables TOKEN or OWNER_ID does not found in config.env")

    except Exception as e:
        print(str(e))

        TOKEN = input(f"\nPaste your VK token: ")
        OWNER_ID = input(f"\nPaste your VK account ID: ")

    finally:
        photo_files = find_photos()

        if photo_files:
            print("\nFound the following photos in the current directory (max=5):")
            for i, file in enumerate(photo_files, 1):
                print(f"{i}. {file}")

            choice = None
            while choice != 'y' and choice != 'n':
                choice = input("Would you like to use these files? (Y/N): ").strip().lower()
            if choice == "y":
                files = photo_files
            else:
                files = input("Enter path(s) to your photo(s) (comma-separated): ").strip().split(",")
                files = [file.strip() for file in files]
        else:
            print("\nNo valid photo files found in the current directory")
            files = input("Enter path(s) to your photo(s) (comma-separated): ").strip().split(",")        
            files = [file.strip() for file in files]

        print('\n--- Processing, please wait... ---\n')
        try:
            SaveVKPhoto(token=TOKEN, owner_id=OWNER_ID, files=files)
        except ValueError as e:
            print(e)
            