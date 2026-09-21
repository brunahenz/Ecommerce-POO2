import pytest
from ecommerce.pedido import Pedido
from ecommerce.entrega import EntregaCorreios
from ecommerce.expedidor import ExpedidorLojaCentral


class TestExpedidor:

    def _pedido_pago(self) -> Pedido:
        pedido = Pedido()
        pedido.adicionar_item(self.notebook, 1)
        pedido.confirmar_pagamento()
        return pedido

    def test_loja_central_despacha_pelos_correios(self) -> None:
        entrega = ExpedidorLojaCentral().despachar(self._pedido_pago())
        assert isinstance(entrega, EntregaCorreios)
        assert entrega.modalidade == "SEDEX"

    def test_despachar_registra_entrega_e_muda_o_estado(self) -> None:
        pedido = self._pedido_pago()
        entrega = ExpedidorLojaCentral().despachar(pedido)
        assert pedido.entrega is entrega
        assert pedido.status == "enviado"

    def test_nao_despacha_pedido_nao_pago(self) -> None:
        pedido = Pedido()
        pedido.adicionar_item(self.notebook, 1)
        with pytest.raises(ValueError):
            ExpedidorLojaCentral().despachar(pedido)