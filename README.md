# Sistema de Controle de Acesso

Aplicação em Python para cadastro de usuários, autenticação e controle de acesso a arquivos com base em perfis.

## Funcionalidades

- Login de usuários
- Recuperação de senha
- Cadastro e listagem de usuários
- Cadastro, consulta e exclusão de arquivos conforme perfil
- Registro de eventos em log local

## Perfis

- Administrador: cadastra usuários, gerencia arquivos e visualiza logs
- Gerente: cadastra e consulta arquivos
- Funcionário: consulta arquivos

## Execução

```bash
python main.py
```

## Observações

- As informações são mantidas em memória durante a execução
- As senhas são armazenadas com hash SHA-256
