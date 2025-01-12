import webbrowser
from tools import extract_token_and_owner_id, save_to_config


APP_ID = '51709693'                                 # 'VK Saved Photo Uploader' Standalone application
REDIRECT_URI = 'https://oauth.vk.com/blank.html'
SCOPE = 'photos,offline'                            # REMOVE OFFLINE IF YOU WANT A LIMITED TIME TOKEN

AUTH_URL = (
    f"https://oauth.vk.com/authorize?"
    f"client_id={APP_ID}&display=page&redirect_uri={REDIRECT_URI}"
    f"&scope={SCOPE}&response_type=token&v=5.131"
)


def init_token():
    # Далее откроется в браузере страница авторизации и разрешению доступа к фото
    webbrowser.open(AUTH_URL)

    success = False
    while not success:
        url = input("Скопируйте полную ссылку с токеном (пример: https://oauth.vk.com/blank.html#access_token=TOKEN&expires_in=0&user_id=OWNER_ID): ")
        
        access_token, owner_id = extract_token_and_owner_id(url)
        
        if access_token and owner_id:
            save_to_config(access_token, owner_id)

        #     print(f"\nВаш Токен: {access_token}")
        #     print(f"Ваш ID страницы: {owner_id}")
            
            # choose = None
            # while choose != 'y' and choose != 'n':
            #     choose = input("\nСохранить в config.env? (Y/N): ").strip().lower()
                
            # if choose == 'y':
            #     save_to_config(access_token, owner_id)
            # else:
            #     print("\nВставьте свои данные в терминал для сохранения фото")

            success = True
            return access_token, owner_id
        else:
            print("\nНе удалось извлечь данные из ссылки. Пожалуйста, убедитесь, что ссылка корректна.\n")
