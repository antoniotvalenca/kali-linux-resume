# --> CODIGO BASE <-- #

from urllib import request, parse
from urllib import request

response = request.urlopen("http://g1.com.br")  # 1
html = response.read()  # 2
print(html)

# 1) Retorna um objeto de resposta da requisição
# 2) o .read() vai ler esse objeto (transformar em string)
# __________________________________________________________________________________________________________________________________________________________________ #

# --> REQUISIÇÕES QUE EXIGEM HEADER (COOKIES, OU QUE INDIQUEM QUE ESTAO SENDO FEITAS EM UM NAVEGADOR)


# 1

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Cookie": "PHPSESSID=nf3k2v6ct1p7ns34p4n9br2hq6; cf_clearance=Svk.M699dS.k9v9pMBwdJ_o4jJ8pNdT9XmjY5vrtS3Q-1682533684-0-250"
}

req = request.Request("http://www.bancocn.com", headers=header)  # 3
res = request.urlopen(req)

html = response.read()

print(html)

# 1) fiz uma req no site pelo navegador e absorvi o seu header, pois, no caso do site que quero acessar, é preciso que a requisição mande
# que eu estou fazendo em um navegador (user-agent) e o cookie de autenticação
# 3) passo o header como parametro do "headers"
# __________________________________________________________________________________________________________________________________________________________________ #

# --> FAZENDO UMA REQ POST <-- #


header = {
    "...": "...",
    "...": "..."
}

dados = {
    "user": "admin",
    "password": "senhaTal"
}  # 1

dados = parse.urlencode(dados).encode()  # 2

req = request.Request("http://www.bancocn.com/admin/index.php",
                      headers=header, data=dados)  # 3
res = request.urlopen(req)
html = res.read()
print(html)

# 1) guardo os dados que serão inseridos
# 2) transformo no formato que o navegador vai receber
# 3) passo como parametro do "data"
