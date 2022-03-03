from typing import Union

from aiogram import types

from frontend.keyboards.inline.settings_keyboards import experience_keyboard, language_keyboard,\
                                                         save_keyboard, settings_keyboard


async def ask_for_settings(message: types.Message):
    await settings_menu(message=message)


async def settings_menu(message: Union[types.Message, types.CallbackQuery], **kwargs):

    markup = await settings_keyboard()

    if isinstance(message, types.Message):
        await message.answer('Lets make your settings', reply_markup=markup)

    elif isinstance(message, types.CallbackQuery):
        call = message
        await call.message.edit_reply_markup(markup)


async def experience_menu(message: types.CallbackQuery, **kwargs):

    markup = await experience_keyboard()

    call = message
    await call.message.edit_reply_markup(markup)


async def language_menu(message: types.CallbackQuery, **kwargs):

    markup = await language_keyboard()

    call = message
    await call.message.edit_reply_markup(markup)


async def save_menu(message: types.CallbackQuery, **kwargs):

    markup = await save_keyboard()

    call = message
    await call.message.edit_reply_markup(markup)


async def navigate(call: types.CallbackQuery, callback_data: dict):

    current_level = callback_data.get('level')

    levels = {
        '1': ask_for_settings,
        '2': experience_menu,
        '3': language_menu,
        '4': save_menu,
    }
    current_level_func = levels[current_level]

    await current_level_func(call)