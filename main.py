import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = '7094294744:AAEEC2Bc9WY7YwGrrQjtN_iS4PQsimOTEMY'
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


@bot.message_handler(regexp='C++')
def history_C1(message):
    history = ('История C++ начинается в 1979 году, когда Бьерн Страуструп, создатель этого языка программирования, '
               'впервые начал работу над языком, который тогда был известен как «С c классами» (C with Classes). '
               'Изначально язык разрабатывался, как новая улучшенная версия языка программирования C с добавлением '
               'дополнительных фич, которые сделали его объектно-ориентированным. В 1998 году C++ был официально '
               'стандартизирован и стал надежной рабочей лошадкой. К этому моменту C++ был одним из наиболее часто '
               'используемых языков программирования во всем мире и сохраняет эту позицию по сей день.')
    info_about = ('C++ компилируемый язык программирования общего назначения, сочетает свойства как высокоуровневых, '
                  'так и низкоуровневых языков программирования. В сравнении с его предшественником, '
                  'языком программирования Cи, наибольшее внимание уделено поддержке объектно-ориентированного и '
                  'обобщённого программирования. Название «язык программирования C++» происходит от языка '
                  'программирования'
                  'C, в котором унарный оператор ++ обозначает инкремент переменной.')
    file = '.cpp или .cxx'
    bot.send_message(message.chat.id,
                     history)
    bot.send_message(message.chat.id,
                     info_about)
    bot.send_message(message.chat.id,
                     f'расширения для программирования {file}')


@bot.message_handler(regexp='Pascal')
def history_Pascal(message):
    history = ('Язык был создан Никлаусом Виртом в 1968—1969 годах после его участия в работе комитета разработки '
               'стандарта языка Алгол-68. Язык назван в честь французского математика, физика, литератора и философа '
               'Блеза Паскаля, который создал одну из первых в мире механических машин, складывающую два числа.')
    info_about = ('Pascal — это универсальный язык программирования, отличающийся строгой структурой и типизацией '
                  'переменных, а также интуитивно понятным синтаксисом.')
    file = '.pass'
    bot.send_message(message.chat.id,
                     history)
    bot.send_message(message.chat.id,
                     info_about)
    bot.send_message(message.chat.id,
                     f'расширения для программирования {file}')


@bot.message_handler(regexp='C#')
def history_C2(message):
    history = ('С# был создан в период с 1998 по 2002 год командой инженеров Microsoft под руководством Андерса '
               'Хейлсберга и Скотта Вильтаумота.')
    info_about = 'C# — это объектно-ориентированный язык программирования.'
    file = '.cs или .csx'
    bot.send_message(message.chat.id,
                     history)
    bot.send_message(message.chat.id,
                     info_about)
    bot.send_message(message.chat.id,
                     f'расширения для программирования {file}')


@bot.message_handler(regexp='Python')
def history_python(message):
    history = ('История языка программирования Python началась в конце 1980-х. Гвидо ван Россум задумал Python в '
               '1980-х годах, а приступил к его созданию в декабре 1989 года в центре математики и информатики '
               'в Нидерландах. Язык Python был задуман как потомок языка программирования ABC, способный к обработке '
               'исключений и взаимодействию с операционной системой Амёба. Ван Россум является основным автором '
               'Python и продолжал выполнять центральную роль в принятии решений относительно развития языка вплоть '
               'до 12 июля 2018 года')
    info_about = 'Python — это интерпретируемый язык программирования высокого уровня с динамической типизацией.'
    file = '.py'
    bot.send_message(message.chat.id,
                     history)
    bot.send_message(message.chat.id,
                     info_about)
    bot.send_message(message.chat.id,
                     f'расширения для программирования {file}')


@bot.message_handler(regexp='Java')
def history_java(message):
    history = ('Проект родился в 1991 году, за кулисами команды Sun Microsystems, когда три инженера, Джеймс Гослинг, '
               'Майк Шеридан и Патрик Нотон, стремились разработать язык, применимый к небольшим электрическим '
               'устройствам. Вскоре после этого они запустили «Зеленый проект» для изучения влияния конвергенции '
               'бытовой техники с цифровым управлением и компьютеров. Используя синтаксис, аналогичный C++, '
               'они создали цифровой пульт дистанционного управления, оснащенный графическим и анимированным '
               'сенсорным экраном. Плод нескольких месяцев интенсивных исследований, этот пульт дистанционного '
               'управления обладал фантастической функцией управления всем оборудованием в гостиной. Он был '
               'запрограммирован на новом языке, полностью независимом от процессора, на котором он работал, '
               'что делало пульт уникальным в своем роде.')
    info_about = ('Java описывается как многоцелевой, строго типизированный язык объектно-ориентированного '
                  'программирования (ООП) .')
    file = '.jar'
    bot.send_message(message.chat.id,
                     history)
    bot.send_message(message.chat.id,
                     info_about)
    bot.send_message(message.chat.id,
                     f'расширения для программирования {file}')


@bot.message_handler(regexp='JavaScript')
def history_java_script(message):
    history = ('JavaScript был создан компанией Netscape в 1995 году и быстро стал одним из самых популярных языков '
               'программирования благодаря своей простоте и широкому применению.')
    info_about = ('JavaScript — это динамический язык программирования, который используется для создания '
                  'веб-приложений.')
    file = '.js'
    bot.send_message(message.chat.id,
                     history)
    bot.send_message(message.chat.id,
                     info_about)
    bot.send_message(message.chat.id,
                     f'расширения для программирования {file}')


@bot.message_handler(regexp='Basic')
def history_basic(message):
    history = ('BASIC появился в 1964 году. Его создатели — Джон Кемени и Томас Курц, сотрудники Дартмутского '
               'колледжа. Цель языка — обучение программированию на маломощных компьютерах, каковыми в ту пору '
               'являлись установленные в учебных заведениях вычислительные машины.')
    info_about = ('BASIC (в переводе с английского «базовый», «основной») — язык программирования и связанная с ним '
                  'среда разработки, созданные как средство обучения студентов-непрограммистов написанию программ для '
                  'решения несложных профессиональных задач.')
    file = '.vb'
    bot.send_message(message.chat.id,
                     history)
    bot.send_message(message.chat.id,
                     info_about)
    bot.send_message(message.chat.id,
                     f'расширения для программирования {file}')


@bot.message_handler(regexp='О проекте')
def about_me(message):
    info_me = 'Автор: Устинов Тимур'
    info_about = 'Проект нацелен на помощь, начинающим программистам определиться с выбором своего первого языка.'

    bot.send_message(message.chat.id,
                     info_me)
    bot.send_message(message.chat.id,
                     info_about)


bot.infinity_polling()
