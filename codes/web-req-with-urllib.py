# --> CODIGO BASE <-- #

from urllib import request

# --> retorna um objeto de resposta da requisição <-- #
response = request.urlopen("http://g1.com.br")
# --> o .read() vai ler esse objeto <-- #
html = response.read()
print(html)

# __________________________________________________________________________________________________________________________________________________________________ #
# --> REQUISIÇÕES QUE EXIGEM HEADER (COOKIES, OU QUE INDIQUEM QUE ESTAO SENDO FEITAS EM UM NAVEGADOR)
# from urllib import request

# # --> fiz uma req no site pelo navegador e absorvi o seu header, pois, no caso do site que quero acessar, é preciso que a requisição mande <-- #
# # --> que eu estou fazendo em um navegador (user-agent) e o cookie de autenticação <-- #

# header = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
#     "Cookie": "PHPSESSID=nf3k2v6ct1p7ns34p4n9br2hq6; cf_clearance=Svk.M699dS.k9v9pMBwdJ_o4jJ8pNdT9XmjY5vrtS3Q-1682533684-0-250"
# }
# # --> retorna um objeto de resposta da requisição <-- #
# response = request.urlopen("http://g1.com.br")

# # --> o .read() vai ler esse objeto <-- #
# html = response.read()

# print(html)
