from models.no_usuario import NoUsuario


class ListaUsuarios:

    def __init__(self):
        self.inicio = None

    def adicionar(self, usuario):

        novo_no = NoUsuario(usuario)

        if self.inicio is None:
            self.inicio = novo_no
            return

        atual = self.inicio

        while atual.proximo:
            atual = atual.proximo

        atual.proximo = novo_no

    def buscar_login(self, login):

        atual = self.inicio

        while atual:

            if atual.usuario.login == login:
                return atual.usuario

            atual = atual.proximo

        return None

    def listar(self):

        atual = self.inicio

        while atual:

            usuario = atual.usuario

            print(
                f"ID: {usuario.usuario_id} | "
                f"Nome: {usuario.nome} | "
                f"Perfil: {usuario.perfil}"
            )

            atual = atual.proximo