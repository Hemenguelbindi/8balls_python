import random
ANSWERS = [
    'Бесспорно',
    'Предрешено',
    'Никаких сомнений',
    'Определённо да',
    'Можешь быть уверен в этом',
    'Мне кажется — «да»',
    'Вероятнее всего',
    'Хорошие перспективы',
    'Знаки говорят — «да»',
    'Да',
    'Пока не ясно, попробуй снова',
    'Спроси позже',
    'Лучше не рассказывать',
    'Сейчас нельзя предсказать',
    'Сконцентрируйся и спроси опять',
    'Даже не думай',
    'Мой ответ — «нет»',
    'По моим данным — «нет»',
    'Перспективы не очень хорошие',
    'Весьма сомнительно',
]
yes = ['Y','y','Д', 'д']
do_not = ['N', 'n', 'Н', 'н']
stop_item_log = ['log']

def logic_main():

    while True:
        start = input("Ты хочешь узнать будущие у/n >> ")
        if start in yes:
            with open("log.txt", 'a') as log:
                user_talk = input("Что ты хочешь спросить у меня? ")
                text_user = 'User: '
                ent = '\n'
                log.write(text_user)
                log.write(user_talk)
                log.write(ent)
                random_Answers = random.choice(ANSWERS)
                text_programm = 'Ответ программы: '
                log.write(text_programm)
                log.write(random_Answers)
                log.write(ent)
                print(random_Answers)
        if start in do_not:
            print("Пока приходи еще.")
            break
        if start in stop_item_log:
            with open("log.txt", 'r') as log:
                print(log.read())
        else:
            print(f"""Ты должен нажать один из вариантов {yes}, 
                    если хочешь получить ответ 
                   или {do_not} если хочешь прекратить работу программы.""")




logic_main()