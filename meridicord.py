from pypresence import Presence
from pypresence.exceptions import DiscordError, DiscordNotFound 

app_id = "1230571019786518608"
mode = 2 # 1 - файлы стримера, 2 - WebSocket сервер
path = "/home/li0ard/streamer" # путь к файлам стримера (Обязательно для mode = 1)
ip = "127.0.0.1" # IP WebSocket сервера (Обязательно для mode = 2)
port = "3000" # Порт WebSocket сервера (Обязательно для mode = 2)

print("Meridicord by li0ard")
if mode == 1:
	print("Путь до папки: " + path)
elif mode == 2:
	print("IP: " + ip)
	print("Порт: " + port)

RPC = Presence(app_id)
RPC.connect()

print("Начинаем трансляцию RPC")

if mode == 1:
	import os, time 
	def readFile(path):
		f = open(path, "r")
		content = f.read()
		f.close()
		return content
	try:
		while True:
			title = readFile(os.path.join(path, "title.txt"))
			author = readFile(os.path.join(path, "performer.txt"))
			RPC.update(details=title, state="by " + author, large_image="logo", large_text="Meridius")
			time.sleep(3)
	except DiscordError:
		print("Произошла ошибка Discord")
	except DiscordNotFound:
		print("Discord не найден")
elif mode == 2:
	import websocket, json
	def recvMsg(ws, msg):
		msg = json.loads(msg)
		try:
			album = "Meridius"
			cover = "logo"
			if "album" in msg:
				album = msg["album"]["title"]
				try:
					cover = msg["album"]["thumb"]["photo_600"]
				except:
					pass
			RPC.update(details=msg["title"], state="by " + msg["performer"], large_image=cover, large_text=album)
		except DiscordError:
			print("Произошла ошибка Discord")
		except DiscordNotFound:
			print("Discord не найден")
	ws = websocket.WebSocketApp("ws://{}:{}/socket/player/song".format(ip, port), on_message=recvMsg)
	ws.run_forever(reconnect=5)