import hashlib


def gerar_hash(senha: str) -> str:
    return hashlib.sha256(senha.encode()).hexdigest()


def validar_senha(senha_digitada: str, senha_salva: str) -> bool:
    return gerar_hash(senha_digitada) == senha_salva
