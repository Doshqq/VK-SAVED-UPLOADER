"""
Подробнее в README.md
"""

import webbrowser

def get_vk_token(app_id):
    url = (f"https://oauth.vk.com/authorize?client_id={app_id}&scope=photos,offline&"
           "redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token")
    print("Откройте следующую ссылку в браузере и скопируйте токен из адресной строки:")
    print(url)
    webbrowser.open(url)

if __name__ == "__main__":
    app_id = input("Введите ID вашего приложения VK: ")
    get_vk_token(app_id)