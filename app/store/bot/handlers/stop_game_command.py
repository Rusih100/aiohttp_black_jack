import typing

from app.store.bot.commands import BotCommands
from app.store.bot.router import Router
from app.store.vk_api.dataclasses import Message, Update

if typing.TYPE_CHECKING:
    from app.web.app import Application


router = Router()


@router.handler(commands=[BotCommands.STOP_GAME.value.command])
async def stop_game(update: "Update", app: "Application"):
    """
    Выводит результаты и останавливает игровую сессию
    """
    # TODO: Игру может отстановить только участник игры

    # TODO: Вывод результов игры
    await app.store.game.close_game(chat_id=update.object.message.peer_id)

    message = Message(
        peer_id=update.object.message.peer_id, text="Игра остановлена"
    )
    await app.store.vk_api.send_message(message=message)
