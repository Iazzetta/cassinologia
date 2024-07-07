from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from core.game import Game
from core.player import Player
from core.bank import Bank
from core.utils import reset_game

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# game/player settings
bank = Bank(saldo=0)
new_game = Game(bank=bank, slots=[], bet_price=0, logs=[])
player = Player(coins=100_000, ganhos=0)


@app.get("/")
async def home(request: Request):
    new_game.girar_roleta()

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"slots": new_game.slots, "player": player, "bank": bank},
    )


@app.get("/reset-saldo")
async def reset_saldo(request: Request):
    reset_game(player, new_game)

    return {"saldo": player.coins}


@app.post("/girar")
async def girar_roleta(request: Request, bet_price: float = None):
    new_game.bet_price = bet_price
    response = new_game.girar_roleta(player)

    if response["status"] == "error":
        raise HTTPException(status_code=403, detail="Sem saldo")

    return templates.TemplateResponse(
        request=request,
        name="slot_desenho.html",
        context={
            "slots": new_game.slots,
            "results": response.get("results", []),
            "apenas_ganho": response.get("apenas_ganho", 0),
            "player": player,
            "logs": new_game.logs,
            "bank": bank,
        },
    )
