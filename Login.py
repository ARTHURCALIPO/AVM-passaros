# Login.py

from Cadastro import usuarios

def login_usuario(email, senha):
    """Fazer login de um usuário."""
    for usuario in usuarios:
        if usuario["email"] == email and usuario["senha"] == senha:
            return "Login bem-sucedido"
    return "Email ou senha incorretos"
