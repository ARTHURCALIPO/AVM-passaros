# test_pagamento.py

import pytest
from Pagamento import processar_pagamento
from Carrinho import adicionar_ao_carrinho

def test_pagamento_sucesso():
    """Testar pagamento bem-sucedido"""
    adicionar_ao_carrinho("Açúcar de Uva 500G", 2)
    resposta = processar_pagamento(70.00)
    assert "Pagamento realizado com sucesso! Troco: R$2.00" in resposta

def test_pagamento_insuficiente():
    """Testar pagamento insuficiente"""
    adicionar_ao_carrinho("Açúcar de Uva 500G", 2)
    resposta = processar_pagamento(60.00)
    assert "Valor insuficiente" in resposta
