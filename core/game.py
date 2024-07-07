from dataclasses import dataclass
from typing import List
from core.utils import random_slot
from core.slot import Slot
from core.player import Player
from core.bank import Bank


@dataclass
class Game:
    bank: Bank
    slots: List[List[Slot]]
    bet_price: float
    logs: List[str]

    def girar_roleta(self, player: Player = None):
        self.slots = [
            [random_slot(), random_slot(), random_slot()],
            [random_slot(), random_slot(), random_slot()],
            [random_slot(), random_slot(), random_slot()],
        ]

        results = self.verificar()
        novo_coins = 0
        if player:
            if player.coins < self.bet_price:
                return {"status": "error"}

            player.coins -= self.bet_price
            self.bank.pagar_banco(self.bet_price)

            results = self.verificar()

            # verificar bank
            saldo_disponivel = self.bank.saldo_para_premio()
            print("Saldo disponivel bank: ", saldo_disponivel)
            total_ganhos, log_message = self.calcular_ganhos(results, self.bet_price)
            novo_coins = round(self.bet_price * total_ganhos, 2)

            if saldo_disponivel < novo_coins:
                print("loop saldo_disponivel < novo_coins ")
                while novo_coins > 0:
                    self.slots = [
                        [random_slot(), random_slot(), random_slot()],
                        [random_slot(), random_slot(), random_slot()],
                        [random_slot(), random_slot(), random_slot()],
                    ]
                    results = self.verificar()
                    total_ganhos, log_message = self.calcular_ganhos(
                        results, self.bet_price
                    )
                    novo_coins = round(self.bet_price * total_ganhos, 2)
                    print("loop", novo_coins)

            if total_ganhos > 0:
                self.logs.append(log_message)

            player.coins += novo_coins
            player.add_ganho(novo_coins)

        return {
            "status": "success",
            "results": results,
            "apenas_ganho": novo_coins,
        }

    def calcular_ganhos(self, results: List[str], bet_price: float):
        total = 0
        log_message = ""
        for r in results:
            total += r.value
            log_message += f"- {r.display} (x{r.value})<br/>"
        if total > 0:
            log_message += f"Total: R$ {round(bet_price * total, 2)}"
        return (total, log_message)

    def verificar(self):
        list_results = []

        # verificar horizontais
        count_horizontal = 0
        for l in self.slots:
            if l[0].display == l[1].display and l[0].display == l[2].display:
                list_results.append(l[0])
                l[0].fill = True
                l[1].fill = True
                l[2].fill = True
            count_horizontal += 1

        # verificar diagonal top bottom
        count_diagonal = 0
        dlist = []
        for l in self.slots:
            dlist.append(l[count_diagonal])
            count_diagonal += 1

        if (
            dlist[0].display == dlist[1].display
            and dlist[0].display == dlist[2].display
        ):
            list_results.append(dlist[0])
            dlist[0].fill = True
            dlist[1].fill = True
            dlist[2].fill = True

        # verificar diagonal bottom top
        count_diagonal = 2
        dlist = []
        for l in self.slots:
            dlist.append(l[count_diagonal])
            count_diagonal -= 1

        if (
            dlist[0].display == dlist[1].display
            and dlist[0].display == dlist[2].display
        ):
            list_results.append(dlist[0])
            dlist[0].fill = True
            dlist[1].fill = True
            dlist[2].fill = True

        return list_results
