from pypresence import Presence
from pypresence.exceptions import DiscordError, DiscordNotFound 
import os, time

app_id = "1230571019786518608"
path = "/home/li0ard/streamer"

print("Meridicord by li0ard")
print("Путь до папки: " + path)

RPC = Presence(app_id)
RPC.connect()

print("Начинаем трансляцию RPC")

try:
	while True:
		f1 = open(os.path.join(path, "title.txt"), "r")
		f2 = open(os.path.join(path, "performer.txt"), "r")
		title = f1.read()
		author = f2.read()
		f1.close()
		f2.close()
		RPC.update(details=title, state="by " + author, large_image="logo", large_text="Meridius")
		time.sleep(3)
except DiscordError:
	print("Произошла ошибка Discord")
except DiscordNotFound:
	print("Discord не найден")