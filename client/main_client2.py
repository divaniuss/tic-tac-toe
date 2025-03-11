import socket

class Client2:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.ip, self.port))
        self.x_or_o = ''  # 1 - x 2 - o

    def send_message(self):
        message = self.create_message()
        if message is not None:
            self.client.send(message.encode())
        else:
            print("Сообщение не отправлено, повторите ввод.")
            print("Техническое поражение")
            self.client.close()


    def create_message(self):
        while True:
            raw = -1
            col = -1
            while not (0 <= raw <= 2):
                raw = int(input("Введите рядок (0-2): "))
            while not (0 <= col <= 2):
                col = int(input("Введите колонку (0-2): "))
            if self.x_or_o == "1":
                symbol = input("Введите ваш символ ('X' или любой другой символ для пересмены хода): ").lower()
                if symbol in "x":
                    return f"{raw} {col} {symbol}"
            elif self.x_or_o == "2":
                symbol = input("Введите ваш символ ('O' или любой другой символ для пересмены хода): ").lower()
                if symbol in "o":
                    return f"{raw} {col} {symbol}"
            else:
                print("Ошибка! Введите X или O.")

    def catch_recv(self):

        response = self.client.recv(1024).decode()
        print(f"\nОтвет сервера: {response}")
        if response == "win":
            print("Победа Клиента2")
            return True
        elif response == "tie":
            print("Ничья")
            return True
        elif response == "defeat":
            print("Поражение Клиента2")
            return True

    def whosFirst(self):
        self.x_or_o = self.client.recv(1024).decode()
        return self.x_or_o


c2 = Client2('127.0.0.1', 4000)

Your_move = c2.whosFirst()
while True:
    if Your_move == "1":
        print("Ход Клиента1:")
        c2.send_message()
        if c2.catch_recv():
            break
        Your_move = "2"
    if Your_move == "2":
        print("Ожидайте пока Клиент1 сделает свой ход")
        if c2.catch_recv():
            break
        Your_move = "1"
c2.client.close()
