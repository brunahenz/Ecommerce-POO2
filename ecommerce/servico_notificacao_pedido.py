from ecommerce.criador_notificacao import CriadorNotificacao
from ecommerce.notificacao import Notificacao

class ServicoNotificacaoPedido:

    def __init__(self, criador_notificacao: CriadorNotificacao) -> None:
        self._criador_notificacao = criador_notificacao

    def pedido_pago(self, pedido: "Pedido", cliente: "Cliente") -> None:
        mensagem = (
            f"Ola, {cliente.nome}. O pagamento do seu pedido foi confirmado. "
            f"Total: R$ {pedido.calcular_total():.2f}."
        )
        self._notificar(cliente, mensagem)

    def pedido_enviado(self, pedido: "Pedido", cliente: "Cliente") -> None:
        rastreio = pedido.entrega.codigo_rastreio if pedido.entrega is not None else "-"
        mensagem = (
            f"Ola, {cliente.nome}. Seu pedido foi enviado. "
            f"Codigo de rastreio: {rastreio}."
        )
        self._notificar(cliente, mensagem)

    def _notificar(self, cliente: "Cliente", mensagem: str) -> None:
        notificacao = self._criador_notificacao.criar(cliente.canal_preferido)
        notificacao.enviar(cliente.contato, mensagem)

    