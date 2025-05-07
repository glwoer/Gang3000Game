from time import sleep
import colorama
import random
import sys  

colorama.init()

def печать(текст, задержка=0.1):
    for буква in текст:
        sys.stdout.write(буква)  
        sys.stdout.flush()       
        sleep(задержка)
печать(colorama.Fore.BLUE + 'Зайти в магаз?')
Вход_в_магаз = input(' да/нет: ' + colorama.Fore.RESET).lower()

if Вход_в_магаз == 'да':
    print('Вы вошли')
    print('ВЫ ВСЁ ПРОЕБАЛИ')
    print('GAME OVERR')

elif Вход_в_магаз == 'нет':
    print('Ты не Пошёл в Магаз')
    sleep(3)
    print('БЛЯТТЬЬЬ МУСАААРАААА')
    sleep(3)
    Сумка = ['Марихуанка,Кокс,Glock17,Несколько магазинов на Glock17']
    print('Бляя Брат ты свою сумку видел...')
    sleep(3)
    for Предметы_в_сумке in Сумка:
        print(f'В карманах: {Сумка}')
    печать('Блять Они идут к тебе чё будешь делать? ')
    sleep(3)
    Мусора = input(colorama.Fore.BLUE + '\nСтрелять с Glock17 Нажми 1\nСбежать Нажми 2\nЗаныкать запрещёнку в Труселя нажми 3: ' + colorama.Fore.RESET)
    
    if Мусора == '1':
        Выстрел = random.choice(['Попал','Промах'])
        if Выстрел == "Попал":
            print(colorama.Fore.GREEN + 'Выстрел Пранзил Мусора насквозь')
            print('Youuu WIN' + colorama.Fore.RESET)
        elif Выстрел == 'Промах':
            print(colorama.Fore.RED + 'ЕБЛАН ТЫ НЕ ПОПАЛ')
            print('Тебя повязали ЛОХ')
            print('GAME OVER' + colorama.Fore.RESET)
    
    elif Мусора == '2':
        Побег = random.choice(['сбежал','поймали'])
        if Побег == 'сбежал':
            print(colorama.Fore.GREEN + 'Ты Себался!!!')
            print('Youuu Winn' + colorama.Fore.RESET)
        elif Побег == 'поймали':
            print('ТЕБА СПОЙМАЛИИИ ЛОХХХ')
            print('GAME OVER')
    
    elif Мусора == '3':
        сброс = random.choice(['нашли','не_нашли'])
        if сброс == 'нашли':
            print('НАРКАТУ УВИДЕЛИ')
            print('Game Overr ЛОХХХ')
        elif сброс == 'не_нашли':
            for i in range(1,6):
                печать(f'\nИдёт обыск...{i}/5')
                sleep(0.5)
            sleep(1.5)
            print('\nОк Брат Наркату не увидели')
            print('Тебя отпустили ты пошёл дальше')
            печать('Перед табой есть заваротик в переулок')
            print('\nТы завернул в переулок')
            print('Ты Идёшь...')
            sleep(4.5)
            print(colorama.Fore.GREEN + 'НА ТЕБЯ ВЫСКАЧИЛ GANG ЯЩЕР')
            print('WASSAP МЕНЧИК Нетуда ты завернул ёёёуу' + colorama.Fore.RESET)
            печать(colorama.Fore.BLUE + 'На ТЕБЯ НАПРАВИЛИ СТВОЛ ЧЁ БУДЕШЬ ДЕЛАТЬ' + colorama.Fore.RESET)
            sleep(4)
            Gang = input(colorama.Fore.BLUE + '\n1. Шмальнуть с Glock17\n2. Договориться\n3. Выбить ствол\nВыбор: ' + colorama.Fore.RESET)
            
            if Gang == '1':
                Gang_Shot = random.choice(['Получилось','Не_Получилось'])
                if Gang_Shot == 'Получилось':
                    печать(colorama.Fore.MAGENTA + 'Вы отталкиваете Ящера с криком САСАТЬ СУЧКААА\nЯщер упал на землю попытался достать писталет но увы не успел\nПока Ящер пытался достать писталет вы всаживаете в него 3 выстрела' + colorama.Fore.RESET + colorama.Fore.LIGHTBLUE_EX + '\nВы успели отталкнуть ящера и выстрелеть в него он мёртв')
                    печать('\nYooooUUUU WIIIN')
                elif Gang_Shot == 'Не_Получилось':
                    печать(colorama.Fore.MAGENTA + 'Ты попытался достать пистолет но в тебя сразу же выстелили\nТы упал на землу с дыркой в животе...\nЯщер подходит и напровляет писталет на вашу голову со словами...\nНа что ты надеелся...')
                    print(colorama.Fore.RED + 'GAME OVER' + colorama.Fore.RESET)
            
            elif Gang == '2':
                Договр = random.choice(['Договор','Не_Договор'])
                if Договр == 'Договор':
                    печать(colorama.Fore.MAGENTA + 'Вы поднимаете руки...')
                    печать('Ты:ЁЁУУ МЕНЧИК РЕЛАКС Я ВООБЩЕ НЕ ЗНАЛ ЧЁ ВЫ ТУТ КРЫШУЕТЕ УЖЕ УХОЖУ\nЯщер:Ладно менчик ну довай чтоб больше я тебя тут не видел')
                    печать('\nYOOUUUU WINNN!!!!!')
                elif Договр == 'Не_Договор':
                    печать(colorama.Fore.MAGENTA + 'Вы поднимаете руки...')
                    печать('\nТы:ЁЁУУ МЕНЧИК РЕЛАКС Я ВООБЩЕ НЕ ЗНАЛ ЧЁ ВЫ ТУТ КРЫШУЕТЕ УЖЕ УХОЖУ\nЯщер:Договариваться с богом будешь сучка')
                    print(colorama.Fore.RED + '\nGAMEOVER' + colorama.Fore.RESET)
            
            elif Gang == '3':
                Выбить = random.choice(['Выбил','Не_Выбил'])
                if Выбить == 'Выбил':
                    печать(colorama.Fore.MAGENTA + 'Вы Наносите удар сверху в низ по руке...\n')
                    sleep(1)
                    печать('Писталет выподает')
                    sleep(2)
                    печать('\nЯщер с криком: АХ ТЫ МАЛЕНЬКАЯ СУЧКА попытался ударить вас но вы успели увернутся и контратоковать')
                    sleep(1.5)
                    печать('\nВы ударили его в печень и он упал')
                    sleep(1.5)
                    печать('\nВы достаёте писталет и выпускаете в лежащего ящера всё обойму' + colorama.Fore.RESET)
                    печать('\nYOU WIIIIN SCHKAAA')
                elif Выбить == 'Не_Выбил':
                    печать(colorama.Fore.RED + 'Вы попытались выбить писталет но вас отталкнули и выстрелили в голову')
                    sleep(2)
                    печать('\nЯщер:ХА ХА ХА СМЕШНОЙ FUCKIN МЕНЧИК')
                    sleep(1)
                    печать('\nGAMEEE OVERRR LOXXX' + colorama.Fore.RESET)
