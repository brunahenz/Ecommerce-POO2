from enum import Enum

class SituacaoPagamento(Enum):
    PENDENTE = 'pendente'
    CONFIRMADO = 'confirmado'
    RECUSADO =  'recusado'