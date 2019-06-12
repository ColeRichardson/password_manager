import socket



class Connection:

	def __init__(self, host: str, port: int):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.host = host
		self.port = port
		self.connect()

	def connect(self):
		self.sock.connect((self.host, self.port))

	def Register(self, data):
		self.sock.sendall(bytes(data, encoding='utf-8'))
