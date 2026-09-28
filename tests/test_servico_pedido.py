from ecommerce.criador_pagamento import CriadorPagamento
from ecommerce.criador_notificacao import CanalNotificacao
from ecommerce.expedidor import Expedidor
from ecommerce.servico_notificacao_pedido import ServicoNotificacaoPedido
from ecommerce.servico_pedido import ServicoPedido
from ecommerce.pedido import Pedido
from ecommerce.entrega import Entrega, EntregaCorreios
from ecommerce.cliente import Cliente
from ecommerce.categoria import Categoria
from ecommerce.produto import Produto

from tests.test_servico_notificacao_pedido import (
    CriadorNotificacaoFake,
    NotificacaoEspia,
)


def test_colaboradores_podem_ser_trocados_sem_tocar_no_servico() -> None:
    class ExpedidorFake(Expedidor):
        def __init__(self) -> None:
            self.chamado = False

        def criar_entrega(self, pedido: Pedido) -> Entrega:
            self.chamado = True
            return EntregaCorreios(pedido, "FAKE-1")

    espia = NotificacaoEspia()

    cliente = Cliente(
        "João",
        "joao@email.com",
        telefone="+55 47 90000-0000",
        canal_preferido=CanalNotificacao.SMS,
    )

    categoria = Categoria("Informática")
    notebook = Produto("Notebook", 3500.0, 10, categoria)

    pedido = Pedido()
    pedido.adicionar_item(notebook, 1)

    expedidor_fake = ExpedidorFake()

    servico = ServicoPedido(
        criador_pagamento=CriadorPagamento(),
        expedidor=expedidor_fake,
        servico_notificacao=ServicoNotificacaoPedido(
            CriadorNotificacaoFake(espia)
        ),
    )

    servico.pagar(pedido, cliente)
    servico.despachar(pedido, cliente)

    assert expedidor_fake.chamado is True