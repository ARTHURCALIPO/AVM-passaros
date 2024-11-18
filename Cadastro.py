# Cadastro.py

usuarios = []  # Lista para armazenar usuários cadastrados

def cadastrar_usuario(email, senha):
    """Cadastrar um novo usuário."""
    for usuario in usuarios:
        if usuario["email"] == email:
            return "Usuário já cadastrado"
    
    usuarios.append({"email": email, "senha": senha})
    return "Usuário cadastrado com sucesso"

def login_usuario(email, senha):
    """Fazer login de um usuário."""
    for usuario in usuarios:
        if usuario["email"] == email and usuario["senha"] == senha:
            return "Login bem-sucedido"
    return "Email ou senha incorretos"