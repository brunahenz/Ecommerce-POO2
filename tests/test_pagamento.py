import pytest
from datetime import date, timedelta
from ecommerce.categoria import Categoria
from ecommerce.pagamento import Pagamento
from ecommerce.pedido import Pedido
from ecommerce.produto import Produto
from ecommerce.pagamento import (
    Pagamento,
    PagamentoBoleto,
    PagamentoCartao,
    PagamentoPix,
)
from ecommerce.situacao_pagamento import SituacaoPagamento
from ecommerce.criador_pagamento import CriadorPagamento


class TestPagamento:

    def setup_method(self) -> None:
        self.cat = Categoria("Informática")
        self.notebook = Produto("Notebook", 3500.0, 10, self.cat)
        self.pedido = Pedido()
        self.pedido.adicionar_item(self.notebook, 1)

    def test_criar_pagamento(self) -> None:
        pag = PagamentoPix(self.pedido, 3500.0)
        assert pag.valor == 3500.0
        assert pag.confirmado is False

    def test_confirmar_pagamento(self) -> None:
        pag = PagamentoPix(self.pedido, 3500.0)
        pag.confirmar()
        assert pag.confirmado is True

    def test_valor_invalido_zero(self) -> None:
        with pytest.raises(ValueError):
            PagamentoPix(self.pedido, 0)

    def test_pagamento_e_abstrato(self) -> None:
        with pytest.raises(TypeError):
             Pagamento(self.pedido, 3500.0)

    def test_boleto_vencido_e_recusado(self) -> None:
        pag = PagamentoBoleto(
        self.pedido, 3500.0, linha_digitavel="123",
        vencimento=date.today() - timedelta(days=1),
        )
        pag.confirmar()
        assert pag.situacao == SituacaoPagamento.RECUSADO