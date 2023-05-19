import socket
import threading

# Choosing Nickname
nickname = input("adin ne: ")

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('8.tcp.ngrok.io', 19979))
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break
def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()



#Developer:Muter
#Discord:https://discord.gg/WRWEk6jKG7


#Bu kod, bir basit sohbet uygulamasının istemci tarafını temsil etmektedir. İstemci, sunucuya bağlanır, kullanıcıların mesajlarını alır ve gönderir. Sunucu tarafıyla haberleşmek için belirli bir protokol kullanılır. Sunucu, mesajları alır ve gerekli işlemleri gerçekleştirir veya diğer istemcilere iletir.
