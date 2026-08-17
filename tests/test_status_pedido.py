from ecommerce.status_pedido import StatusPedido


class TestStatusPedido:

    def test_transicao_valida(self) -> None:
        assert StatusPedido.transicao_valida(StatusPedido.CRIADO, StatusPedido.PAGO) is True
        assert StatusPedido.transicao_valida(StatusPedido.CRIADO, StatusPedido.CANCELADO) is True
        assert StatusPedido.transicao_valida(StatusPedido.PAGO, StatusPedido.ENVIADO) is True
        assert StatusPedido.transicao_valida(StatusPedido.ENVIADO, StatusPedido.ENTREGUE) is True

    def test_transicao_invalida(self) -> None:
        assert StatusPedido.transicao_valida(StatusPedido.CRIADO, StatusPedido.ENTREGUE) is False
        assert StatusPedido.transicao_valida(StatusPedido.CRIADO, StatusPedido.ENVIADO) is False
        assert StatusPedido.transicao_valida(StatusPedido.PAGO, StatusPedido.ENTREGUE) is False