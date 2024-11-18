# test_carrinho.py

import pytest
from Carrinho import adicionar_ao_carrinho, remover_do_carrinho, calcular_total

def test_adicionar_ao_carrinho():
    """Testar adicionar produto ao carrinho"""
    resposta = adicionar_ao_carrinho("Açúcar de Uva 500G", 2)
    assert "2x Açúcar de Uva 500G adicionado(s) ao carrinho" in resposta

def test_remover_do_carrinho():
    """Testar remover produto do carrinho"""
    adicionar_ao_carrinho("Açúcar de Uva 500G", 2)
    resposta = remover_do_carrinho("Açúcar de Uva 500G")
    assert "Açúcar de Uva 500G removido do carrinho" in resposta

def test_calcular_total():
    """Testar cálculo do total do carrinho"""
    adicionar_ao_carrinho("Açúcar de Uva 500G", 2)
    total = calcular_total()
    assert total == 68.00  # 34.00 * 2
