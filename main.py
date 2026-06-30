from typing import TYPE_CHECKING

from services.sistema_acesso import SistemaAcesso

if TYPE_CHECKING:
    from models.usuario import Usuario


def menu() -> None:  # noqa: C901, PLR0912, PLR0915
    sistema = SistemaAcesso()
    usuario_logado: Usuario | None = None
    while True:
        # =====================================================================
        # USUÁRIO NÃO LOGADO
        # =====================================================================
        if usuario_logado is None:
            print("\n" + "=" * 20)
            print(" SISTEMA DE ACESSO ")
            print("=" * 20)
            print("1 - Login")
            print("0 - Sair")
            opcao: str = input("\nEscolha: ")
            if opcao == "1":
                usuario_logado: Usuario | None = sistema.login()
            elif opcao == "0":
                print("Sistema encerrado.")
                break
            else:
                print("Faça login primeiro.")
        # =====================================================================
        # ADMINISTRADOR
        # =====================================================================
        elif usuario_logado.perfil == "Administrador":
            print("\n" + "=" * 20)
            print(" SISTEMA DE ACESSO ")
            print("=" * 20)
            print(f"Usuário: {usuario_logado.nome}")
            print(f"Perfil: {usuario_logado.perfil}")
            print("\n1 - Cadastrar Usuário")
            print("2 - Listar Usuários")
            print("3 - Cadastrar Arquivo")
            print("4 - Listar Arquivos")
            print("5 - Ler Arquivo")
            print("6 - Excluir Arquivo")
            print("7 - Ver Logs")
            print("8 - Logout")
            print("0 - Sair")

            opcao: str = input("\nEscolha: ")

            if opcao == "1":
                sistema.cadastrar_usuario()
            elif opcao == "2":
                sistema.usuarios.listar()
            elif opcao == "3":
                sistema.cadastrar_arquivo(usuario_logado)
            elif opcao == "4":
                sistema.listar_arquivos()
            elif opcao == "5":
                sistema.acessar_arquivo(usuario_logado)
            elif opcao == "6":
                sistema.excluir_arquivo(usuario_logado)
            elif opcao == "7":
                sistema.mostrar_logs()
            elif opcao == "8":
                usuario_logado = None
                print("Logout realizado.")
            elif opcao == "0":
                print("Sistema encerrado.")
                break
            else:
                print("Opção inválida.")
        # =====================================================================
        # GERENTE
        # =====================================================================
        elif usuario_logado.perfil == "Gerente":
            print("\n" + "=" * 20)
            print(" SISTEMA DE ACESSO ")
            print("=" * 20)
            print(f"Usuário: {usuario_logado.nome}")
            print(f"Perfil: {usuario_logado.perfil}")
            print("\n1 - Cadastrar Arquivo")
            print("2 - Listar Arquivos")
            print("3 - Ler Arquivo")
            print("4 - Logout")
            print("0 - Sair")

            opcao: str = input("\nEscolha: ")

            if opcao == "1":
                sistema.cadastrar_arquivo(usuario_logado)
            elif opcao == "2":
                sistema.listar_arquivos()
            elif opcao == "3":
                sistema.acessar_arquivo(usuario_logado)
            elif opcao == "4":
                usuario_logado = None
                print("Logout realizado.")
            elif opcao == "0":
                print("Sistema encerrado.")
                break
            else:
                print("Opção inválida.")
        # =====================================================================
        # FUNCIONÁRIO
        # =====================================================================
        elif usuario_logado.perfil == "Funcionario":
            print("\n" + "=" * 20)
            print(" SISTEMA DE ACESSO ")
            print("=" * 20)
            print(f"Usuário: {usuario_logado.nome}")
            print(f"Perfil: {usuario_logado.perfil}")
            print("\n1 - Listar Arquivos")
            print("2 - Ler Arquivo")
            print("3 - Logout")
            print("0 - Sair")

            opcao: str = input("\nEscolha: ")

            if opcao == "1":
                sistema.listar_arquivos()
            elif opcao == "2":
                sistema.acessar_arquivo(usuario_logado)
            elif opcao == "3":
                usuario_logado = None
                print("Logout realizado.")
            elif opcao == "0":
                print("Sistema encerrado.")
                break
            else:
                print("Opção inválida.")


if __name__ == "__main__":
    menu()
