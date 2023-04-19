import ipaddress

ip = ipaddress.ip_address("192.168.6.1")
print(ip)  # --> 192.168.6.1 <-- #
print(ip + 3)  # --> 192.168.6.4 <-- #
print(ip + 10000)  # --> 192.168.45.17 <-- #


# --> guarda um bloco de IPs <-- #
network = ipaddress.ip_network("192.168.6.0/24")

for ip in network:  # --> o "ip" não se refere à variável ip <-- #
    print(ip)
