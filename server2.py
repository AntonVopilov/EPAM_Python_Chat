import socket, time


# current ip
host = socket.gethostbyname(socket.gethostname())
# use 9090 port, http://ru.adminsub.net/tcp-udp-port-finder/9090
print('host', host)
port = 9090

# лист активных пользователей
clients = []

# socket.AF_INET - tcp/ soket.SOCK_DGRAM - ip
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

quit = False
print('Серевер запущен')

while not quit:
    try:
        # data - сообщение отправленное пользоветелем
        # addr - адрес пользователя
        data, addr = s.recvfrom(1024)

        if addr not in clients:
            clients.append(addr)

        # текущее время
        itsatime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())

        print(f'[{addr[0]}] [{addr[1]}] [{itsatime}]')
        print(data.decode("utf-8"))

        # отправляем сообщение другим пользователям
        for client in clients:
            if addr != client:
                s.sendto(data, client)
    except:
        print('\n Сервер остановлен')
        quit = True

s.close()