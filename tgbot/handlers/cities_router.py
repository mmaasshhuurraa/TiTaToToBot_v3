from aiogram import types, Router, F
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.utils.markdown import hcode

cities_router = Router()


@cities_router.message(F.text, state=None)
async def city_attempt(message: types.Message):
    cities = ['Винница',
              'Кропивницкий',
              'Полтава',
              'Харьков',
              'Днепр',
              'Луганск',
              'Ровно',
              'Херсон',
              'Донецк',
              'Луцк',
              'Симферополь',
              'Хмельницкий',
              'Житомир',
              'Львов',
              'Сумы',
              'Черкассы',
              'Запорожье',
              'Николаев',
              'Тернополь',
              'Чернигов',
              'Ивано-Франковск',
              'Одесса',
              'Ужгород',
              'Черновцы',
              'Киев'
              ]

    if message.text.casefold() in map(str.casefold, cities):
        await message.answer('Ура, есть такой город "'+message.text+'!!!"')
    else:
        await message.answer('Нет такого областного центра "'+message.text+'"')

    # text = [
    #     "Ехо без стану.",
    #     "Повідомлення:",
    #     message.text
    # ]

    # await message.answer('\n'.join(text))


# @cities_router.message(F.text)
# async def bot_echo_all(message: types.Message, state: FSMContext):
#     state_name = await state.get_state()
#     text = [
#         f'Ехо у стані {hcode(state_name)}',
#         'Зміст повідомлення:',
#         hcode(message.text)
#     ]
#     await message.answer('\n'.join(text))
