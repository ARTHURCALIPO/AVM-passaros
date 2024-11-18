# Pagamento.py

from Carrinho import calcular_total

def processar_pagamento(valor_pago):
    """Processar o pagamento do valor total"""
    total = calcular_total()
    if valor_pago >= total:
        troco = valor_pago - total
        return f"Pagamento realizado com sucesso! Troco: R${troco:.2f}"
    else:
        return f"Valor insuficiente. Total: R${total:.2f}, Pago: R${valor_pago:.2f}"
