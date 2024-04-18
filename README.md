# meridicord
Rich Presence для Meridius на Linux

![](https://habrastorage.org/webt/ut/iu/bd/utiubdcfwf4c8n9d7j48nfe529e.jpeg)

## Зависимости

- Python
- pypresence

## Установка

- Включите "Режим стримера" в Настройки->Основные

*(Совет если вы установили плеер из flatpak: Необходимо дать доступ к директории пользователя, сделать это можно через `flatpak override io.github.purplehorrorrus.Meridius --filesystem=/home/user`)*

- Укажите путь до вашей папки в переменной `path`

- Запустите приложение командой `python meridius_rpc.py`
