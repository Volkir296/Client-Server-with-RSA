from socket import *

class TcpServer:
    def __init__(self, ip, port):                       #Конструктор для принятия IP и порта, а также для создания сокета(server) МБ ПРИМЕМ ОТКРЫТЫЙ ЗАКРЫТЫЙ КЛЮЧ
        self.ip = ip                                    # IPv4
        self.port = port                                # Порт
        self.server = socket(AF_INET, SOCK_STREAM)      # IPv4 и TCP-сокет
        print("Данные получены, сокет создан")

    def start(self):                                    #Чисто для запуска ожидания подключений
        self.server.bind((self.ip, self.port))          # привязка сокета к IP-адресу и порту
        self.server.listen(1)                           # количество входящих соединений в очереди -> единица для красоты, т.к сервер однопоточный
        print("Ожидание входящий соединений")
        self.user, self.addr = self.server.accept()     # принятие входящего соединения
        print(f"Соединение установлено с \n\t{self.addr}")

    def stop(self):                                     #Выключаем сервак 
        self.server.close()                             # закрываю соединение нужен если работаем без with ну и легче привязать к кнопкам и интерфейсу
        print("Сервер выключен!")


ip = "127.0.0.1"
port = 8005 
s = TcpServer(ip,port)
s.start()
s.stop()

'''
HOST = "127.0.0.1"          # Объявление адреса сервера. Данный аддрес = localhost
PORT = 8005                 # Объявление порта подключения

server = socket(AF_INET, SOCK_STREAM)

server.bind((HOST,PORT))

server.listen(2)

user, addr = server.accept()

print(f"CONNECTED: \n\t{user}, \n\t{addr}")

user.send('You are connected!'.encode('utf-8'))

##while True:
'''