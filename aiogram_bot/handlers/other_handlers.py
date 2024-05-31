from aiogram import F, Router
from aiogram.types import Message, Update

router = Router()

@router.message()
async def nothing(message: Message):
    await message.answer('Я всего лишь простой бот калькулятор...')