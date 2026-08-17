import pytest
from ecommerce.categoria import Categoria
from ecommerce.item_pedido import ItemPedido
from ecommerce.produto import Produto


class TestItemPedido:

    def setup_method(self) -> None:
        self.cat = Categoria("Informática")
        self.notebook = Produto("Notebook", 3500.0, 10, self.cat)

    def test_criar_item_pedido(self) -> None:
        item = ItemPedido(self.notebook, 2, self.notebook.preco)
        assert item.produto == self.notebook
        assert item.quantidade == 2
        assert item.preco_no_momento == 3500.0

    def test_calcular_subtotal(self) -> None:
        item = ItemPedido(self.notebook, 3, self.notebook.preco)
        assert item.calcular_subtotal() == 10500.0

    def test_quantidade_invalida(self) -> None:
        with pytest.raises(ValueError):
            ItemPedido(self.notebook, 0, self.notebook.preco)
            