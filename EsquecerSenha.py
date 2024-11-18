# EsquecerSenha.py

from Cadastro import usuarios

def recuperar_senha(email):
    """Recuperar senha de um usuário pelo email"""
    for usuario in usuarios:
        if usuario["email"] == email:
            return f"Sua senha é: {usuario['senha']}"
    return "Email não encontrado"
