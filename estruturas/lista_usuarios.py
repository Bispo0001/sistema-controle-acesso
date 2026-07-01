from typing import TYPE_CHECKING

from models.no_usuario import NoUsuario

if TYPE_CHECKING:
    from models.usuario import Usuario


class ListaUsuarios:
    def __init__(self) -> None:
        self.inicio: NoUsuario | None = None

    def adicionar(self, usuario: Usuario) -> None:
        novo_no = NoUsuario(usuario)
        if self.inicio is None:
            self.inicio: NoUsuario = novo_no
            return
        atual: NoUsuario = self.inicio
        while atual.proximo:
            atual: NoUsuario = atual.proximo
        atual.proximo = novo_no

    def buscar_login(self, login: str) -> Usuario | None:
        atual: NoUsuario | None = self.inicio
        while atual:
            if atual.usuario.login == login:
                return atual.usuario
            atual: NoUsuario | None = atual.proximo
        return None

    def listar(self) -> None:
        atual: NoUsuario | None = self.inicio
        while atual:
            usuario: Usuario = atual.usuario
            print(f"ID: {usuario.usuario_id} | Nome: {usuario.nome} | Perfil: {usuario.perfil}")
            atual: NoUsuario | None = atual.proximo
