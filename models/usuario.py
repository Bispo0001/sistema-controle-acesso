import hashlib

class Usuario:

    def __init__(
        self,
        usuario_id,
        nome,
        login,
        senha,
        perfil
    ):

        self.usuario_id = usuario_id
        self.nome = nome
        self.login = login

        self.senha = hashlib.sha256(
            senha.encode()
        ).hexdigest()

        self.perfil = perfil

