import socket


def scan(host, ports):
    opened_ports = []
    try:
        for port in ports:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(0.5)

            status_code = client.connect_ex((host, port))

            if status_code == 0:
                opened_ports.append(port)

        print(f"HOST: {host} // OPEN_PORTS: {opened_ports}")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        host = sys.argv[1]

        if len(sys.argv) >= 3:
            ports = sys.argv[2].split(",")
            ports = [int(port) for port in ports]

        else:
            ports = [21, 22, 23, 25, 80, 443, 445, 8080, 8443, 3306, 139, 135]

        scan(host, ports)

    else:
        print("Usage: python portscan.py <ip/domain> <port/ports>")
        print("EX: python portscan.py google.com 22,23,80")
