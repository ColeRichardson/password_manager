import socket
import time



class Connection:

	def __init__(self, host: str, port: int):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.host = host
		self.port = port
		self.connect()

	def connect(self):
		self.sock.connect((self.host, self.port))

	def register(self, email: str, passwd: str):
		cmd = bytes('register', encoding='utf-8')
		self.sock.send(cmd)
		time.sleep(0.05)
		self.sock.send(bytes(email, encoding='utf-8'))
		time.sleep(0.05)
		self.sock.send(bytes(passwd, encoding='utf-8'))
		return True 

	def login(self, username: str, passwd: str):
		cmd = bytes('login', encoding='utf-8')
		self.sock.send(cmd)
		time.sleep(0.05)
		self.sock.send(bytes(username, encoding='utf-8'))
		time.sleep(0.05)
		self.sock.send(bytes(passwd, encoding='utf-8'))
		return True
