import random
from core.slot import Slot
from core.constants import PLAYER_COINS_INITIAL

slot_types = []
slot_types += [Slot(display="php", value=1.1)] * 10
slot_types += [Slot(display="java", value=1.2)] * 8
slot_types += [Slot(display="c#", value=1.3)] * 6
slot_types += [Slot(display="ruby", value=3)] * 5
slot_types += [Slot(display="c++", value=5)] * 3
slot_types += [Slot(display="javascript", value=8)] * 4
slot_types += [Slot(display="go", value=13)] * 3
slot_types += [Slot(display="cobol", value=17)] * 2
slot_types += [Slot(display="rust", value=30)]
slot_types += [Slot(display="assembly", value=40)]
slot_types += [Slot(display="kotlin", value=63)]
slot_types += [Slot(display="R", value=71)]
slot_types += [Slot(display="Haskel", value=80)]
slot_types += [Slot(display="pythonzinho", value=100)]


def random_slot():
    slot = random.choice(slot_types)
    return slot.copy(deep=True)


def reset_game(player, game):
    # game.logs = []
    player.coins = PLAYER_COINS_INITIAL
