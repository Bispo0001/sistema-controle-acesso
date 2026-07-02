from collections import deque

from estruturas.lista_usuarios import ListaUsuarios
from models.arquivo import Arquivo
from models.usuario import Usuario
from seguranca.autenticacao import validar_senha
from seguranca.permissoes import PERMISSOES


class SistemaAcesso:
    def __init__(self) -> None:
        self.usuarios = ListaUsuarios()
        self.arquivos: list[Arquivo] = []
        self.logs: deque[str] = deque()
        self.criar_admin()

    def criar_admin(self) -> None:
        admin = Usuario(1, "Administrador", "admin", "admin123", "Administrador")
        self.usuarios.adicionar(admin)

    def registrar_log(self, mensagem: str) -> None:
        self.logs.append(mensagem)

    def possui_permissao(self, usuario: Usuario, acao: str) -> bool:
        return acao in PERMISSOES[usuario.perfil]

    def cadastrar_usuario(self) -> None:
        print("\n=== CADASTRO DE USUÁRIO ===")
        usuario_id = int(input("ID: "))
        nome: str = input("Nome: ")
        login: str = input("Login: ")
        senha: str = input("Senha: ")
        print("\n1 - Administrador")
        print("2 - Gerente")
        print("3 - Funcionario")
        opcao: str = input("Perfil: ")
        perfis: dict[str, str] = {"1": "Administrador", "2": "Gerente", "3": "Funcionario"}
        perfil: str | None = perfis.get(opcao)
        if perfil is None:
            print("Perfil inválido!")
            return
        if self.usuarios.buscar_login(login):
            print("Login já existe!")
            return
        usuario = Usuario(usuario_id, nome, login, senha, perfil)
        self.usuarios.adicionar(usuario)
        self.registrar_log(f"Usuário {nome} cadastrado.")
        print("Usuário cadastrado com sucesso!")

    def login(self) -> Usuario | None:
        print("\n=== LOGIN ===")
        login: str = input("Login: ")
        senha: str = input("Senha: ")
        usuario: Usuario | None = self.usuarios.buscar_login(login)
        if usuario and validar_senha(senha, usuario.senha):
            self.registrar_log(f"Login realizado por {usuario.nome}")
            print("Login realizado com sucesso!")
            return usuario
        print("Login inválido!")
        return None

    def esqueci_senha(self) -> None:
        print("\n=== RECUPERAÇÃO DE SENHA ===")
        login: str = input("Login: ")
        usuario: Usuario | None = self.usuarios.buscar_login(login)
        if usuario is None:
            print("Usuário não encontrado.")
            return
        nova_senha: str = input("Nova senha: ")
        confirmacao: str = input("Confirme a nova senha: ")
        if nova_senha != confirmacao:
            print("As senhas não conferem.")
            return
        usuario.redefinir_senha(nova_senha)
        self.registrar_log(f"Senha redefinida para {usuario.nome}.")
        print("Senha redefinida com sucesso!")

    def cadastrar_arquivo(self, usuario: Usuario) -> None:
        if not self.possui_permissao(usuario, "criar"):
            print("Acesso negado!")
            self.registrar_log(f"{usuario.nome} tentou criar arquivo.")
            return
        print("\n=== CADASTRO DE ARQUIVO ===")
        nome: str = input("Nome do arquivo: ")
        conteudo: str = input("Conteúdo: ")
        arquivo = Arquivo(len(self.arquivos) + 1, nome, conteudo)
        self.arquivos.append(arquivo)
        self.registrar_log(f"{usuario.nome} criou o arquivo {nome}")
        print("Arquivo cadastrado com sucesso!")

    def listar_arquivos(self) -> None:
        print("\n=== ARQUIVOS ===")
        if not self.arquivos:
            print("Nenhum arquivo cadastrado.")
            return
        for arquivo in self.arquivos:
            print(f"ID: {arquivo.arquivo_id} | Nome: {arquivo.nome}")

    def acessar_arquivo(self, usuario: Usuario) -> None:
        if not self.possui_permissao(usuario, "ler"):
            print("Acesso negado!")
            return
        nome: str = input("Nome do arquivo: ")
        for arquivo in self.arquivos:
            if arquivo.nome == nome:
                self.registrar_log(f"{usuario.nome} acessou {arquivo.nome}")
                print("\nConteúdo:")
                print(arquivo.conteudo)
                return
        print("Arquivo não encontrado.")

    def excluir_arquivo(self, usuario: Usuario) -> None:
        if not self.possui_permissao(usuario, "excluir"):
            print("Acesso negado!")
            self.registrar_log(f"{usuario.nome} tentou excluir arquivo.")
            return
        nome: str = input("Nome do arquivo: ")
        for arquivo in self.arquivos:
            if arquivo.nome == nome:
                self.arquivos.remove(arquivo)
                self.registrar_log(f"{usuario.nome} excluiu {arquivo.nome}")
                print("Arquivo removido com sucesso!")
                return
        print("Arquivo não encontrado.")

    def mostrar_logs(self) -> None:
        print("\n=== LOGS DE AUDITORIA ===")
        if not self.logs:
            print("Nenhum log registrado.")
            return
        for log in self.logs:
            print(log)
