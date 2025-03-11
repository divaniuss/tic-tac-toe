import socket
from tictactoe_logic import Field


class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.IsWho = 0
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.ip, self.port))
        self.server.listen(2)
        self.conn1, addr1 = self.server.accept()
        self.conn1.send("1".encode()) # 2 - o 1 - x распределям ході
        print("Подлючено 1...")
        self.conn2, addr2 = self.server.accept()
        self.conn2.send("2".encode())
        print("Подлючено 2...")


    def request_first(self):

        request1 = self.conn1.recv(1024).decode()

        if request1.count(' ') < 2:
            print(f"Ошибка: получено некорректное сообщение 1 : {request1}")
            self.conn1.send("Неверный символ".encode())
            print("тех penis")
            return False


        raw, col, symbol = request1.split(' ', 2)
        raw, col = int(raw), int(col)

        if not field.step(raw, col, symbol):
            self.conn1.send("Эта клетка занята".encode())
            return False
        elif field.CheckIsPeremoga():
            self.conn1.send("win".encode())
            self.conn2.send("defeat".encode())
            print("penis peremoga 1")
            return True
        elif field.IsTie():
            self.conn1.send("tie".encode())
            print("penis tie 1")
            return True
        else:
            res = "Принято 1:\n\n" + field.OutField()
            self.conn2.send(res.encode())     # отправляем 2
            self.conn1.send(res.encode())
            return False



    def request_second(self):

        request2 = self.conn2.recv(1024).decode()

        if request2.count(' ') < 2:
            print(f"Ошибка: получено некорректное сообщение 2 : {request2}")
            self.conn2.send("Неверный символ".encode())
            print("тех penis")
            return False

        raw, col, symbol = request2.split(' ', 2)
        raw, col = int(raw), int(col)

        if not field.step(raw, col, symbol):
            self.conn2.send("Эта клетка занята".encode())
            return False
        elif field.CheckIsPeremoga():
            self.conn2.send("win".encode())
            self.conn1.send("defeat".encode())
            print("penis peremoga 2")
            return True
        elif field.IsTie():
            self.conn2.send("tie".encode())
            print("penis tie 2")
            return True
        else:
            res = "Принято 2:\n\n" + field.OutField()
            self.conn1.send(res.encode())
            self.conn2.send(res.encode())
            return False




field = Field()
serv = Server('127.0.0.1', 4000)
# serv.start()



# 0 - first , 1 - second

IsWho = 0
while (not serv.request_first() and not serv.request_second()):
    if IsWho == 0:
        print("first")
        serv.request_first()
        IsWho = 1
    if IsWho == 1:
        print("second")
        serv.request_second()
        IsWho = 0
    pass
    print("\n")

serv.conn1.close()
serv.conn2.close()
serv.server.close()

# field.step(0, 1, "х")