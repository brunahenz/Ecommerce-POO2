from datetime import date, timedelta

from ecommerce.forma_pagamento import FormaPagamento
from ecommerce.pagamento import (
    Pagamento,
    PagamentoBoleto,
    PagamentoCartao,
    PagamentoPix,
)


class CriadorPagamento:

    @staticmethod
    def criar(forma: FormaPagamento, pedido, valor: float, **dados) -> Pagamento:
        if forma == FormaPagamento.PIX:
            return PagamentoPix(pedido, valor, **dados)
        elif forma == FormaPagamento.CARTAO_CREDITO:
            return PagamentoCartao(pedido, valor, **dados)
        elif forma == FormaPagamento.BOLETO:
            return PagamentoBoleto(pedido, valor, **dados)
        else:
            raise ValueError(f"Forma de pagamento não suportada: {forma}")

CHAVE_PIX_DA_LOJA = "loja@ecommerce.com"


class CriadorPagamento:

    def criar(self, forma: FormaPagamento, pedido, valor: float, **dados) -> "Pagamento":
        if forma == FormaPagamento.PIX:
            return PagamentoPix(pedido, valor, chave=dados.get("chave", CHAVE_PIX_DA_LOJA))
        if forma == FormaPagamento.BOLETO:
            return PagamentoBoleto(
                pedido, valor,
                linha_digitavel=dados.get("linha_digitavel", "..."),
                vencimento=dados.get("vencimento", date.today() + timedelta(days=3)),
            )
        if forma == FormaPagamento.CARTAO_CREDITO:
            return PagamentoCartao(
                pedido, valor,
                bandeira=dados.get("bandeira", "VISA"),
                parcelas=dados.get("parcelas", 1),
            )
        raise ValueError(f"Forma de pagamento desconhecida: {forma}")