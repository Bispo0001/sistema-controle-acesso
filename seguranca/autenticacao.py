import hashlib


def gerar_hash(senha):

    return hashlib.sha256(
        senha.encode()
    ).hexdigest()


def validar_senha(
    senha_digitada,
    senha_salva
):

    return (
        gerar_hash(senha_digitada)
        == senha_salva
    )