import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = 'TOKEN'
bot = telebot.TeleBot(TOKEN)
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

keyboard.add(KeyboardButton('C++'))
keyboard.add(KeyboardButton('Pascal'))
keyboard.add(KeyboardButton('C#'))
keyboard.add(KeyboardButton('Python'))
keyboard.add(KeyboardButton('Java'))
keyboard.add(KeyboardButton('JavaScript'))
keyboard.add(KeyboardButton('Basic'))
keyboard.add(KeyboardButton('О проекте'))


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     "Я бот, который может расказать о языках программирования!",
                     reply_markup=keyboard)


# C++

@bot.message_handler(regexp='C++')
def history_C1(message):
    keyboard_1 = ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard_1.add(KeyboardButton('История'))
    keyboard_1.add(KeyboardButton('Что такое?'))
    keyboard_1.add(KeyboardButton('Для чего?'))
    keyboard_1.add(KeyboardButton('Файлы'))
    keyboard_1.add(KeyboardButton('Другие языки'))
    bot.send_message(message.chat.id,
                     'О чем хотите узнать?',
                     reply_markup=keyboard_1)

    @bot.message_handler(regexp='История')
    def history(message):
        text = ('История C++ начинается в 1979 году, когда Бьерн Страуструп, создатель этого языка программирования, '
                'впервые начал работу над языком, который тогда был известен как «С c классами» (C with Classes). '
                'Изначально язык разрабатывался, как новая улучшенная версия языка программирования C с добавлением '
                'дополнительных фич, которые сделали его объектно-ориентированным. В 1998 году C++ был официально '
                'стандартизирован и стал надежной рабочей лошадкой. К этому моменту C++ был одним из наиболее часто '
                'используемых языков программирования во всем мире и сохраняет эту позицию по сей день.')
        bot.send_message(message.chat.id,
                         text)

    @bot.message_handler(regexp='Что такое?')
    def what_is(message):
        text = ('C++ компилируемый язык программирования общего назначения, сочетает свойства как высокоуровневых, '
                'так и низкоуровневых языков программирования. В сравнении с его предшественником, '
                'языком программирования Cи, наибольшее внимание уделено поддержке объектно-ориентированного и '
                'обобщённого программирования. Название «язык программирования C++» происходит от языка '
                'программирования'
                'C, в котором унарный оператор ++ обозначает инкремент переменной.')
        bot.send_message(message.chat.id,
                         text)

    @bot.message_handler(regexp='Для чего?')
    def for_what(message):
        text = ('C++ используют для создания программного обеспечения разного рода: от игр до операционных систем. '
                'Этот язык также широко применяется в интенсивной обработке данных и научных расчётах.')
        bot.send_message(message.chat.id,
                         text)

    @bot.message_handler(regexp='Файлы')
    def file(message):
        text = '.cpp или .cxx'
        bot.send_message(message.chat.id,
                         text)

    @bot.message_handler(regexp='Другие языки')
    def another(message):
        bot.send_message(message.chat.id,
                         'Выберайте',
                         reply_markup=keyboard)


# Pascal

@bot.message_handler(regexp='Pascal')
def history_Pascal(message):
    keyboard_1 = ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard_1.add(KeyboardButton('История'))
    keyboard_1.add(KeyboardButton('Что такое?'))
    keyboard_1.add(KeyboardButton('Для чего?'))
    keyboard_1.add(KeyboardButton('Файлы'))
    keyboard_1.add(KeyboardButton('Другие языки'))
    bot.send_message(message.chat.id,
                     'О чем хотите узнать?',
                     reply_markup=keyboard_1)

    @bot.message_handler(regexp='История')
    def history(message):
        text = ('Язык был создан Никлаусом Виртом в 1968—1969 годах после его участия в работе комитета разработки '
                'стандарта языка Алгол-68. Язык назван в честь французского математика, физика, литератора и философа '
                'Блеза Паскаля, который создал одну из первых в мире механических машин, складывающую два числа.')
        bot.send_message(message.chat.id,
                         text)

    @bot.message_handler(regexp='Что такое?')
    def what_is(message):
        text = ('Pascal — это универсальный язык программирования, отличающийся строгой структурой и типизацией '
                'переменных, а также интуитивно понятным синтаксисом.')
        bot.send_message(message.chat.id,
                         text)

    @bot.message_handler(regexp='Для чего?')
    def for_what(message):
        text = ('Паскаль используют для создания программных кодов, обучения основам структурной разработки, '
                'автоматизации производственных процессов, программирования устройств с микропроцессорами и создания '
                'специализированного программного обеспечения для бытовой техники и электроники.')
        bot.send_message(message.chat.id,
                         text)

    @bot.message_handler(regexp='Файлы')
    def file(message):
        text = '.pass'
        bot.send_message(message.chat.id,
                         text)

    @bot.message_handler(regexp='Другие языки')
    def another(message):
        bot.send_message(message.chat.id,
                         'Выберайте',
                         reply_markup=keyboard)


# 'C#'

@bot.message_handler(regexp='C#')
def history_C2(message):
    keyboard_1 = ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard_1.add(KeyboardButton('История'))
    keyboard_1.add(KeyboardButton('Что такое?'))
    keyboard_1.add(KeyboardButton('Для чего?'))
    keyboard_1.add(KeyboardButton('Файлы'))
    keyboard_1.add(KeyboardButton('Другие языки'))
    bot.send_message(message.chat.id,
                     'О чем хотите узнать?',
                     reply_markup=keyboard_1)

    @bot.message_handler(regexp='История')
    def history(message):
        text = ('С# был создан в период с 1998 по 2002 год командой инженеров Microsoft под руководством Андерса '
                'Хейлсберга и Скотта Вильтаумота.')
        bot.send_message(message.chat.id,
                         text)

    @bot.message_handler(regexp='Что такое?')
    def what_is(message):
        text = 'C# — это объектно-ориентированный язык программирования.'
        bot.send_message(message.chat.id,
                         text)

    @bot.message_handler(regexp='Для чего?')
    def for_what(message):
        text = ('C# используют для создания различных типов приложений, включая веб-приложения, мобильные приложения, '
                'десктопные приложения и игры.')
        bot.send_message(message.chat.id,
                         text)

    @bot.message_handler(regexp='Файлы')
    def file(message):
        text = '.cs или .csx'
        bot.send_message(message.chat.id,
                         text)

    @bot.message_handler(regexp='Другие языки')
    def another(message):
        bot.send_message(message.chat.id,
                         'Выберайте',
                         reply_markup=keyboard)


# Python

@bot.message_handler(regexp='Python')
def history_python(message):
    keyboard_1 = ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard_1.add(KeyboardButton('История'))
    keyboard_1.add(KeyboardButton('Что такое?'))
    keyboard_1.add(KeyboardButton('Для чего?'))
    keyboard_1.add(KeyboardButton('Файлы'))
    keyboard_1.add(KeyboardButton('Другие языки'))
    bot.send_message(message.chat.id,
                     'О чем хотите узнать?',
                     reply_markup=keyboard_1)

    @bot.message_handler(regexp='История')
    def history(message):
        text = ('История языка программирования Python началась в конце 1980-х. Гвидо ван Россум задумал Python в '
                '1980-х годах, а приступил к его созданию в декабре 1989 года в центре математики и информатики '
                'в Нидерландах. Язык Python был задуман как потомок языка программирования ABC, способный к обработке '
                'исключений и взаимодействию с операционной системой Амёба. Ван Россум является основным автором '
                'Python и продолжал выполнять центральную роль в принятии решений относительно развития языка вплоть '
                'до 12 июля 2018 года')
        bot.send_message(message.chat.id,
                         text)

    @bot.message_handler(regexp='Что такое?')
    def what_is(message):
        text = 'Python — это интерпретируемый язык программирования высокого уровня с динамической типизацией.'
        bot.send_message(message.chat.id,
                         text)

    @bot.message_handler(regexp='Для чего?')
    def for_what(message):
        text = ('Python используют для веб-разработки, тестирования, машинного обучения, анализа данных и создания '
                'парсеров.')
        bot.send_message(message.chat.id,
                         text)

    @bot.message_handler(regexp='Файлы')
    def file(message):
        text = '.py'
        bot.send_message(message.chat.id,
                         text)

    @bot.message_handler(regexp='Другие языки')
    def another(message):
        bot.send_message(message.chat.id,
                         'Выберайте',
                         reply_markup=keyboard)


# Java

@bot.message_handler(regexp='Java')
def history_java(message):
    keyboard_1 = ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard_1.add(KeyboardButton('История'))
    keyboard_1.add(KeyboardButton('Что такое?'))
    keyboard_1.add(KeyboardButton('Для чего?'))
    keyboard_1.add(KeyboardButton('Файлы'))
    keyboard_1.add(KeyboardButton('Другие языки'))
    bot.send_message(message.chat.id,
                     'О чем хотите узнать?',
                     reply_markup=keyboard_1)

    @bot.message_handler(regexp='История')
    def history(message):
        text = ('Проект родился в 1991 году, за кулисами команды Sun Microsystems, когда три инженера, Джеймс Гослинг, '
                'Майк Шеридан и Патрик Нотон, стремились разработать язык, применимый к небольшим электрическим '
                'устройствам. Вскоре после этого они запустили «Зеленый проект» для изучения влияния конвергенции '
                'бытовой техники с цифровым управлением и компьютеров. Используя синтаксис, аналогичный C++, '
                'они создали цифровой пульт дистанционного управления, оснащенный графическим и анимированным '
                'сенсорным экраном. Плод нескольких месяцев интенсивных исследований, этот пульт дистанционного '
                'управления обладал фантастической функцией управления всем оборудованием в гостиной. Он был '
                'запрограммирован на новом языке, полностью независимом от процессора, на котором он работал, '
                'что делало пульт уникальным в своем роде.')
        bot.send_message(message.chat.id,
                         text)

    @bot.message_handler(regexp='Что такое?')
    def what_is(message):
        text = ('Java описывается как многоцелевой, строго типизированный язык объектно-ориентированного '
                'программирования (ООП) .')
        bot.send_message(message.chat.id,
                         text)

    @bot.message_handler(regexp='Для чего?')
    def for_what(message):
        text = ('Java используют для создания серверных приложений, веб-приложений, мобильных приложений, игр и других '
                'видов программного обеспечения.')
        bot.send_message(message.chat.id,
                         text)

    @bot.message_handler(regexp='Файлы')
    def file(message):
        text = '.jar'
        bot.send_message(message.chat.id,
                         text)

    @bot.message_handler(regexp='Другие языки')
    def another(message):
        bot.send_message(message.chat.id,
                         'Выберайте',
                         reply_markup=keyboard)


# JS

@bot.message_handler(regexp='JavaScript')
def history_java_script(message):
    keyboard_1 = ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard_1.add(KeyboardButton('История'))
    keyboard_1.add(KeyboardButton('Что такое?'))
    keyboard_1.add(KeyboardButton('Для чего?'))
    keyboard_1.add(KeyboardButton('Файлы'))
    keyboard_1.add(KeyboardButton('Другие языки'))
    bot.send_message(message.chat.id,
                     'О чем хотите узнать?',
                     reply_markup=keyboard_1)

    @bot.message_handler(regexp='История')
    def history(message):
        text = ('JavaScript был создан компанией Netscape в 1995 году и быстро стал одним из самых популярных языков '
                'программирования благодаря своей простоте и широкому применению.')
        bot.send_message(message.chat.id,
                         text)

    @bot.message_handler(regexp='Что такое?')
    def what_is(message):
        text = ('JavaScript — это динамический язык программирования, который используется для создания '
                'веб-приложений.')
        bot.send_message(message.chat.id,
                         text)

    @bot.message_handler(regexp='Для чего?')
    def for_what(message):
        text = ('JavaScript используют для создания интерактивных веб-страниц, передачи информации между пользователем '
                'и сервером, анимации объектов и выполнения вычислений на стороне клиента или сервера.')
        bot.send_message(message.chat.id,
                         text)

    @bot.message_handler(regexp='Файлы')
    def file(message):
        text = '.js'
        bot.send_message(message.chat.id,
                         text)

    @bot.message_handler(regexp='Другие языки')
    def another(message):
        bot.send_message(message.chat.id,
                         'Выберайте',
                         reply_markup=keyboard)


# Basic

@bot.message_handler(regexp='Basic')
def history_basic(message):
    keyboard_1 = ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard_1.add(KeyboardButton('История'))
    keyboard_1.add(KeyboardButton('Что такое?'))
    keyboard_1.add(KeyboardButton('Для чего?'))
    keyboard_1.add(KeyboardButton('Файлы'))
    keyboard_1.add(KeyboardButton('Другие языки'))
    bot.send_message(message.chat.id,
                     'О чем хотите узнать?',
                     reply_markup=keyboard_1)

    @bot.message_handler(regexp='История')
    def history(message):
        text = ('BASIC появился в 1964 году. Его создатели — Джон Кемени и Томас Курц, сотрудники Дартмутского '
                'колледжа. Цель языка — обучение программированию на маломощных компьютерах, каковыми в ту пору '
                'являлись установленные в учебных заведениях вычислительные машины.')
        bot.send_message(message.chat.id,
                         text)

    @bot.message_handler(regexp='Что такое?')
    def what_is(message):
        text = ('BASIC (в переводе с английского «базовый», «основной») — язык программирования и связанная с ним '
                'среда разработки, созданные как средство обучения студентов-непрограммистов написанию программ для '
                'решения несложных профессиональных задач.')
        bot.send_message(message.chat.id,
                         text)

    @bot.message_handler(regexp='Для чего?')
    def for_what(message):
        text = ('Бейсик используют для разработки прикладных программ, работающих под управлением ОС Windows, '
                'а также как встроенный язык программных систем и язык программирования калькуляторов.')
        bot.send_message(message.chat.id,
                         text)

    @bot.message_handler(regexp='Файлы')
    def file(message):
        text = '.vb'
        bot.send_message(message.chat.id,
                         text)

    @bot.message_handler(regexp='Другие языки')
    def another(message):
        bot.send_message(message.chat.id,
                         'Выберайте',
                         reply_markup=keyboard)


@bot.message_handler(regexp='О проекте')
def about_me(message):
    info_me = 'Автор: Устинов Тимур'
    info_about = 'Проект нацелен на помощь, начинающим программистам определиться с выбором своего первого языка.'

    bot.send_message(message.chat.id,
                     info_me)
    bot.send_message(message.chat.id,
                     info_about)


bot.infinity_polling()
