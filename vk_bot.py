import vk_api, json
import Air_departure, Air_arrival, Train_departure, Train_arrival
from vk_api.longpoll import VkLongPoll, VkEventType

TOKEN = '8948f2017e31d91b51efab463b5212965653c2f6eebe988549964f0c7e4e11563509601fb54d7e0dca55f'

# Авторизуемся как сообщество
vk_session = vk_api.VkApi(token=TOKEN)
session_api = vk_session.get_api()
# Работа с сообщениями
longpoll = VkLongPoll(vk_session)

start = ['начать', 'привет', 'помощь', 'меню', 'start']


def sender(user_id, message, key):
    vk_session.method('messages.send', {'user_id': user_id, 'message': message, "random_id": 0, 'keyboard': key})


def get_but(text, color):
    return {
        'action':{
            'type': 'text',
            'payload': ['{\'button\': \'' + '1' + '\'}'],
            'label': f'{text}'
        },
        'color': f'{color}'
    }


m_keyboard = {
    'one_time': False,
    'buttons': [
        [get_but("Где поесть", "secondary"), get_but("Чат", "positive"), get_but("Пляжи", "secondary")],
        [get_but("Транспорт", "primary"), get_but("Справочник", "primary")]
    ]
}

m_keyboard = json.dumps(m_keyboard, ensure_ascii=False).encode('utf-8')
m_keyboard = str(m_keyboard.decode('utf-8'))

t_keyboard = {
    'one_time': False,
    'buttons': [
        [get_but("Аэропорт", "primary"), get_but("Вокзал", "primary")],
        [get_but("Такси", "positive")],
        [get_but("Меню", "secondary")]
    ]
}

t_keyboard = json.dumps(t_keyboard, ensure_ascii=False).encode('utf-8')
t_keyboard = str(t_keyboard.decode('utf-8'))

f_keyboard = {
    'one_time': False,
    'buttons': [
        [get_but("Вылет", "primary"), get_but("Прилет", "positive")],
        [get_but("Меню", "secondary")]
    ]
}

f_keyboard = json.dumps(f_keyboard, ensure_ascii=False).encode('utf-8')
f_keyboard = str(f_keyboard.decode('utf-8'))

tr_keyboard = {
    'one_time': False,
    'buttons': [
        [get_but("Отправление", "primary"), get_but("Прибытие", "positive")],
        [get_but("Меню", "secondary")]
    ]
}

tr_keyboard = json.dumps(tr_keyboard, ensure_ascii=False).encode('utf-8')
tr_keyboard = str(tr_keyboard.decode('utf-8'))


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg = event.text.lower()
            user_id = event.user_id
            print(user_id, event.text.lower())
            if msg in start:
                sender(user_id, 'Используй кнопки для получения информации', m_keyboard)
            elif msg == 'где поесть':
                sender(user_id, 'Держи ссылку на лучшие блюда Анапы &#128523; \nhttps://vk.cc/ayuXlz', m_keyboard)
            elif msg == 'чат':
                sender(user_id, 'Ссылка на чат &#128540; \nhttps://vk.cc/ayuXlz', m_keyboard)
            elif msg == 'пляжи':
                sender(user_id, 'Наши пляжи &#128525; \nhttps://vk.com/@anapatuta-plyazhi', m_keyboard)
            elif msg == 'справочник':
                sender(user_id, 'Держи скорее справочник! &#128563; \nhttps://vk.cc/c9XFv6', m_keyboard)
            elif msg == 'транспорт':
                sender(user_id, 'Что интересует?', t_keyboard)
            elif msg == 'погода':
                sender(user_id, ' ', m_keyboard)
            elif msg == 'аэропорт':
                sender(user_id, 'Вылет или прилет?', f_keyboard)
            elif msg == 'вылет':
                sender(user_id, 'Смотри...', m_keyboard)
                sender(user_id, Air_departure.departure(), m_keyboard)
            elif msg == 'прилет':
                sender(user_id, 'Секунду...', m_keyboard)
                sender(user_id, Air_arrival.arrival(), m_keyboard)
            elif msg == 'такси':
                sender(user_id, 'Номер телефона диспетчера для заказа Яндекс такси в Анапе: +7(86133)3-33-33.', m_keyboard)
            elif msg == 'вокзал':
                sender(user_id, 'Отправление или прибытие?', tr_keyboard)
            elif msg == 'отправление':
                sender(user_id, 'Смотри...', m_keyboard)
                sender(user_id, Train_departure.departure(), m_keyboard)
            elif msg == 'прибытие':
                sender(user_id, 'Секунду...', m_keyboard)
                sender(user_id, Train_arrival.arrival(), m_keyboard)

            elif msg == 'pass':
                sender(user_id, 'Скоро', m_keyboard)
