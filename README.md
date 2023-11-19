# BullyingUserBot

Бот автоматически проставляет clown-reaction под всеми сообщениями юзеров, прописанных в переменной `USERS`, во всех общих чатаx.

Дополнительно добавлено: 
* Функция slow-печати командой `.s текст сообщения`.
* Автоматическая чистка своих сообщений в чате командой `.clear`
   * Просто "рай" для админов, в логах у которых будет куча удаленных сообщений.  
* Функция спама реакцией под всеми сообщениями, выбранного юзера, реплай-командой `.react смайлик-эмодзи`


## Инструкция:
Склонируйте репозиторий на свой локальный компьютер.

`git clone https://github.com/3JloDey/BullyingUserBot.git`

Установите зависимости используя команду.

`pip install -r requirements.txt`

Переименуйте файл `.env_template` в .`env` и заполните его по шаблону внутри. Все нужное вы найдете 
[здесь](https://core.telegram.org/api/obtaining_api_id).

Запустите файл `main.py`.

### PS Просьба не удалять двух дурачков прописанных по умолчанию :)
### PSS Реакцию можно изменить, отредактировав хендлер