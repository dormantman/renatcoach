import json
import traceback

from django.core import mail
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views import View

from project.settings import DEFAULT_FROM_EMAIL, DEFAULT_TO_EMAIL

DATA = dict(
    meta=dict(
        title='Renat Coach | Приходи на тренировку!',
        phone='+7 (912) 345-67-89',
        email='renat.coach@gmail.com',
        address_coords='[59.972366,30.301980]',
        address_city='Санкт-Петербург',
        address_location='Вяземский переулок, 5-7',
        address_coach_city='Санкт-Петербург',
        address_coach_location='улица Белорусская дом 6',

        meta_theme_color='#1790ff',
        meta_favicon='https://image.flaticon.com/icons/svg/2736/2736135.svg',
        meta_image='https://sun1-94.userapi.com/V6d4WDVKEb3PcVEaF-TPtzJfw7wU6-5JAnNAAQ/9FcFvvYuT08.jpg',
        meta_site_title='Renat Coach · Приходи на тренировку!',
        meta_site_description='Хочешь быть сильнее и активнее? Приходи на тренировку!'
    ),

    email_settings=dict(

    ),

    tariffs=[
        {
            'number': 1,
            'title': 'Одна тренировка в группе',
            'short': 'Тренировка в гр. · 600 р.',
            'warning': {
                'message': '<div class="price-warning">Популярный выбор <span '
                           'class="beauty-number">👑</span></div>',
                'color': '#1771F1',
            },
            'price': '<span>600</span> рублей',
            'image': 'https://image.flaticon.com/icons/svg/1530/1530833.svg',
            'button': 'Договориться',
            'url': '#mail'
        },
        {
            'number': 2,
            'title': 'Восемь тренировок в группе',
            'short': '8 трен. в гр. · 3500 р./мес',
            'price': '<span>3 500</span> рублей/мес',
            'image': 'https://image.flaticon.com/icons/svg/599/599928.svg',
            'button': 'Попробовать',
            'url': '#mail'
        },
        {
            'number': 3,
            'title': 'Персональная тренировка',
            'short': 'Персонал. тр. · 2 000 р.',
            'warning': {
                'message': '<div class="price-warning">Скидка <span class="beauty-number">15%</span></div>',
                'color': '#E20338',
            },
            'price': '<span>2 000</span> рублей',
            'image': 'https://image.flaticon.com/icons/svg/2734/2734214.svg',
            'button': 'Организовать',
            'url': '#mail'
        },
        {
            'number': 4,
            'title': 'Обучение мастерству!',
            'short': 'Обуч. маст. · 15 000 р.',
            'price': '<span>15 000</span> рублей',
            'image': 'https://image.flaticon.com/icons/svg/744/744984.svg',
            'button': 'Начать!',
            'url': '#mail'
        }
    ],
)


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html', {
            'tariffs': json.dumps(DATA['tariffs'], ensure_ascii=False),
            **DATA['meta']
        })


class MailView(View):
    def post(self, request):
        data = request.POST

        message = f'Не удалось отправить заявку!<br>Попробуйте позже<br>' \
                  f'или позвоните по номеру:<br>{DATA["meta"]["phone"]}'

        try:
            name = data['name']
            phone = data['phone']
            tariff_id = int(data['tariff'])
            tariffs = DATA['tariffs']

            if name and phone and tariff_id in range(1, len(tariffs) + 1):
                tariff = [element for element in tariffs if element['number'] == tariff_id][0]

                print(name, phone, tariff_id, tariff)

                connection = mail.get_connection()
                connection.open()

                message_body = render_to_string('email.html', context={
                    'title': tariff['title'],
                    'price': tariff['price'],
                    'name': name,
                    'phone': phone
                })

                email = mail.EmailMessage(
                    f'Заявка на запись от «{name}»',
                    message_body,
                    from_email=DEFAULT_FROM_EMAIL,
                    to=[DEFAULT_TO_EMAIL, ],
                    connection=connection,
                )

                email.content_subtype = "html"

                status = email.send()

                if status:
                    message = 'Заявка успешно отправлена!'

                connection.close()

        except (BaseException, Exception):
            traceback.print_exc()

        print(message)

        return render(request, 'index.html', {
            'message': f'<div class="backend-message">{message}</div',
            'tariffs': json.dumps(DATA['tariffs'], ensure_ascii=False),
            **DATA['meta']
        })
