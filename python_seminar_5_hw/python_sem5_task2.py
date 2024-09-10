# Задача 2. Глубокое копирование
# Вы сделали для заказчика структуру сайта по продаже телефонов:
# site = {
# 'html': {
# 'head': {
# 'title': 'Куплю/продам телефон недорого'
# },
# 'body': {
# 'h2': 'У нас самая низкая цена на iPhone',
# 'div': 'Купить',
# 'p': ‘Продать'
# }
# }
# }
# Заказчик рассказал своим коллегам на рынке, и они захотели такой же сайт для
# своих товаров. Вы посчитали, что это лёгкая задача, и быстро принялись за
# работу.
# Напишите программу, которая запрашивает у клиента количество сайтов, затем
# названия продуктов, а после каждого запроса выводит на экран активные
# сайты.
# Условия:
# ● учтите, что функция должна уметь работать с разными сайтами (иначе
# вам придётся переделывать программу под каждого заказчика заново);
# ● вы должны получить список, хранящий сайты для разных продуктов (а
# значит, для каждого продукта нужно будет первым делом выполнить
# глубокое копирование сайта).
# Пример вывода
# Сколько сайтов: 2
# Введите название продукта для нового сайта: iPhone
# Сайт для iPhone:
# site = {
# 'html': {
# 'head': {
# 'title': 'Куплю/продам iPhone недорого'
# },
# 'body': {
# 'h2': 'У нас самая низкая цена на iPhone',
# 'div': 'Купить',
# 'p': ‘Продать'
# }
# }
# }
# Введите название продукта для нового сайта: Samsung
# Сайт для iPhone:
# site = {
# 'html': {
# 'head': {
# 'title': 'Куплю/продам iPhone недорого'
# },
# 'body': {
# 'h2': 'У нас самая низкая цена на iPhone',
# 'div': 'Купить',
# 'p': ‘Продать'
# }
# }
# }
# Сайт для Samsung:
# site = {
# 'html': {
# 'head': {
# 'title': 'Куплю/продам Samsung недорого'
# },
# 'body': {
# 'h2': 'У нас самая низкая цена на Samsung',
# 'div': 'Купить',
# 'p': ‘Продать'
# }
# }
# }
# Обратите внимание, что на первой итерации выводится только один сайт (для
# iPhone), а на второй итерации — оба сайта (и для iPhone и для Samsung).
# Чтобы это реализовать, нужно сохранять сайты в списке и каждый раз печатать
# все его элементы.


# С такой функцией не заменяются наименования продуктов:
# def make_site(site_struct:dict, product:str) -> dict:
#     for key, value in site_struct.items():
#         if key == 'title':
#             value = f'Куплю/продам {product} недорого'
#         elif key == 'h2':
#             value = f'У нас самая низкая цена на {product}'
#         elif type(value) is dict:
#             value = make_site(value, product)
#     return site_struct

import copy

def make_site(site_struct:dict, product:str) -> dict:
    for key, value in site_struct.items():
        if key == 'title':
            site_struct[key] = value.replace('телефон', product)
        elif key == 'h2':
            site_struct[key] = value.replace('iPhone', product)
        elif type(value) is dict:
            value = make_site(value, product)
    return site_struct

site = {'html': {'head': {'title': 'Куплю/продам телефон недорого'},
                 'body': {'h2': 'У нас самая низкая цена на iPhone',
                          'div': 'Купить',
                          'p': 'Продать'}
                }
        }

sites_count = int(input('Введите количество необходимых сайтов: '))

site_list = []

while sites_count > 0:
    site_product = input('Введите название продукта: ')
    site_struct = copy.deepcopy(site)
    site_list.append(make_site(site_struct, site_product))
    sites_count -= 1

print(site_list)