# test_produtos.py

import pytest
from Produtos import listar_produtos, buscar_produto

def test_listar_produtos():
    """Testar a listagem de produtos"""
    produtos = listar_produtos()
    assert len(produtos) > 0  # Verifica se a lista de produtos não está vazia

def test_buscar_produto():
    """Testar a busca por produto"""
    produto = buscar_produto("Açúcar de Uva 500G")
    assert produto is not None
    assert produto["nome"] == "Açúcar de Uva 500G"
    assert produto["preco"] == 34.00

def test_buscar_produto_inexistente():
    """Testar busca por produto inexistente"""
    produto = buscar_produto("Produto Inexistente")
    assert produto is None
