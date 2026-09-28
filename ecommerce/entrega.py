from abc import ABC, abstractmethod


class Entrega(ABC):
    def __init__(self, pedido: "Pedido", codigo_rastreio: str) -> None:
        self._pedido = pedido
        self._codigo_rastreio = codigo_rastreio

    @property
    def modalidade(self) -> str:
        return self._modalidade

    @property
    def codigo_rastreio(self) -> str:
        return self._codigo_rastreio

    @abstractmethod
    def prazo_estimado(self) -> int:
        """Numero de dias uteis previstos ate a entrega."""
        ...

    def etiqueta(self) -> str:
        return (
            f"{type(self).__name__} | rastreio {self._codigo_rastreio} "
            f"| prazo {self.prazo_estimado()} dias uteis"
        )


class EntregaCorreios(Entrega):
    def __init__(self, pedido, codigo_rastreio: str, modalidade: str = "PAC") -> None:
        super().__init__(pedido, codigo_rastreio)
        self._modalidade = modalidade

    def prazo_estimado(self) -> int:
        return 3 if self._modalidade == "SEDEX" else 8


class EntregaTransportadora(Entrega):
    def __init__(self, pedido, codigo_rastreio: str, transportadora: str) -> None:
        super().__init__(pedido, codigo_rastreio)
        self._transportadora = transportadora

    def prazo_estimado(self) -> int:
        return 5


class CriadorEntrega:
    def criar(self, origem: str, pedido) -> Entrega:
        if origem == "loja_central":
            return EntregaCorreios(pedido, gerar_codigo(), modalidade="SEDEX")
        elif origem == "centro_sul":
            return EntregaTransportadora(
                pedido, gerar_codigo(), transportadora="Transportadora Sul"
            )
        elif origem == "marketplace":
            ...  # regra do parceiro
