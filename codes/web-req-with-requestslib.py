import requests  # 1

header = {  # 2
    "...": "...",
    "...": "..."
}
res = requests.get("http://www.bancocn.com", headers=header)  # 3
html = res.text  # 4
print(html)

# 1) pip install requests
# 2) caso necessario, colocar os headers do site (em alguns servidores, é preciso passar o header do user-agent (que diz o navegador que voce esta usando,
# já que alguns sites so aceitam requisicao de navegadores) e cookies de autenticacao (por questoes de segurança))
# 3) após o requests, voce passa o método de requisicao (post, get, delete...)
# 4) o .text transforma a resposta para string
