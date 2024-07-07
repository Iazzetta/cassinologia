from dataclasses import dataclass
from core.constants import BANCO_PREMIO_PORCENTAGEM


@dataclass
class Bank:
    saldo: float

    def saldo_para_premio(self):
        return self.saldo * BANCO_PREMIO_PORCENTAGEM

    def pagar_banco(self, value: float):
        self.saldo += value
