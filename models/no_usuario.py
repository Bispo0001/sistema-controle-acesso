from models.usuario import Usuario


class NoUsuario:
    def __init__(self, usuario: Usuario) -> None:
        self.usuario: Usuario = usuario
        self.proximo: NoUsuario | None = None
