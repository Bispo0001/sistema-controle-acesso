import hashlib


class Usuario:
    def __init__(self, usuario_id: int, nome: str, login: str, senha: str, perfil: str) -> None:
        self.usuario_id: int = usuario_id
        self.nome: str = nome
        self.login: str = login
        self.senha: str = hashlib.sha256(senha.encode()).hexdigest()
        self.perfil: str = perfil

    def redefinir_senha(self, nova_senha: str) -> None:
        self.senha: str = hashlib.sha256(nova_senha.encode()).hexdigest()
