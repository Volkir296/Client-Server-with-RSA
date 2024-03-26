from socket import * 

class TcpClient:
    def __init__(self, ip, port):                       #Конструктор для принятия IP и порта, а также для создания сокета(server) МБ ПРИМЕМ ОТКРЫТЫЙ ЗАКРЫТЫЙ КЛЮЧ
        self.ip = ip                                    # IPv4
        self.port = port                                # Порт
        self.client = socket(AF_INET, SOCK_STREAM)      # IPv4 и TCP-сокет

    def start(self):
        self.client.connect((self.ip,self.port))        # Подключаемся к серверу
        print("Подключение выполнено")
    

    def stop(self):
        self.client.close()
        print("Клиент выключен!")


ip = "127.0.0.1" 
port = 8005

c = TcpClient(ip,port)
c.start()

'''
HOST = "127.0.0.1"          # Объявление адреса сервера. Данный аддрес = localhost
PORT = 8005                 # Объявление порта подключения

client = socket(AF_INET, SOCK_STREAM)

client.connect((HOST,PORT))

data = client.recv(1024)
msg = data.decode('utf-8')

print(f'Server MSG:\n\t{msg}')

input('END')
'''