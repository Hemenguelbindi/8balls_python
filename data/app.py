import random
from config import config

def logic_main():

    while True:
        start = input("Ты хочешь узнать будущие у/n >> ")
        if start in config.yes:
            with open("log.txt", 'a') as log:
                user_talk = input("Что ты хочешь спросить у меня? ")
                text_user = 'User: '
                ent = '\n'
                log.write(text_user)
                log.write(user_talk)
                log.write(ent)
                random_Answers = random.choice(config.ANSWERS)
                text_programm = 'Ответ программы: '
                log.write(text_programm)
                log.write(random_Answers)
                log.write(ent)
                print(random_Answers)
        if start in config.do_not:
            print("Пока приходи еще.")
            break
        if start in config.stop_item_log:
            with open("log.txt", 'r') as log:
                print(log.read())
        else:
            print(f"""Ты должен нажать один из вариантов {config.yes}, 
                    если хочешь получить ответ 
                   или {config.do_not} если хочешь прекратить работу программы.""")
