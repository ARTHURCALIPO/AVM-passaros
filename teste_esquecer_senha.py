# test_esquecer_senha.py

import pytest
from EsquecerSenha import recuperar_senha

def test_recuperar_senha():
    """Testar recuperação de senha"""
    resposta = recuperar_senha("teste@exemplo.com")
    assert "Sua senha é: senha123" in resposta

def test_recuperar_senha_usuario_inexistente():
    """Testar recuperação de senha para email não cadastrado"""
    resposta = recuperar_senha("usuario_inexistente@exemplo.com")
    assert "Email não encontrado" in resposta
