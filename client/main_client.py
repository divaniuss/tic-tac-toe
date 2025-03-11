import socket

class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.ip, self.port))
        self.x_or_o = '' # 1 - x 2 - o

    def send_message(self):
        message = self.create_message()
        if message is not None:
            self.client.send(message.encode())
        else:
            print("Сообщение не отправлено, повторите ввод.")
            print("Тех. луз")
            self.client.close()


    def create_message(self):
        while True:
            # raw = input("Введите рядок: ")
            # col = input("Введите колонку: ")
            raw = -1
            col = -1
            while not (0 <= raw <= 2):
                raw = int(input("Введите рядок (0-2): "))
            while not (0 <= col <= 2):
                col = int(input("Введите колонку (0-2): "))
            if self.x_or_o == "1":
                symbol = input("Введите ваш символ (X или любой другой символ для пересмены хода): ").lower()
                if symbol in "x":
                    return f"{raw} {col} {symbol}"
            elif self.x_or_o == "2":
                symbol = input("Введите ваш символ (O или любой другой символ для пересмены хода): ").lower()
                if symbol in "o":
                    return f"{raw} {col} {symbol}"
            else:
                print("Ошибка! Введите X или O.")




    def catch_recv(self):
        response = self.client.recv(1024).decode()
        print(f"Ответ сервера: {response}")
        if response == "win":
            print("peremoga client1")
            return True
        elif response == "tie":
            print("tie")
            return True
        elif response == "defeat":
            print("proebali")
            return True


    def whosFirst(self):
        self.x_or_o = self.client.recv(1024).decode()
        return self.x_or_o


c = Client('127.0.0.1', 4000)

Your_move = c.whosFirst()


# Your_move = ""
# X_or_O = c.whosFirst()
# if X_or_O == "x":
#     print("первый1")
#     Your_move = "1"
# else:
#     Your_move = "2"
#     print("второй1")
#
# print(Your_move)
# if Your_move == "1":
#     c.send_message()
#     Your_move = "2"

while True:
    if Your_move == "1":
        print("hod1")
        c.send_message()
        if c.catch_recv():
            break
        Your_move = "2"

    if Your_move == "2":
        print("wait1 ")
        if c.catch_recv():
            break
        Your_move = "1"

c.client.close()
