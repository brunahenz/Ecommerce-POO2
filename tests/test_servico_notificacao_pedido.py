

from ecommerce.notificacao import Notificacao

from ecommerce.criador_notificacao import CanalNotificacao

class NotificacaoEspia(Notificacao):
    def __init__(self) -> None:
        self.enviadas: list[tuple[str, str]] = []

    def enviar(self, destinatario: str, mensagem: str) -> None:
        self.enviadas.append((destinatario, mensagem))


class CriadorNotificacaoFake:
    def __init__(self, notificacao: Notificacao) -> None:
        self._notificacao = notificacao
        self.canais_pedidos: list[CanalNotificacao] = []

    def criar(self, canal: CanalNotificacao) -> Notificacao:
        self.canais_pedidos.append(canal)
        return self._notificacao


def test_usa_o_canal_preferido_do_cliente(self) -> None:
    cliente = Cliente("João", "joao@email.com", telefone="+55 47 90000-0000",
                      canal_preferido=CanalNotificacao.SMS)
    self.servico.pedido_pago(self._pedido_pago(), cliente)
    assert self.criador_fake.canais_pedidos == [CanalNotificacao.SMS]
    assert self.espia.enviadas[0][0] == "+55 47 90000-0000"