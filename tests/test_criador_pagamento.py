import pytest
from ecommerce.criador_pagamento import CriadorPagamento
from ecommerce.pedido import Pedido
from ecommerce.produto import Produto
from ecommerce.forma_pagamento import FormaPagamento
from ecommerce.pagamento import (
    Pagamento,
    PagamentoBoleto,
    PagamentoCartao,
    PagamentoPix,
)


class TestCriadorPagamento:

    def setup_method(self) -> None:
        self.pedido = Pedido()
        self.pedido.adicionar_item(self.notebook, 1)
        self.criador = CriadorPagamento()

    def test_cria_pagamento_pix(self) -> None:
        pagamento = self.criador.criar(FormaPagamento.PIX, self.pedido, 3500.0)
        assert isinstance(pagamento, PagamentoPix)

    def test_cria_pagamento_cartao_com_parcelas(self) -> None:
        pagamento = self.criador.criar(
            FormaPagamento.CARTAO_CREDITO, self.pedido, 3600.0, parcelas=3
        )
        assert isinstance(pagamento, PagamentoCartao)
        assert pagamento.parcelas == 3

    def test_forma_desconhecida_lanca_erro(self) -> None:
        with pytest.raises(ValueError):
            self.criador.criar("pix", self.pedido, 3500.0)