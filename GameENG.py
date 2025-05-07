from time import sleep
import colorama
import random
import sys  

colorama.init()

def typewriter(text, delay=0.1):
    for letter in text:
        sys.stdout.write(letter)  
        sys.stdout.flush()       
        sleep(delay)
typewriter(colorama.Fore.BLUE + 'Go to the shop?')
shop_entry = input(' yes/no: ' + colorama.Fore.RESET).lower()

if shop_entry == 'yes':
    print('You entered')
    print('YOU LOST EVERYTHING')
    print('GAME OVERR')

elif shop_entry == 'no':
    print("You didn't go to the shop")
    sleep(3)
    print('SHIIITTT COPS!!!')
    sleep(3)
    bag = ['Weed,Coke,Glock17,A few mags for the Glock17']
    print('Damn bro have you seen what’s in your bag...')
    sleep(3)
    for item in bag:
        print(f'In your pockets: {bag}')
    typewriter('Shit they’re coming for you, what you gonna do? ')
    sleep(3)
    cops = input(colorama.Fore.BLUE + '\nShoot with Glock17 Press 1\nRun Press 2\nHide the illegal stuff in your underwear press 3: ' + colorama.Fore.RESET)
    
    if cops == '1':
        shot = random.choice(['Hit','Miss'])
        if shot == "Hit":
            print(colorama.Fore.GREEN + 'Shot pierced through the cop')
            print('Youuu WIN' + colorama.Fore.RESET)
        elif shot == 'Miss':
            print(colorama.Fore.RED + 'DUMBASS YOU MISSED')
            print('They cuffed you FOOL')
            print('GAME OVER' + colorama.Fore.RESET)
    
    elif cops == '2':
        escape = random.choice(['escaped','caught'])
        if escape == 'escaped':
            print(colorama.Fore.GREEN + 'You ran off!!!')
            print('Youuu Winn' + colorama.Fore.RESET)
        elif escape == 'caught':
            print('THEY FUCKIN CAUGHT YOUUUU')
            print('GAME OVER')
    
    elif cops == '3':
        stash = random.choice(['found','not_found'])
        if stash == 'found':
            print('THEY SAW THE DRUGS')
            print('Game Overr LOSERRR')
        elif stash == 'not_found':
            for i in range(1,6):
                typewriter(f'\nSearch in progress...{i}/5')
                sleep(0.5)
            sleep(1.5)
            print('\nAlright bro, they didn’t see the stash')
            print('They let you go, you kept walking')
            typewriter('Ahead of you there’s an alleyway')
            print('\nYou turned into the alley')
            print('You are walking...')
            sleep(4.5)
            print(colorama.Fore.GREEN + 'A GANG LIZARD JUMPED AT YOU')
            print('WASSAP HOMIE You turned the wrong way yoooo' + colorama.Fore.RESET)
            typewriter(colorama.Fore.BLUE + 'They pointed a gun at you, what you gonna do' + colorama.Fore.RESET)
            sleep(4)
            gang = input(colorama.Fore.BLUE + '\n1. Shoot with Glock17\n2. Talk it out\n3. Disarm them\nChoice: ' + colorama.Fore.RESET)
            
            if gang == '1':
                gang_shot = random.choice(['Success','Fail'])
                if gang_shot == 'Success':
                    typewriter(colorama.Fore.MAGENTA + 'You shove the Lizard yelling SUCK IT BIIITCH\nLizard fell to the ground trying to pull his gun but failed\nWhile he struggled you pumped 3 bullets into him' + colorama.Fore.RESET + colorama.Fore.LIGHTBLUE_EX + '\nYou managed to push the Lizard and shoot him, he’s dead')
                    typewriter('\nYooooUUUU WIIIN')
                elif gang_shot == 'Fail':
                    typewriter(colorama.Fore.MAGENTA + 'You tried to pull your gun but he shot you right away\nYou fell to the ground with a hole in your stomach...\nLizard walks up and points the gun to your head saying...\nWhat were you hoping for...')
                    print(colorama.Fore.RED + 'GAME OVER' + colorama.Fore.RESET)
            
            elif gang == '2':
                deal = random.choice(['Deal','No_Deal'])
                if deal == 'Deal':
                    typewriter(colorama.Fore.MAGENTA + 'You raise your hands...')
                    typewriter('You: YOO HOMIE RELAX I DIDN’T KNOW YOU GUYS OWN THIS PLACE I’M OUT\nLizard: Alright homie just don’t let me see you here again')
                    typewriter('\nYOOUUUU WINNN!!!!!')
                elif deal == 'No_Deal':
                    typewriter(colorama.Fore.MAGENTA + 'You raise your hands...')
                    typewriter('\nYou: YOO HOMIE RELAX I DIDN’T KNOW YOU GUYS OWN THIS PLACE I’M OUT\nLizard: You’ll negotiate with God bitch')
                    print(colorama.Fore.RED + '\nGAMEOVER' + colorama.Fore.RESET)
            
            elif gang == '3':
                disarm = random.choice(['Disarmed','Failed'])
                if disarm == 'Disarmed':
                    typewriter(colorama.Fore.MAGENTA + 'You strike downward on the hand...\n')
                    sleep(1)
                    typewriter('Gun drops')
                    sleep(2)
                    typewriter('\nLizard screams: AH YOU LITTLE BITCH tries to punch you but you dodge and counter')
                    sleep(1.5)
                    typewriter('\nYou hit him in the liver and he goes down')
                    sleep(1.5)
                    typewriter('\nYou grab the gun and unload the whole mag into the lizard' + colorama.Fore.RESET)
                    typewriter('\nYOU WIIIIN SCHKAAA')
                elif disarm == 'Failed':
                    typewriter(colorama.Fore.RED + 'You tried to knock the gun out but got shoved and shot in the head')
                    sleep(2)
                    typewriter('\nLizard: HA HA HA FUNNY FUCKIN HOMIE')
                    sleep(1)
                    typewriter('\nGAMEEE OVERRR LOXXX' + colorama.Fore.RESET)
