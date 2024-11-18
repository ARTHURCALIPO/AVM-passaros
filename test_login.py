# test_login.py

import pytest
from Login import login_usuario

def test_login_sucesso():
    """Testar login bem-sucedido"""
    resposta = login_usuario("teste@exemplo.com", "senha123")
    assert resposta == "Login bem-sucedido"

def test_login_falha():
    """Testar login com credenciais erradas"""
    resposta = login_usuario("teste@exemplo.com", "senha_errada")
    assert resposta == "Email ou senha incorretos"
