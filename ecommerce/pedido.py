from ecommerce.item_pedido import ItemPedido
from ecommerce.status_pedido import StatusPedido
from ecommerce.pagamento import Pagamento
from ecommerce.estrategia_desconto import EstrategiaDesconto
from ecommerce.cupom import Cupom
from ecommerce.estrategia_frete import EstrategiaFrete


class Pedido:
    def __init__(self) -> None:
        self._itens: list[ItemPedido] = []
        self._status = StatusPedido.CRIADO
        self._pagamento: Pagamento | None = None
        self._cupom: Cupom | None = None

    @property
    def itens(self) -> list[ItemPedido]:
        return list(self._itens)

    @property
    def status(self) -> str:
        return self._status

    @property
    def pagamento(self) -> Pagamento | None:
        return self._pagamento

    @property
    def cupom(self) -> Cupom | None:
        return self._cupom

    def calcular_valor_final(
        self,
        estrategia_desconto: EstrategiaDesconto | None = None,
        estrategia_frete: EstrategiaFrete | None = None,
    ) -> float:
        total = self.calcular_total(estrategia_desconto)
        if estrategia_frete is None:
            return total
        return total + estrategia_frete.calcular(total)

    def adicionar_item(self, produto: "Produto", quantidade: int) -> None:
        if self._status != StatusPedido.CRIADO:
            raise ValueError("Não é possível adicionar itens a um pedido já finalizado")
        preco_no_momento = produto.preco
        self._itens.append(ItemPedido(produto, quantidade, preco_no_momento))

    def calcular_total(
        self, estrategia_desconto: EstrategiaDesconto | None = None) -> float:
        total = sum(item.calcular_subtotal() for item in self._itens)
        if self._cupom is not None:
            return self._cupom.calcular_desconto(total)
        if estrategia_desconto is None:
            return total
        return estrategia_desconto.calcular(total)

    def aplicar_cupom(self, cupom: Cupom) -> None:
        if not cupom.esta_valido():
            raise ValueError(f"Cupom {cupom.codigo} esta expirado")
        self._cupom = cupom

    def quantidade_itens(self) -> int:
        return len(self._itens)

    def _transicionar(self, novo_status: str) -> None:
        if not StatusPedido.transicao_valida(self._status, novo_status):
            raise ValueError(f"Transicao invalida: {self._status} -> {novo_status}")
        self._status = novo_status

    def pagar(self) -> None:
        self._transicionar(StatusPedido.PAGO)
        self._pagamento = Pagamento(self, self.calcular_total())

    def confirmar_pagamento(self) -> None:
        self._transicionar(StatusPedido.PAGO)
        self._pagamento = Pagamento(self, self.calcular_total())
        self._pagamento.confirmar()

    def enviar(self) -> None:
        self._transicionar(StatusPedido.ENVIADO)

    def entregar(self) -> None:
        self._transicionar(StatusPedido.ENTREGUE)

    def cancelar(self) -> None:
        self._transicionar(StatusPedido.CANCELADO)
