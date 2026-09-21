from ecommerce.criador_notificacao import CanalNotificacao

class Cliente:

    def __init__(self, nome, email, telefone: str = "",
                 canal_preferido: CanalNotificacao = CanalNotificacao.EMAIL) -> None:
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.canal_preferido = canal_preferido
        self.carrinho: "Carrinho | None" = None
        self._pedidos: list["Pedido"] = []


    @property
    def contato(self) -> str:
        if self.canal_preferido == CanalNotificacao.SMS:
            return self.telefone
        return self.email
    def pedidos(self) -> list["Pedido"]:
        return list(self._pedidos)
    def possui_carrinho(self) -> bool:
        return self.carrinho is not None

    def adicionar_pedido(self, pedido: "Pedido") -> None:
        self._pedidos.append(pedido)

    def finalizar_compra(self) -> "Pedido":
        if self.carrinho is None:
            raise ValueError("Cliente nao possui carrinho")
        if not self.carrinho.itens:
            raise ValueError("Carrinho vazio")
        pedido = self.carrinho.finalizar()
        self._pedidos.append(pedido)
        self.carrinho.esvaziar()
        return pedido



if __name__ == "__main__":  # 
    c = Cliente("João", "joao@email.com")
    print(f"Cliente: {c.nome}, Email: {c.email}")
    print(f"Possui carrinho: {c.possui_carrinho()}")