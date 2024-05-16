import socket

def GetCords(cords):
    print(cords[0])
    print(cords[1])
    print(cords[2])
def main():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    host = '192.168.1.75'
    port = 12345
    server_socket.bind((host, port))
    while True:
        # Начало прослушивания входящих соединений
        server_socket.listen(1)
        #print(f"Сервер запущен и прослушивает на {host}:{port}")
        # Принятие входящего соединения
        connection, client_address = server_socket.accept()

        try:
            while True:
                data = connection.recv(1024)
                if data:
                    numbers = list(map(int, data.decode().split()))
                    #print(f"Получены числа: {numbers}")
                    GetCords(numbers)
                    #connection.sendall(b"all send")
                else:
                    #Если данные не получены, закрываем соединение
                    #print("break")
                    break
        finally:
            #print("con close")
            #Закрытие соединения и сокета
            connection.close()

    server_socket.close()

if __name__ == "__main__":
    main()