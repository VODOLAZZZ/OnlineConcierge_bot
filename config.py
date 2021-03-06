from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from aiogram.dispatcher.filters.state import State, StatesGroup

TOKEN = '2096892030:AAGczC-gxnMIFbKFymQIvOr2x9R2QqywrZ0'


class OrderFood(StatesGroup):
    waiting_for_room_name = State()


class RoomCleaning(StatesGroup):
    waiting_for_room_name = State()


start_message = 'Привет, {0}, чем я могу вам помочь? Если вы хотите заказать еду, нажмите кнопку "Заказ еды". ' \
                'Если хотите, чтобы убрали в комнате, нажмите "Уборка комнаты". '

main_menu_message = start_message
main_menu_buttons = ['Заказ еды', 'Уборка номера']
main_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(*main_menu_buttons)

ordering_food_message = 'Выберете и нажмите на одну из кнопок снизу.'
ordering_food_callback_data = CallbackData('ordering_food', 'button_name')
ordering_food_inline_buttons = [
    InlineKeyboardButton('Холодные закуски', callback_data=ordering_food_callback_data.new(button_name='0')),
    InlineKeyboardButton('Первые блюда', callback_data=ordering_food_callback_data.new(button_name='1')),
    InlineKeyboardButton('Вторые блюда', callback_data=ordering_food_callback_data.new(button_name='2')),
    InlineKeyboardButton('Напитки', callback_data=ordering_food_callback_data.new(button_name='3')),
    InlineKeyboardButton('Сформировать заказ',
                         callback_data=ordering_food_callback_data.new(button_name='form_an_order')),
    InlineKeyboardButton('Назад',
                         callback_data=ordering_food_callback_data.new(button_name='back_to_main_menu'))
]
ordering_food_inline_keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1).add(
    *ordering_food_inline_buttons)

ordering_food_inline_button_back_to_category_menu = InlineKeyboardButton('Назад',
                                                                         callback_data=ordering_food_callback_data.new(
                                                                             button_name='back_to_category_menu'))

ordering_food_category_callback_data = CallbackData('ordering_food_category', 'category', 'id', 'food_name')
ordering_food_message_c0 = 'ХОЛОДНЫЕ ЗАКУСКИ'
ordering_food_inline_buttons_c0 = [
    InlineKeyboardButton('Яйцо вареное 1/070 12-00',
                         callback_data=ordering_food_category_callback_data.new(category='0', id='0',
                                                                                food_name='Яйцо вареное')),
    InlineKeyboardButton('Творог со сметаной 1/100 50-00',
                         callback_data=ordering_food_category_callback_data.new(category='0', id='1',
                                                                                food_name='Творог со сметаной')),
    InlineKeyboardButton('Сырники 1/070 60-00',
                         callback_data=ordering_food_category_callback_data.new(category='0', id='2',
                                                                                food_name='Сырники')),
]
ordering_food_inline_keyboard_c0 = InlineKeyboardMarkup(resize_keyboard=True, row_width=1).add(
    *ordering_food_inline_buttons_c0).add(ordering_food_inline_button_back_to_category_menu)

ordering_food_message_c1 = 'ПЕРВЫЕ БЛЮДА'
ordering_food_inline_buttons_c1 = [
    InlineKeyboardButton('Борщ красный 1/300 50-00',
                         callback_data=ordering_food_category_callback_data.new(category='1', id='0',
                                                                                food_name='Борщ красный')),
    InlineKeyboardButton('Борщ зеленый 1/301 50-00',
                         callback_data=ordering_food_category_callback_data.new(category='1', id='1',
                                                                                food_name='Борщ зеленый')),
    InlineKeyboardButton('Рассольник 1/300 60-00',
                         callback_data=ordering_food_category_callback_data.new(category='1', id='2',
                                                                                food_name='Рассольник')),
]
ordering_food_inline_keyboard_c1 = InlineKeyboardMarkup(resize_keyboard=True, row_width=1).add(
    *ordering_food_inline_buttons_c1).add(ordering_food_inline_button_back_to_category_menu)

ordering_food_message_c2 = 'ВТОРЫЕ БЛЮДА'
ordering_food_inline_buttons_c2 = [
    InlineKeyboardButton('Солянка по-грузински 1/300 200-00',
                         callback_data=ordering_food_category_callback_data.new(category='2', id='0',
                                                                                food_name='Солянка')),
    InlineKeyboardButton('Гуляш /говядина/ 1/100 100-00',
                         callback_data=ordering_food_category_callback_data.new(category='2', id='1',
                                                                                food_name='Гуляш говядина')),
    InlineKeyboardButton('Филе рыбы Зубатка 1/100 60-00',
                         callback_data=ordering_food_category_callback_data.new(category='2', id='2',
                                                                                food_name='Филе рыбы Зубатка')),
]
ordering_food_inline_keyboard_c2 = InlineKeyboardMarkup(resize_keyboard=True, row_width=1).add(
    *ordering_food_inline_buttons_c2).add(ordering_food_inline_button_back_to_category_menu)

ordering_food_message_c3 = 'НАПИТКИ'
ordering_food_inline_buttons_c3 = [
    InlineKeyboardButton('Вода 50-00',
                         callback_data=ordering_food_category_callback_data.new(category='3', id='0',
                                                                                food_name='Вода')),
    InlineKeyboardButton('Сок Яблочный 100-00',
                         callback_data=ordering_food_category_callback_data.new(category='3', id='1',
                                                                                food_name='Сок Яблочный')),
    InlineKeyboardButton('Сок Апельсиновый 100-00',
                         callback_data=ordering_food_category_callback_data.new(category='3', id='2',
                                                                                food_name='Сок Апельсиновый')),
    InlineKeyboardButton('Сок Вишневый 100-00',
                         callback_data=ordering_food_category_callback_data.new(category='3', id='3',
                                                                                food_name='Сок Вишневый')),
    InlineKeyboardButton('Кофе 80-00',
                         callback_data=ordering_food_category_callback_data.new(category='3', id='4',
                                                                                food_name='Кофе')),
    InlineKeyboardButton('Чай 60-00',
                         callback_data=ordering_food_category_callback_data.new(category='3', id='5',
                                                                                food_name='Чай')),
]
ordering_food_inline_keyboard_c3 = InlineKeyboardMarkup(resize_keyboard=True, row_width=1).add(
    *ordering_food_inline_buttons_c3).add(ordering_food_inline_button_back_to_category_menu)

ordering_food_inline_keyboard_c_text = '''ХОЛОДНЫЕ ЗАКУСКИ
Яйцо вареное 1/070 12-00
Творог со сметаной 1/100 50-00
Сырники 1/070 60-00

ПЕРВЫЕ БЛЮДА
Борщ красный 1/300 50-00
Борщ зеленый 1/301 50-00
Рассольник 1/300 60-00

ВТОРЫЕ БЛЮДА
Солянка по-грузински 1/300 200-00
Гуляш /говядина/ 1/100 100-00
Филе рыбы Зубатка 1/100 60-00

НАПИТКИ
Вода 50-00
Сок Яблочный 100-00
Сок Апельсиновый 100-00
Сок Вишневый 100-00
Кофе 80-00
Чай 60-00'''

ordering_food_inline_keyboard_c_text_list = [i.split('\n') for i in ordering_food_inline_keyboard_c_text.split('\n\n')]

# 476343978
# 616343618

ordering_food_form_an_order_message = 'Ваш заказ {0}, будет доставлен в номер {1}, в течение часа.'
ordering_food_form_an_order_inline_keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1).add(
    ordering_food_inline_buttons[-1])

room_cleaning_callback_data = CallbackData('room_cleaning', 'button_name')
room_cleaning_message = 'Уборка номера'
room_cleaning_inline_message = 'Нажмите на кнопку "Заказать" чтобы заказать уборку'
room_cleaning_inline_buttons = [
    InlineKeyboardButton('Заказать', callback_data=room_cleaning_callback_data.new(button_name='order'))]
room_cleaning_inline_keyboard = InlineKeyboardMarkup(resize_keyboard=True).add(*room_cleaning_inline_buttons).add(
    ordering_food_inline_buttons[-1])
room_cleaning_message_form = 'К вам в номер {0}, придет уборщик в течении часа'
