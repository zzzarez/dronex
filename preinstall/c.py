import socket

#global client_socket
def SendXYZ(x,y,z):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '192.168.1.75'  # Адрес сервера
    port = 12345  # Порт сервера
    client_socket.connect((host, port))
    message = str(x) + ' ' + str(y) + ' ' + str(z)
    client_socket.sendall(message.encode())
    # Получение подтверждения от сервера
    #data = client_socket.recv(1024)
    #print("Сервер ответил: {data.decode()}")
    client_socket.close()

def main():
    SendXYZ(1,2,3)
    SendXYZ(11, 21, 33)

if __name__ == "__main__":
    main()