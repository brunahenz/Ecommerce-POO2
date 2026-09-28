from ecommerce.criador_pagamento import CriadorPagamento
from ecommerce.expedidor import Expedidor
from ecommerce.servico_notificacao_pedido import ServicoNotificacaoPedido
from ecommerce.forma_pagamento import FormaPagamento
from ecommerce.entrega import Entrega



class ServicoPedido:

    def __init__(
        self,
        criador_pagamento: CriadorPagamento,
        expedidor: Expedidor,
        servico_notificacao: ServicoNotificacaoPedido,
    ) -> None:
        self._criador_pagamento = criador_pagamento
        self._expedidor = expedidor
        self._servico_notificacao = servico_notificacao

    def pagar(self, pedido, cliente, forma: FormaPagamento = FormaPagamento.PIX, **dados) -> None:
        pedido.confirmar_pagamento(self._criador_pagamento, forma, **dados)
        self._servico_notificacao.pedido_pago(pedido, cliente)

    def despachar(self, pedido, cliente) -> Entrega:
        entrega = self._expedidor.despachar(pedido)
        self._servico_notificacao.pedido_enviado(pedido, cliente)
        return entrega