from cat import Cat

your_cat = Cat('Димок', 'Сірий', 25, 9)

print('Привіт, це гра про котика.')

"""
your_cat = input('Дай ім`я своєму котику: ')
your_cat = input('Вибери колір шерсті котика: ')

Я хотіла зробити щоб user самостійно міг вибрати ім'я і колір, але як підключити ім'я і колір до about коли user вже вибрав не знаю :(
Знаю тільки, що треба такий код щоб вписати ім'я і колір. 
"""

print('Що ти зараз хочеш робити? ')
user_action = input('їсти, бігати, спати, прокинутись, дізнатись про кота ?: ')

if user_action == 'їсти':
   your_cat.feed()

elif user_action == 'бігати':
    your_cat.run()

if user_action == 'спати':
   your_cat.sleep()

elif user_action == 'дізнатись про кота':
    your_cat.about()

if user_action == 'прокинутись':
   your_cat.get_up()


user_action = input('Що далі будемо робити ?: ')

if user_action == 'їсти':
   your_cat.feed()

elif user_action == 'бігати':
    your_cat.run()

if user_action == 'спати':
   your_cat.sleep()

elif user_action == 'дізнатись про кота':
    your_cat.about()

if user_action == 'прокинутись':
   your_cat.get_up()


user_action = input('Що далі будемо робити ?: ')

if user_action == 'їсти':
   your_cat.feed()

elif user_action == 'бігати':
    your_cat.run()

if user_action == 'спати':
   your_cat.sleep()

elif user_action == 'дізнатись про кота':
    your_cat.about()

if user_action == 'прокинутись':
   your_cat.get_up()
