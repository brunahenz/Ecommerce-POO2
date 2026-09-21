from abc import ABC, abstractmethod
from datetime import date

from ecommerce.situacao_pagamento import SituacaoPagamento


class Pagamento(ABC):
    def __init__(self, pedido: "Pedido", valor: float) -> None:
        if valor <= 0:
            raise ValueError("Valor do pagamento deve ser positivo")
        self._pedido = pedido
        self._valor = valor
        self._data = date.today()
        self._situacao = SituacaoPagamento.PENDENTE

    @property
    def situacao(self) -> SituacaoPagamento:
        return self._situacao

    @property
    def confirmado(self) -> bool:
        return self._situacao == SituacaoPagamento.CONFIRMADO

    def confirmar(self) -> None:
        if self._situacao == SituacaoPagamento.CONFIRMADO:
            raise ValueError("Pagamento ja foi confirmado")
        self._situacao = self._processar()

    @abstractmethod
    def _processar(self) -> SituacaoPagamento: ...


class PagamentoPix(Pagamento):
    def __init__(self, pedido: "Pedido", valor: float, chave: str) -> None:
        super().__init__(pedido, valor)
        self._chave = chave

    def _processar(self) -> SituacaoPagamento:
        # A compensacao do Pix e imediata: nada mais precisa acontecer.
        return SituacaoPagamento.CONFIRMADO


class PagamentoBoleto(Pagamento):
    def __init__(self, pedido, valor, linha_digitavel: str, vencimento: date) -> None:
        super().__init__(pedido, valor)
        self._linha_digitavel = linha_digitavel
        self._vencimento = vencimento

    def _processar(self) -> SituacaoPagamento:
        if date.today() > self._vencimento:
            return SituacaoPagamento.RECUSADO
        return SituacaoPagamento.CONFIRMADO


class PagamentoCartao(Pagamento):
    def __init__(self, pedido, valor, bandeira: str, parcelas: int = 1) -> None:
        super().__init__(pedido, valor)
        if parcelas < 1:
            raise ValueError("Numero de parcelas deve ser no minimo 1")
        self._bandeira = bandeira
        self._parcelas = parcelas

    def valor_parcela(self) -> float:
        return self._valor / self._parcelas

    def _processar(self) -> SituacaoPagamento:
        return SituacaoPagamento.CONFIRMADO
