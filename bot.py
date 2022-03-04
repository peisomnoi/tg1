import telebot
import random

Text = telebot.types.ReplyKeyboardMarkup(True)
Text1 = telebot.types.ReplyKeyboardMarkup(True)
Text2 = telebot.types.ReplyKeyboardMarkup(True)
Text3 = telebot.types.ReplyKeyboardMarkup(True)
Text4 = telebot.types.ReplyKeyboardMarkup(True)
Text5 = telebot.types.ReplyKeyboardMarkup(True)
Text6 = telebot.types.ReplyKeyboardMarkup(True)
Text7 = telebot.types.ReplyKeyboardMarkup(True)
Text8 = telebot.types.ReplyKeyboardMarkup(True)
weapon = telebot.types.ReplyKeyboardMarkup(True)
аrmo = telebot.types.ReplyKeyboardMarkup(True)
Question1 = telebot.types.ReplyKeyboardMarkup(True)
Question2 = telebot.types.ReplyKeyboardMarkup(True)
Question3 = telebot.types.ReplyKeyboardMarkup(True)
Question4 = telebot.types.ReplyKeyboardMarkup(True)
Question5 = telebot.types.ReplyKeyboardMarkup(True)
Question6 = telebot.types.ReplyKeyboardMarkup(True)
Question7 = telebot.types.ReplyKeyboardMarkup(True)
Question8 = telebot.types.ReplyKeyboardMarkup(True)
name = ""
weapons = ""
аrmor = ""

global xp
global xpe
global xper
xper = 100
xpe = 100
xp = 100

Text.row("Я хочу услышать твою легенду")
Text1.row("Спасибо, я пойду")
Text2.row("Наконец-то, джунгли")
Text3.row("Конечно, я не вижу других дорог")
Text4.row("Ну и жесть!!!")
Text5.row("Пора идти!")
Text6.row("Кинуть кубик")
Text7.row("Пойдем")
Text8.row("Любовь", "Деньги")
weapon.row("Кинжалы", "Моргенштерн", "Нунчаки")
аrmo.row("Алмазная броня", "Броня из кожи с чарами крутыми как из майнкрафта",
         "Кольчуга")
Question1.row("Переплыть", "Обойти")
Question2.row("Налоксон", "Зеленка", "Налорфин", "Ибупрофен")
Question3.row(
    "Метнуться кабанчиком сквозь джунгли",
    "Аккуратно пробираться через корни деревьев и осматривать все вокруг")
Question4.row("Отсосать яд", "Ничего, само пройдет", "Отрубить руки")
Question5.row("Убить", "Поговорить")
Question6.row("метод input()", "метод get()", "метод read()")
Question7.row("clock", "time", "period")
Question8.row("print()", "write()", "log()")

bot = telebot.TeleBot('1707302503:AAHezkh8xk23MWVDVMV2lj-CriN2VDngspg')


@bot.message_handler(commands=['start'])
def startWork(message):
    mid = message.chat.id
    bot.send_message(mid,
                     "Здравствуй, странник, хочешь я расскажу тебе легенду?",
                     reply_markup=Text)


@bot.message_handler(content_types=['text'])
def sendYourMessage(message):
    mid = message.chat.id
    if message.text == "Я хочу услышать твою легенду":
        msg = bot.send_message(
            mid,
            "Для начала тебе нужно представиться",
            reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(msg, get_name)
    else:
        bot.send_message(
            mid, "Ты работаешь не по сценарию, я сейчас режиссера позову")


def get_name(message):
    global name
    name = message.text
    bot.send_message(
        message.from_user.id, "Ну, здравствуй, " + name +
        ", xодит легенда о том, что богатый отец очень хотел выдать свою дочь замуж, но хотел, чтобы ее избранником был сильный и выносливый человек, поэтому сделал дорогу к принцессе очень сложной ...К слову баллад о ее красоте никто не писал, так что, возможно, с ней что-то неладное...Но я думаю, ты  хотел бы показать всем свою смелость и преодолеть все испытания."
    )
    bot.send_message(message.from_user.id,
                     "Чтобы пройти путь нужно выбрать экипировку",
                     reply_markup=weapon)
    bot.register_next_step_handler(message, get_armor)


def get_armor(message):
    global weapons
    weapons = message.text
    bot.send_message(
        message.from_user.id,
        "Не забудь про доспех, выбор небольшой, но посмотри, что есть:",
        reply_markup=аrmo)
    bot.register_next_step_handler(message, outreach)


def outreach(message):
    global аrmor
    аrmor = message.text
    bot.send_message(
        message.from_user.id, "Отличный выбор: " + weapons + " и " + аrmor +
        ", не забудь, что у тебя всего " + str(xp) + "XP. ")
    bot.send_message(
        message.from_user.id,
        "Держи карту, тут ты увидишь, куда тебе нужно идти."
    )
    bot.send_photo(
        message.from_user.id,
        "https://i.pinimg.com/originals/21/1a/df/211adfee38563a140b3b85af1642a0a6.jpg",
        reply_markup=Text1)
    bot.send_message(message.from_user.id,
                     "Удачи тебе, помни, что это все не то, чем кажется..")
    bot.register_next_step_handler(message, swamp)


def swamp(message):
    bot.send_photo(
        message.from_user.id,
        "https://sun9-64.userapi.com/impg/AoNwxIM9UWd-qTVreJ_BA1YOELxSPhw7A2pjsA/n4JmFvjr3mQ.jpg?size=1280x740&quality=96&sign=5a94a8943a098b84855729ce8354eab5&type=album",
        reply_markup=telebot.types.ReplyKeyboardRemove())
    bot.send_message(message.from_user.id, "Локация болото с крокодилами")
    bot.send_message(
        message.from_user.id,
        "Странно, я не вижу ни одного крокодила, может переплыть?",
        reply_markup=Question1)
    bot.register_next_step_handler(message, Question)


def Question(message):
    if message.text == "Переплыть":
        bot.send_message(
            message.from_user.id,
            "Ты подходишь к болоту и чувствуешь резкий бензиновый запах, но это не смогло тебя переубедить, тогда ты нырнул и поплыл, и только после этого понял, что это болото и есть 'крокодил', дезоморфин научным языком. Было уже поздно, чтобы менять траекторию. Ты из последних сил добрался до противоположного берега....И теряешь сознание."
        )
        global xpe
        xpe = xp - 30
        bot.send_message(
            message.from_user.id,
            "Чтобы остаться в живых, тебе нужно выбрать один из антидотов крокодила:",
            reply_markup=Question2)
        bot.register_next_step_handler(message, crocodile)
    elif message.text == "Обойти":
        bot.send_message(
            message.from_user.id,
            "Ты долго идёшь в обход и видишь, как впереди поваляется туман. Ты заходишь вглубь этого густого тумана. В нем слышатся голоса но ты не слушаешь и идёшь дальше. Вот уже из далека и видятся джунгли. ",
            reply_markup=Text2)
        bot.register_next_step_handler(message, junley)
    else:
        bot.send_message(
            message.from_user.id,
            "Ты работаешь не по сценарию, я сейчас режиссера позову")
        bot.register_next_step_handler(message, Question)


def crocodile(message):
    if message.text == "Налоксон":
        bot.send_message(
            message.from_user.id,
            "Ты очнулся, но тебе не хорошо, у тебя осталось всего " + str(xpe) +
            " XP. Дальше нужно быть более аккуратным, чтобы суметь дойти до конца...",
            reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.send_message(
            message.from_user.id,
            "Не забывай  https://zuzino.mos.ru/sotsialnaya-sfera/useful-information-about-the-dangers-of-drugs/",
            reply_markup=Text1)
        bot.register_next_step_handler(message, junley)
    elif message.text == "Налорфин":
        bot.send_message(
            message.from_user.id,
            "Ты очнулся, но тебе не хорошо, у тебя осталось всего " + str(xpe) +
            " XP. Дальше нужно быть более аккуратным, чтобы суметь дойти до конца...",
            reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.send_message(
            message.from_user.id,
            "Не забывай  https://zuzino.mos.ru/sotsialnaya-sfera/useful-information-about-the-dangers-of-drugs/",
            reply_markup=Text1)
        bot.register_next_step_handler(message, junley)
    elif message.text == "Ибупрофен":
        bot.send_message(message.from_user.id,
                         "YOU DIED((",
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.send_message(
            message.from_user.id,
            "Не забывай  https://zuzino.mos.ru/sotsialnaya-sfera/useful-information-about-the-dangers-of-drugs/"
        )
        bot.register_next_step_handler(message, startWork)
    elif message.text == "Зеленка":
        bot.send_message(message.from_user.id,
                         "YOU DIED((",
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.send_message(
            message.from_user.id,
            "Не забывай  https://zuzino.mos.ru/sotsialnaya-sfera/useful-information-about-the-dangers-of-drugs/"
        )
        bot.register_next_step_handler(message, startWork)
    else:
        bot.send_message(
            message.from_user.id,
            "Ты работаешь не по сценарию, я сейчас режиссера позову")
        bot.register_next_step_handler(message, crocodile)


def junley(message):
    bot.send_photo(
        message.from_user.id,
        "https://sun9-58.userapi.com/impg/xjrJtc6jPZfmyn6h-Pe4zOXpeITUldzNjbzyiw/08AmIWDSdG8.jpg?size=1280x727&quality=96&sign=c768ab85e8d92542925273f2b869beb8&type=album",
        reply_markup=telebot.types.ReplyKeyboardRemove())
    bot.send_message(
        message.from_user.id,
        "Локация джунгли с ядовитыми змеями\nОгромные деревья пробивают облака, а с них свисают плотные толстые лианы, ты подходишь к самому началу этих зарослей и пытаешься придумать план, как все-таки преодолеть это испытание\nЧто будем делать?",
        reply_markup=Question3)
    bot.register_next_step_handler(message, Quest3)


def Quest3(message):
    if message.text == "Метнуться кабанчиком сквозь джунгли":
        bot.send_message(
            message.from_user.id,
            "Ты бежишь очень быстро, джунгли кажутся нескончаемыми.")
        bot.send_message(
            message.from_user.id,
            "Кажется, я тут не один...\nИз кустов на тебя бросается змея и кусает в ногу.\nТы падаешь.\nАааа, надо срочно что-то с этим делать! Как же мне выжить ?\nЧто делать при укусе змеи?",
            reply_markup=Question4)
        bot.register_next_step_handler(message, snake)
    elif message.text == "Аккуратно пробираться через корни деревьев и осматривать все вокруг":
        bot.send_message(
            message.from_user.id,
            "Ты смотришь по сторонам и аккуратно ступаешь на землю. Твоя броня тихо бренчит, а ветер немного задувает под неё. Ты доходишь до трона из корней, а там тебя уже давно ждал мудрый питон.",
            reply_markup=Question5)
        bot.register_next_step_handler(message, snace)
    else:
        bot.send_message(
            message.from_user.id,
            "Ты работаешь не по сценарию, я сейчас режиссера позову")


def snake(message):
    if message.text == "Отсосать яд":
        xper = xp - (100 - xpe) - 10
        bot.send_message(
            message.from_user.id,
            "От испуга ты пытаешься отсосать яд, но ты не можешь дотянутся до ноги и еще "
            + аrmor +
            " мешает тебе, из-за этого ты подаешь и ударяешься головой, твое ХР - "
            + str(xper) +
            ".\nПосле того как ты пришёл в себя, ты увидел сквозь деревья силуэт песчаных дюн и выдвинулся в ту сторону.",
            reply_markup=Text5)
        bot.register_next_step_handler(message, desert)
    elif message.text == "Ничего, само пройдет":
        bot.send_message(
            message.from_user.id,
            "Ты остался жив, а твой враг уже скрылся в кустах, не задумываясь ты пошел дальше.\nПосле того как ты пришёл в себя, ты увидел сквозь деревья силуэт песчаных дюн и выдвинулся в ту сторону.",
            reply_markup=Text5)
        bot.register_next_step_handler(message, desert)
    elif message.text == "Отрубить руки":
        bot.send_message(message.from_user.id,
                         "И что же ты наделал? Ты шутишь, это же уж\nYOU DIED((",
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.send_message(
            message.from_user.id,
            "Выучи\n https://bugaga.ru/interesting/1146752808-top-25-samye-yadovitye-zmei-na-planete.html"
        )
        bot.register_next_step_handler(message, startWork)
    else:
        bot.send_message(
            message.from_user.id,
            "Ты работаешь не по сценарию, я сейчас режиссера позову")
        bot.register_next_step_handler(message, snake)


def snace(message):
    if message.text == "Убить":
        you = random.randint(1, 10)
        if you >= 5:
            bot.send_message(
                message.from_user.id,
                "Ты убиваешь змею, но стоило ли марать свои руки кровью ни в чем неповинного питона? Ты ещё раз оглянул труп.\n Бывает же... Посмотрел по сторонам и увидел сквозь деревья силуэт песчаных дюн и выдвинулся в ту сторону. ",
                reply_markup=Text4)
            bot.register_next_step_handler(message, desert)
        else:
            bot.send_message(message.from_user.id,
                             "Ты не смог одолеть мудрого питона.\nYOU DIED((",
                             reply_markup=telebot.types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, startWork)

    elif message.text == "Поговорить":
        bot.send_message(
            message.from_user.id,
            "Здравствуй, странник, моя память меня подводит. Я родоначальник языка программирования - питон. Но я что-то начинаю забывать, как все работает в моем детище. Помоги мне вспомнить, пожалуйста\nКак получить данные от пользователя?",
            reply_markup=Question6)
        bot.register_next_step_handler(message, python)

    else:
        bot.send_message(
            message.from_user.id,
            "Ты работаешь не по сценарию, я сейчас режиссера позову")
        bot.register_next_step_handler(message, snace)


def python(message):
    if message.text == "метод input()":
        bot.send_message(message.from_user.id,
                         "Молодец.Какая библиотека отвечает за время?",
                         reply_markup=Question7)
        bot.register_next_step_handler(message, python1)

    elif message.text == "метод get()":
        bot.send_message(
            message.from_user.id,
            "Ты не можешь ответить на такие простые вопросы? Я не знаю, как реагировать на это...Я никак не помогу тебе добраться до принцессы, могу только помочь тебе преисполниться в мастерстве языка Питон...\nТебе указали на тропинку, которая выводила из этих джунглей. На удивление больше никаких неприятностей с тобой не произошло. Ты шёл не очень долго и увидел, как резко густые джунгли сменились засушливой пустыней с огромными дюнами...",
            reply_markup=Text5)
        bot.register_next_step_handler(message, desert)

    elif message.text == "метод read()":
        bot.send_message(
            message.from_user.id,
            "Ты не можешь ответить на такие простые вопросы? Я не знаю, как реагировать на это...Я никак не помогу тебе добраться до принцессы, могу только помочь тебе преисполниться в мастерстве языка Питон...\nТебе указали на тропинку, которая выводила из этих джунглей. На удивление больше никаких неприятностей с тобой не произошло. Ты шёл не очень долго и увидел, как резко густые джунгли сменились засушливой пустыней с огромными дюнами...",
            reply_markup=Text5)
        bot.register_next_step_handler(message, desert)

    else:
        bot.send_message(
            message.from_user.id,
            "Ты работаешь не по сценарию, я сейчас режиссера позову")
        bot.register_next_step_handler(message, python)


def python1(message):
    if message.text == "time":
        bot.send_message(
            message.from_user.id,
            "А ты хорош.Какая функция выводит что-либо в консоль?",
            reply_markup=Question8)
        bot.register_next_step_handler(message, python2)

    elif message.text == "clock":
        bot.send_message(
            message.from_user.id,
            "Ты не можешь ответить на такие простые вопросы? Я не знаю, как реагировать на это...Я никак не помогу тебе добраться до принцессы, могу только помочь тебе преисполниться в мастерстве языка Питон...\nТебе указали на тропинку, которая выводила из этих джунглей. На удивление больше никаких неприятностей с тобой не произошло. Ты шёл не очень долго и увидел, как резко густые джунгли сменились засушливой пустыней с огромными дюнами...",
            reply_markup=Text5)
        bot.register_next_step_handler(message, desert)

    elif message.text == "period":
        bot.send_message(
            message.from_user.id,
            "Ты не можешь ответить на такие простые вопросы? Я не знаю, как реагировать на это...Я никак не помогу тебе добраться до принцессы, могу только помочь тебе преисполниться в мастерстве языка Питон...\nТебе указали на тропинку, которая выводила из этих джунглей. На удивление больше никаких неприятностей с тобой не произошло. Ты шёл не очень долго и увидел, как резко густые джунгли сменились засушливой пустыней с огромными дюнами...",
            rreply_markup=Text5)
        bot.register_next_step_handler(message, desert)

    else:
        bot.send_message(
            message.from_user.id,
            "Ты работаешь не по сценарию, я сейчас режиссера позову")
        bot.register_next_step_handler(message, python1)


def python2(message):
    if message.text == "print()":
        bot.send_message(
            message.from_user.id,
            "Ты помог мне вспомнить все, спасибо тебе...Держи за это читерский кубик, он тебе ещё пригодится, вот увидишь. Прощай.\nТебе указали на тропинку, которая выводила из этих джунглей. На удивление больше никаких неприятностей с тобой не произошло. Ты шёл не очень долго и увидел, как резко густые джунгли сменились засушливой пустыней с огромными дюнами...",reply_markup=Text5)
        bot.register_next_step_handler(message, desert1)

    elif message.text == "write()":
        bot.send_message(
            message.from_user.id,
            "Ты не можешь ответить на такие простые вопросы? Я не знаю, как реагировать на это...Я никак не помогу тебе добраться до принцессы, могу только помочь тебе преисполниться в мастерстве языка Питон...\nТебе указали на тропинку, которая выводила из этих джунглей. На удивление больше никаких неприятностей с тобой не произошло. Ты шёл не очень долго и увидел, как резко густые джунгли сменились засушливой пустыней с огромными дюнами...",
            reply_markup=Text5)
        bot.register_next_step_handler(message, desert)

    elif message.text == "log()":
        bot.send_message(
            message.from_user.id,
            "Ты не можешь ответить на такие простые вопросы? Я не знаю, как реагировать на это...Я никак не помогу тебе добраться до принцессы, могу только помочь тебе преисполниться в мастерстве языка Питон...\nТебе указали на тропинку, которая выводила из этих джунглей. На удивление больше никаких неприятностей с тобой не произошло. Ты шёл не очень долго и увидел, как резко густые джунгли сменились засушливой пустыней с огромными дюнами...",
            reply_markup=Text5)
        bot.register_next_step_handler(message, desert)

    else:
        bot.send_message(
            message.from_user.id,
            "Ты работаешь не по сценарию, я сейчас режиссера позову")
        bot.register_next_step_handler(message, python2)


def desert(message):
    bot.send_photo(
        message.from_user.id,
        "https://sun9-34.userapi.com/impg/JcR-TgKjqIGot2TUFZ9oZlL5z4Y6oAeeBivObQ/B0ip46KwxA4.jpg?size=1280x606&quality=96&sign=bc536bc038be605c4e4f20daf794186a&type=album",
        reply_markup=telebot.types.ReplyKeyboardRemove())
    bot.send_message(
        message.from_user.id,
        "Локация пустыня со Скорпионом\n-Фух...Я так устал, что же будет на этот раз?\nПеред тобой во всей красе появляется устрашающий Скорпион, Ханзо Хасаши.\nСразимся?",
        reply_markup=Text3)
    bot.register_next_step_handler(message, fight)


def fight(message):
    if message.text == "Конечно, я не вижу других дорог":
        bot.send_message(message.from_user.id,
                         "Вы садитесь друг перед другом, берете кости и ... ",
                         reply_markup=Text6)
        bot.register_next_step_handler(message, game)
    else:
        bot.send_message(
            message.from_user.id,
            "Ты работаешь не по сценарию, я сейчас режиссера позову")
        bot.register_next_step_handler(message, fight)


def game(message):
    if message.text == "Кинуть кубик":
        bot.send_message(
            message.from_user.id,
            "Кубик выпадает из рук твоего оппонента, а затем и из твоих, ты надеешься на выигрыш, но Фортуна ветрена...",
            reply_markup=telebot.types.ReplyKeyboardRemove())
        enemy = random.randint(1, 10)
        you = random.randint(1, 10)
        if you > enemy:
            bot.send_message(
                message.from_user.id,
                "-А ты везунчик.У тебя выпало " + str(you) +
                ", а у меня всего лишь " + str(enemy) +
                ".\nТак и быть я отведу тебя к принцессе, но не радуйся раньше времени....",
                reply_markup=Text7)
            bot.register_next_step_handler(message, home)
        elif you < enemy:
            bot.send_message(
                message.from_user.id, "-Принцесса - моя.У тебя выпало всего " +
                str(you) + ", а у меня " + str(enemy) +
                ".\nТебе лучше убираться если не хочешь сгинуть на тот свет.\nТебе приходиться уйти чтобы не потерять свою голову, но возможно это к лучшему."
            )
            bot.register_next_step_handler(message, startWork)
        else:
            bot.send_message(
                message.from_user.id,
                "Давай кинем еще раз. А то и у тебя, и у меня " + str(you))
            bot.register_next_step_handler(message, game)
    else:
        bot.send_message(
            message.from_user.id,
            "Ты работаешь не по сценарию, я сейчас режиссера позову")
        bot.register_next_step_handler(message, game)


def home(message):
    bot.send_photo(
        message.from_user.id,
        "https://sun9-37.userapi.com/impg/DZFcqYCjdITc5xVurrKQmoqgSozk8cur7mjy7g/tWJot_NRsLw.jpg?size=1280x535&quality=96&sign=e2e55ede37094c565cedad984f06bf28&type=album",
        reply_markup=telebot.types.ReplyKeyboardRemove())
    bot.send_message(
        message.from_user.id,
        "Тебя ведут сквозь пустыню и ты видишь вдруг, как опять же резко меняется пустыня на лавандовое поле, в котором стоит небольшой каменный замок.\nТы решаешь постучаться в дом, но на секунду задумываешься.\n-Надо ли?\nВ конце концов ты созрел для того, чтобы наконец увидеть принцессу.\nТы слышишь шаги за дверью. Сердце начинает быстрее биться...Дверь медленно открывается и перед тобой появляется девушка неописуемой красоты.\n-Здравствуй, "
        + name +
        ". Мы тебя уже давно ждали.\nХммм...Кто мы?\n- Неужели ты не та самая принцесса?\n-Нет, я лишь ее служанка.\nВы заходите в зал. И там ты видишь, как кто-то сидит в кресле спиной к вам.\n- Принцесса, он пришёл.\n- Здравствуй, "+ name +".\nПринцесса поворачивается к вам лицом...И ты видишь, видишь принцессу. Ты подумал о том, что прав был старик.\nВ общем принцесса оказалась темнокожей, оказалось, кроме того она передвигалась на коляске..\n-Я знаю, что ты тут, потому что я наследница большого состояния, но нужно ли тебе это? Конечно, мой отец будет доволен тем, что ты появился....В общем, я пойму, если ты уйдёшь.",
        reply_markup=Text8)
    bot.register_next_step_handler(message, choice)


def choice(message):
    if message.text == "Деньги":
        bot.send_message(
            message.from_user.id,
            "- Да что ты, Принцесса, ты прекрасна, будь моей супругой.Ты стал членом семьи с большим состоянием, тебе больше никогда не нужно переживать за то, как прокормить себя и у тебя будет все, чего ты хотел.\nНадолго ли тебя хватит? Увидим. А пока всего тебе хорошего.",reply_markup=telebot.types.ReplyKeyboardRemove()
        )

    elif message.text == "Любовь":
        bot.send_message(
            message.from_user.id,
            "- Прости, Принцесса, ты права, не такую я ожидал увидеть...Нет у нас искры. Это будет для меня большим опытом, спасибо вам всем за это путешествие, но я пойду..\n- Спасибо тебе за честность, если ты вдруг передумаешь, ты знаешь дорогу.",reply_markup=telebot.types.ReplyKeyboardRemove()
        )
    else:
        bot.send_message(
            message.from_user.id,
            "Ты работаешь не по сценарию, я сейчас режиссера позову")
        bot.register_next_step_handler(message, choice)


def desert1(message):
    bot.send_photo(
        message.from_user.id,
        "https://sun9-34.userapi.com/impg/JcR-TgKjqIGot2TUFZ9oZlL5z4Y6oAeeBivObQ/B0ip46KwxA4.jpg?size=1280x606&quality=96&sign=bc536bc038be605c4e4f20daf794186a&type=album",
        reply_markup=telebot.types.ReplyKeyboardRemove())
    bot.send_message(
        message.from_user.id,
        "Локация пустыня с Скорпионом\n-Фух...Я так устал, что же будет на этот раз?\nПеред тобой во всей красе появляется Скорпион, Ханзо Хасаши.\nСразимся?",
        reply_markup=Text3)
    bot.register_next_step_handler(message, fight1)


def fight1(message):
    if message.text == "Конечно, я не вижу других дорог":
        bot.send_message(message.from_user.id,
                         "Вы садитесь друг перед другом, берете кости и ... ",
                         reply_markup=Text6)
        bot.register_next_step_handler(message, game1)
    else:
        bot.send_message(
            message.from_user.id,
            "Ты работаешь не по сценарию, я сейчас режиссера позову")
        bot.register_next_step_handler(message, fight1)


def game1(message):
    if message.text == "Кинуть кубик":
        bot.send_message(
            message.from_user.id,
            "Кубик выпадает из рук твоего оппонента, а затем из твоих, ты надеешься на выигрыш, но Фортуна ветрена...",
            reply_markup=telebot.types.ReplyKeyboardRemove())
        enemy = random.randint(1, 10)
        you = random.randint(5, 10)
        if you > enemy:
            bot.send_message(
                message.from_user.id,
                "-А ты везунчик.У тебя выпало " + str(you) +
                ", а у меня всего лишь " + str(enemy) +
                ".\nТак и быть я отведу тебя к принцессе, но не радуйся раньше времени....",
                reply_markup=Text7)
            bot.register_next_step_handler(message, home)
        elif you < enemy:
            bot.send_message(
                message.from_user.id, "-Принцесса моя.У тебя выпало всего " +
                str(you) + ", а у меня " + str(enemy) +
                ".\nТебе лучше убираться если не хочешь сгинуть на тот свет.\nТебе приходиться уйти чтобы не потерять свою голову, но возможно это к лучшему."
            )
            bot.register_next_step_handler(message, startWork)
        else:
            bot.send_message(
                message.from_user.id,
                "Ну давай перекинем. А то и у тебя, и у меня " + str(you),
                 reply_markup=Text6)
            bot.register_next_step_handler(message, game1)
    else:
        bot.send_message(
            message.from_user.id,
            "Ты работаешь не по сценарию, я сейчас режиссера позову")
        bot.register_next_step_handler(message, game1)


bot.polling()
