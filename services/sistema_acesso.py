from collections import deque

from models.usuario import Usuario
from models.arquivo import Arquivo

from estruturas.lista_usuarios import ListaUsuarios

from seguranca.permissoes import PERMISSOES

from seguranca.autenticacao import validar_senha


class SistemaAcesso:

    def __init__(self):

        self.usuarios = ListaUsuarios()
        self.arquivos = []
        self.logs = deque()

        self.criar_admin()

    # ---------------------------------

    def criar_admin(self):

        admin = Usuario(
            1,
            "Administrador",
            "admin",
            "admin123",
            "Administrador"
        )

        self.usuarios.adicionar(admin)

    # ---------------------------------

    def registrar_log(self, mensagem):

        self.logs.append(mensagem)

    # ---------------------------------

    def possui_permissao(self, usuario, acao):

        return acao in PERMISSOES[usuario.perfil]

    # ---------------------------------

    def cadastrar_usuario(self):

        print("\n=== CADASTRO DE USUÁRIO ===")

        usuario_id = int(input("ID: "))
        nome = input("Nome: ")
        login = input("Login: ")
        senha = input("Senha: ")

        print("\n1 - Administrador")
        print("2 - Gerente")
        print("3 - Funcionario")

        opcao = input("Perfil: ")

        perfis = {
            "1": "Administrador",
            "2": "Gerente",
            "3": "Funcionario"
        }

        perfil = perfis.get(opcao)

        if perfil is None:
            print("Perfil inválido!")
            return

        if self.usuarios.buscar_login(login):
            print("Login já existe!")
            return

        usuario = Usuario(
            usuario_id,
            nome,
            login,
            senha,
            perfil
        )

        self.usuarios.adicionar(usuario)

        self.registrar_log(
            f"Usuário {nome} cadastrado."
        )

        print("Usuário cadastrado com sucesso!")

    # ---------------------------------

    def login(self):

        print("\n=== LOGIN ===")

        login = input("Login: ")
        senha = input("Senha: ")

        usuario = self.usuarios.buscar_login(login)

        if usuario and validar_senha(
            senha,
            usuario.senha
        ):

            self.registrar_log(
                f"Login realizado por {usuario.nome}"
            )

            print("Login realizado com sucesso!")

            return usuario

        print("Login inválido!")

        return None

    # ---------------------------------

    def cadastrar_arquivo(self, usuario):

        if not self.possui_permissao(
            usuario,
            "criar"
        ):

            print("Acesso negado!")

            self.registrar_log(
                f"{usuario.nome} tentou criar arquivo."
            )

            return

        print("\n=== CADASTRO DE ARQUIVO ===")

        nome = input("Nome do arquivo: ")
        conteudo = input("Conteúdo: ")

        arquivo = Arquivo(
            len(self.arquivos) + 1,
            nome,
            conteudo
        )

        self.arquivos.append(arquivo)

        self.registrar_log(
            f"{usuario.nome} criou o arquivo {nome}"
        )

        print("Arquivo cadastrado com sucesso!")

    # ---------------------------------

    def listar_arquivos(self):

        print("\n=== ARQUIVOS ===")

        if not self.arquivos:
            print("Nenhum arquivo cadastrado.")
            return

        for arquivo in self.arquivos:

            print(
                f"ID: {arquivo.arquivo_id} | "
                f"Nome: {arquivo.nome}"
            )

    # ---------------------------------

    def acessar_arquivo(self, usuario):

        if not self.possui_permissao(
            usuario,
            "ler"
        ):
            print("Acesso negado!")
            return

        nome = input("Nome do arquivo: ")

        for arquivo in self.arquivos:

            if arquivo.nome == nome:

                self.registrar_log(
                    f"{usuario.nome} acessou {arquivo.nome}"
                )

                print("\nConteúdo:")
                print(arquivo.conteudo)

                return

        print("Arquivo não encontrado.")

    # ---------------------------------

    def excluir_arquivo(self, usuario):

        if not self.possui_permissao(
            usuario,
            "excluir"
        ):

            print("Acesso negado!")

            self.registrar_log(
                f"{usuario.nome} tentou excluir arquivo."
            )

            return

        nome = input("Nome do arquivo: ")

        for arquivo in self.arquivos:

            if arquivo.nome == nome:

                self.arquivos.remove(arquivo)

                self.registrar_log(
                    f"{usuario.nome} excluiu {arquivo.nome}"
                )

                print("Arquivo removido com sucesso!")

                return

        print("Arquivo não encontrado.")

    # ---------------------------------

    def mostrar_logs(self):

        print("\n=== LOGS DE AUDITORIA ===")

        if not self.logs:
            print("Nenhum log registrado.")
            return

        for log in self.logs:
            print(log)
            