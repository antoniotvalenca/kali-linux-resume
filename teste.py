import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        msg = input("Mensagem: ") + "\n"
        client.sendto(msg.encode(), ("192.168.6.196", 9000))
        data, sender = client.recvfrom(1024)
        print(f"{sender[0]}: {data.decode()}")
except Exception as error:
    print("Ocorreu um erro de conexão")
