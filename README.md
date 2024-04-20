# meridicord
Rich Presence для Meridius на Linux (и не только)

![](https://habrastorage.org/webt/ut/iu/bd/utiubdcfwf4c8n9d7j48nfe529e.jpeg)

## Зависимости

- Python
- pypresence
- websocket (если вы будете использовать Websocket сервер)

## Режимы работы

- "Файлы" - обновление информации раз в 3 секунды через файлы "Режима стримера"
- "Сервер" - обновление информации при переключении трека через WebSocket сервер

## Установка

- Шаг для Linux: Необходимо дать доступ к директории пользователя, сделать это можно через `flatpak override io.github.purplehorrorrus.Meridius --filesystem=/home/user`

- Выполните шаги по таблице для режима, который вы планируете использовать:

| Режим "Файлы"                                      | Режим "Сервер"                                                                    |
|----------------------------------------------------|-----------------------------------------------------------------------------------|
| ![](https://habrastorage.org/webt/il/ig/zq/iligzqvjrlt0ogr5rxa_2fpzjbo.jpeg) | ![](https://habrastorage.org/webt/zn/cl/ke/znclkeqessj14ne4x45esdo-jfu.jpeg) |
| 1. Включите "Режим стримера" в Настройки->Основные | 1. Нажмите "Запустить сервер" в Настройки->Сервер                                 |
| 2. Укажите путь до вашей папки в переменной `path` | 2. Укажите IP вашего сервера и его порт в переменные `ip` и `port` соответственно |

- Запустите приложение командой `python meridicord.py`
