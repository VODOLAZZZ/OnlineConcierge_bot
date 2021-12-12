import config as cg
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor
from typing import Union
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token=cg.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
cart = {}
orders = []


async def edit_ordering_food_inline_keyboard(card: list):
    buttons_list = cg.ordering_food_inline_keyboard_c_text_list
    finale_list = []


@dp.message_handler(commands='id')
async def start(message: types.Message, state: FSMContext):
    print(message.from_user.id)
    await message.answer(f'Ваш айди:{message.from_user.id}')


@dp.message_handler(commands='start', state='*')
async def start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(cg.start_message.format(message.chat.first_name), reply_markup=cg.main_menu_keyboard)


@dp.callback_query_handler(cg.ordering_food_callback_data.filter(button_name='back_to_main_menu'))
async def main_menu(cam: Union[types.CallbackQuery, types.Message]):
    if type(cam) == types.CallbackQuery:
        await cam.message.edit_reply_markup()
        await cam.message.answer(cg.main_menu_message.format(cam.from_user.first_name),
                                 reply_markup=cg.main_menu_keyboard)
    elif type(cam) == types.Message:
        await cam.answer(cg.start_message.format(cam.chat.first_name), reply_markup=cg.main_menu_keyboard)


@dp.callback_query_handler(cg.ordering_food_callback_data.filter(button_name='back_to_category_menu'))
@dp.message_handler(Text(equals=cg.main_menu_buttons[0]))
async def ordering_food(cam: Union[types.CallbackQuery, types.Message]):
    if type(cam) == types.Message:
        await cam.answer('Что будете заказывать?', reply_markup=cg.ReplyKeyboardRemove())
        await cam.answer(cg.ordering_food_message, reply_markup=cg.ordering_food_inline_keyboard)
    elif type(cam) == types.CallbackQuery:
        await cam.message.edit_text(cg.ordering_food_message, reply_markup=cg.ordering_food_inline_keyboard)
        await cam.answer()


@dp.callback_query_handler(cg.ordering_food_callback_data.filter(button_name=['0', '1', '2', '3']))
async def ordering_food_category(call: types.CallbackQuery, callback_data: dict):
    category = callback_data['button_name']
    if category == '0':
        await call.message.edit_text(cg.ordering_food_message_c0, reply_markup=cg.ordering_food_inline_keyboard_c0)
    elif category == '1':
        await call.message.edit_text(cg.ordering_food_message_c1, reply_markup=cg.ordering_food_inline_keyboard_c1)
    elif category == '2':
        await call.message.edit_text(cg.ordering_food_message_c2, reply_markup=cg.ordering_food_inline_keyboard_c2)
    elif category == '3':
        await call.message.edit_text(cg.ordering_food_message_c3, reply_markup=cg.ordering_food_inline_keyboard_c3)
    await call.answer()


@dp.callback_query_handler(cg.ordering_food_category_callback_data.filter())
async def ordering_food_add_food(call: types.CallbackQuery, callback_data: dict):
    food_id = callback_data['category'] + callback_data['id']
    cart[call.from_user.id] = cart.get(call.from_user.id, [])
    cart[call.from_user.id] += [food_id]
    await call.answer()


@dp.callback_query_handler(cg.ordering_food_callback_data.filter(button_name=['form_an_order']))
async def ordering_food_form_an_order_enter_room(call: types.CallbackQuery):
    cart[call.from_user.id] = cart.get(call.from_user.id, [])
    if cart[call.from_user.id]:
        await call.message.edit_text('Введите номер в который принесут заказ')
        await cg.OrderFood.waiting_for_room_name.set()
        await call.answer()
    else:
        await call.answer('Вы ничего не добавили в корзину', show_alert=True)


@dp.message_handler(state=cg.OrderFood.waiting_for_room_name)
async def ordering_food_enter_room_name(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Вы неправильно указали номер, пожалуйста введите только цифры')
    else:
        await state.finish()
        room = message.text
        user_id = message.from_user.id
        cart[user_id] = cart.get(user_id, [])
        number = len(orders) + 1
        orders.append({room: cart[user_id]})
        await bot.send_message(367134589,
                               f'Ты типо повар, к тебе тут заказ прилетел: №{number} в номер {room} ({", ".join(orders[-1][room])})')
        await message.answer(cg.ordering_food_form_an_order_message.format(number, room),
                             reply_markup=cg.ordering_food_form_an_order_inline_keyboard)
        cart[user_id] = []


@dp.message_handler(Text(equals=cg.main_menu_buttons[1]))
async def room_cleaning(message: types.Message):
    await message.answer(cg.room_cleaning_message, reply_markup=cg.ReplyKeyboardRemove())
    await message.answer(cg.room_cleaning_inline_message, reply_markup=cg.room_cleaning_inline_keyboard)


@dp.callback_query_handler(cg.room_cleaning_callback_data.filter(button_name='order'))
async def room_cleaning_accept(call: types.CallbackQuery):
    await call.message.edit_text('Введите номер в котором надо убраться')
    await cg.RoomCleaning.waiting_for_room_name.set()
    await call.answer()


@dp.message_handler(state=cg.RoomCleaning.waiting_for_room_name)
async def room_cleaning_enter_the_room_name(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Вы неправильно указали номер, пожалуйста введите только цифры')
    else:
        await state.finish()
        room = message.text
        number = len(orders) + 1
        orders.append({room: 'clean'})
        await bot.send_message(476343978,
                               f'Ты типо уборщик, к тебе тут заказ прилетел: №{number} в номер {room}')
        await message.answer(cg.room_cleaning_message_form.format(room),
                             reply_markup=cg.ordering_food_form_an_order_inline_keyboard)


async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == '__main__':
    executor.start_polling(dp, on_shutdown=shutdown)
