from fastapi import APIRouter

from neiro import Neiro

router = APIRouter()

detect = Neiro()


@router.post('/detection_message/')
async def detection(messages: str):
    '''Дэтекция токсичных сообщений;
    На вход: сообщение;
    Выход: 2 варианта:
    1) neutral - нейтральное сообщение,
    2) toxic - токсичное сообщение
    '''
    return detect.predict(messages)