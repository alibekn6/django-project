from django.http import HttpResponse
from django.shortcuts import render


goods = [
            {'image': 'deps/images/goods/set of tea table and three chairs.jpg',
            'name': 'Чайный столик и три стула',
            'description': 'Комплект из трёх стульев и дизайнерский столик для гостинной комнаты.',
            'price': 150.00,
            'id': 1234
            },

            {'image': 'deps/images/goods/set of tea table and two chairs.jpg',
            'name': 'Чайный столик и два стула',
            'description': 'Набор из стола и двух стульев в минималистическом стиле.',
            'price': 93.00,
            'id': 7182
            },

            {'image': 'deps/images/goods/double bed.jpg',
            'name': 'Двухспальная кровать',
            'description': 'Кровать двухспальная с надголовником и вообще очень ортопедичная.',
            'price': 670.00,
            'id': 1748
            },

            {'image': 'deps/images/goods/kitchen table.jpg',
            'name': 'Кухонный стол с раковиной',
            'description': 'Кухонный стол для обеда с встроенной раковиной и стульями.',
            'price': 365.00,
            'id': 1934
            },

            {'image': 'deps/images/goods/kitchen table 2.jpg',
            'name': 'Кухонный стол с встройкой',
            'description': 'Кухонный стол со встроенной плитой и раковиной. Много полок и вообще красивый.',
            'price': 430.00,
            'id': 8216
            },

            {'image': 'deps/images/goods/corner sofa.jpg',
            'name': 'Угловой диван для гостинной',
            'description': 'Угловой диван, раскладывается в двухспальную кровать, для гостинной и приема гостей самое то!',
            'price': 610.00,
            'id': 3719
            },

            {'image': 'deps/images/goods/bedside table.jpg',
            'name': 'Прикроватный столик',
            'description': 'Прикроватный столик с двумя выдвижными ящиками (цветок не входит в комплект).',
            'price': 55.00,
            'id': 3718
            },

            {'image': 'deps/images/goods/sofa.jpg',
            'name': 'Диван обыкновенный',
            'description': 'Диван, он же софа обыкновенная, ничего примечательного для описания.',
            'price': 190.00,
            'id': 4831
            },

            {'image': 'deps/images/goods/office chair.jpg',
            'name': 'Стул офисный',
            'description': 'Описание товара, про то какой он классный, но это стул, что тут сказать...',
            'price': 30.00,
            'id': 2443
            },

            {'image': 'deps/images/goods/plants.jpg',
            'name': 'Растение',
            'description': 'Растение для украшения вашего интерьера подарит свежесть и безмятежность обстановке.',
            'price': 10.00,
            'id': 4892
            },

            {'image': 'deps/images/goods/flower.jpg',
            'name': 'Цветок стилизированный',
            'description': 'Дизайнерский цветок (возможно искусственный) для украшения интерьера.',
            'price': 15.00,
            'id': 9910
            },

            {'image': 'deps/images/goods/strange table.jpg',
            'name': 'Прикроватный столикb',
            'description': 'Столик, довольно странный на вид, но подходит для размещения рядом с кроватью.',
            'price': 25.00,
            'id': 8212
            },
        ]

def catalog(request):
    context = {
        'title': "Home - Каталог",
        'goods': goods
    }
    return render(request, 'goods/catalog.html', context)



def product(request, product_id):
    for i in goods:
        if i["id"] == product_id:
            goods_detail = i

    context = {
        'goods': goods_detail
    }
    return render(request, 'goods/product.html', context)


