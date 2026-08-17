from datetime import date


class Pagamento:

    def __init__(self, pedido: "Pedido", valor: float) -> None:
        if valor <= 0:
            raise ValueError("Valor do pagamento deve ser positivo")
        self._pedido = pedido
        self._valor = valor
        self._data = date.today()
        self._confirmado = False

    @property
    def pedido(self) -> "Pedido":
        return self._pedido

    @property
    def valor(self) -> float:
        return self._valor

    @property
    def data(self) -> date:
        return self._data

    @property
    def confirmado(self) -> bool:
        return self._confirmado

    def confirmar(self) -> None:
        if self._confirmado:
            raise ValueError("Pagamento ja foi confirmado")
        self._confirmado = True