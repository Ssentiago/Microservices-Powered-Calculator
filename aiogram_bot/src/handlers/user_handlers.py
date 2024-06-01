import logging
import os
import re
import sys


from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from inline_keyboard.keyboard import keyboard as inl_keyboard
from service.service import api_calculate



logger = logging.getLogger(__name__)
router = Router()


@router.message(Command(commands = ['start']))
async def start_command(message: Message):
    await message.answer(text = '0', reply_markup = inl_keyboard)


@router.callback_query(F.data == 'С')
async def process_C(callback: CallbackQuery):
    await callback.message.edit_text(
        text = '0',
        reply_markup = inl_keyboard
    )


@router.callback_query(F.data.in_('÷+×-'))
async def add_sym(callback: CallbackQuery):
    if callback.message.text != '0':
        if callback.message.text[-1] not in "÷+×-":
            await callback.message.edit_text(
                text = callback.message.text + callback.data,
                reply_markup = inl_keyboard)
    await callback.answer()


@router.callback_query(F.data.in_('0123456789.'))
async def add_other_sym(callback: CallbackQuery):
    text = callback.message.text
    if callback.data in "0123456789":
        if callback.message.text != '0':
            text += callback.data
        else:
            text = callback.data
    else:
        if callback.message.text != '0':
            check = re.split(r'÷+×-', callback.message.text)[-1]
            if re.fullmatch(r"\d+", check):
                text += callback.data

    if text != callback.message.text:
        await callback.message.edit_text(
            text = text,
            reply_markup = inl_keyboard
        )
    await callback.answer()


@router.callback_query(F.data == '⌫')
async def del_sym(callback: CallbackQuery):
    if callback.message.text == "0":
        await callback.answer()
    else:
        if len(callback.message.text) == 1:
            await  callback.message.edit_text(text = '0', reply_markup = inl_keyboard)
        else:
            await callback.message.edit_text(text = callback.message.text[:-1], reply_markup = inl_keyboard)


@router.callback_query(F.data == '=')
async def caclculate(callback: CallbackQuery):
    if callback.message.text != "0":
        if "=" not in callback.message.text:
            res = await api_calculate(callback.message.text)
            if res:
                await  callback.message.edit_text(
                    text = callback.message.text + '=' + res,
                    reply_markup = inl_keyboard
                )
            else:
                await callback.answer("Что-то пошло не так... попробуйте повторить попытку позднее")
        else:
            await  callback.message.edit_text(text = "0", reply_markup = inl_keyboard)
    else:
        await  callback.answer()
