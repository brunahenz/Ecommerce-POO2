from enum import Enum

class FormaPagamento(Enum):
    PIX = "pix"
    CARTAO_CREDITO = "cartao_credito"
    BOLETO = "boleto"
