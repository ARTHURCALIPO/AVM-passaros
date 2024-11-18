# test_cadastro.py

import pytest
from Cadastro import cadastrar_usuario, login_usuario, usuarios

def test_cadastrar_usuario():
    """Testar o cadastro de um novo usuário"""
    usuarios.clear()  # Limpa a lista antes de começar o teste
    resposta = cadastrar_usuario("teste@exemplo.com", "senha123")
    assert resposta == "Usuário cadastrado com sucesso"
    assert len(usuarios) == 1
    assert usuarios[0]["email"] == "teste@exemplo.com"

def test_cadastrar_usuario_existente():
    """Testar o cadastro de um usuário já existente"""
    usuarios.clear()
    cadastrar_usuario("teste@exemplo.com", "senha123")
    resposta = cadastrar_usuario("teste@exemplo.com", "senha123")
    assert resposta == "Usuário já cadastrado"

def test_login_usuario():
    """Testar o login de um usuário"""
    usuarios.clear()
    cadastrar_usuario("teste@exemplo.com", "senha123")
    resposta = login_usuario("teste@exemplo.com", "senha123")
    assert resposta == "Login bem-sucedido"

def test_login_usuario_incorreto():
    """Testar login com credenciais erradas"""
    usuarios.clear()
    cadastrar_usuario("teste@exemplo.com", "senha123")
    resposta = login_usuario("teste@exemplo.com", "senha_errada")
    assert resposta == "Email ou senha incorretos"
