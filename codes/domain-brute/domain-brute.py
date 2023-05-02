import sys
import dns.resolver

resolver = dns.resolver.Resolver()

try:
    target = sys.argv[1]
    wordlist = sys.argv[2]
except:
    print("Usage: python3 dnsbrutearquivo.py dominio.com wordlist.txt")

try:
    with open(wordlist, "r") as arq:
        sub_targets = arq.read().splitlines()
except:
    print("error: can't open file")

for sub_target in sub_targets:
    subdominio = f"{sub_target}.{target}"
    resultados = resolver.resolve(subdominio, "A")

    for resultado in resultados:
        print(f"{subdominio} => {resultado}")
