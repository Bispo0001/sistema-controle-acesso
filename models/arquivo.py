class Arquivo:
    def __init__(self, arquivo_id: int, nome: str, conteudo: str) -> None:
        self.arquivo_id: int = arquivo_id
        self.nome: str = nome
        self.conteudo: str = conteudo
