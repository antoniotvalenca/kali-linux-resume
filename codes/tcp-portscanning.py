# --> CÓDIGO BASE <-- #

import sys
import socket

host = "google.com"
port = 80


# --> criando client tcp <-- #
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# --> colocando o codigo para rodar num max. de meio segundo e não ficar demorando <-- #
client.settimeout(0.5)
# --> normalmente usamos .connect e ficamos esperando por uma conexão <--#
status_code = client.connect_ex((host, port))
# --> no caso do .connect_ex, ele continua o programa mesmo se não houver conexão, enquanto o outro espera a conexão para rodar o resto <--#
# --> e o .connect_ex, quando não consegue conectar, ele retorna o status de conexão ao invés de cair num exception <-- #
if status_code == 0:
    print(f"[+] {port} open.")
# --> https://gist.github.com/gabrielfalcao/4216897 para ver o que cada status code significa <--#
else:
    print(f"[-] {port} closed.")

# __________________________________________________________________________________________________________________________________________________________________ #
# --> CÓDIGO COMPLETO <-- #

# import socket

# host = "yahoo.co.jp"
# ports = range(100) // vai do 0 até o 100
# opened_ports = []

# for port in ports:
#     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client.settimeout(0.5)

#     code = client.connect_ex((host, port))

#     if code == 0:
#         opened_ports.append(port)

# print(f"HOST: {host} // OPEN_PORTS: {opened_ports}")

# __________________________________________________________________________________________________________________________________________________________________ #
# --> CÓDIGO COMPLETO PARA USAR NO TERMINAL <-- #


# def scan(host, ports):
#     opened_ports = []
#     try:
#         for port in ports:
#             client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#             client.settimeout(0.5)

#             status_code = client.connect_ex((host, port))

#             if status_code == 0:
#                 opened_ports.append(port)

#         print(f"HOST: {host} // OPEN_PORTS: {opened_ports}")

#     except Exception as e:
#         print(e)


# if __name__ == "__main__":
#     if len(sys.argv) >= 2:
#         host = sys.argv[1]

#         if len(sys.argv) >= 3:
#             ports = sys.argv[2].split(",")
#             ports = [int(port) for port in ports] // transformando em int, já que no split transforma em str

#         else:
#             ports = [21, 22, 23, 25, 80, 443, 445, 8080, 8443, 3306, 139, 135]

#         scan(host, ports)

#     else:
#         print("Usage: python portscan.py <ip/domain> <port/ports>")
#         print("EX: python portscan.py google.com 22,23,80")
