from ecommerce.criador_pagamento import CriadorPagamento
from ecommerce.expedidor import Expedidor
from ecommerce.servico_notificacao_pedido import ServicoNotificacaoPedido
from ecommerce.servico_pedido import ServicoPedido
from ecommerce.pedido import Pedido
from ecommerce.entrega import Entrega, EntregaCorreios


def test_colaboradores_podem_ser_trocados_sem_tocar_no_servico(self) -> None:
    class ExpedidorFake(Expedidor):
        def __init__(self) -> None:
            self.chamado = False

        def criar_entrega(self, pedido: Pedido) -> Entrega:
            self.chamado = True
            return EntregaCorreios(pedido, "FAKE-1")

    expedidor_fake = ExpedidorFake()
    servico = ServicoPedido(
        criador_pagamento=CriadorPagamento(),
        expedidor=expedidor_fake,
        servico_notificacao=ServicoNotificacaoPedido(CriadorNotificacaoFake(self.espia)),
    )

    servico.pagar(pedido, self.cliente)
    servico.despachar(pedido, self.cliente)
    assert expedidor_fake.chamado is True