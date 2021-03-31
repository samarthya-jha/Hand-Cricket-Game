import random


print('Welcome to Hand Cricket (or Command Line Cricket):')
toss = input('Heads or Tails?')
tosscheck = random.randint(0,1)
user = 0
com = 0
if tosscheck == 0 and toss == 'Heads' or tosscheck == 1 and toss == 'Tails':
    choice = input('You won the toss. Choose Bat or Bowl?')
    if choice == 'Bat':
        print('You are batting')
        while(True):
            num = int(input('Enter your number (1-6)?'))
            rand = random.randint(1,6)
            if num == rand:
                print('Oops. You were bowled out.')
                break
            else:
                user+=num
                print('User score = ',user)
        print('You are bowling. Defend ',user,' runs.')
        while(True):
            num = int(input('Enter your number (1-6)?'))
            rand = random.randint(1,6)
            if num == rand:
                print('Congrats. You bowled the AI out.')
                if com < user:
                    print('Congrats. You won')
                elif com==user:
                    print('A tie.')
                break
            else:
                com+=rand
                print('Computer score = ',com)
                if com > user:
                    print('And you got beat by an AI')
                    break
    else:
        print('You are bowling')
        while(True):    
            num = int(input('Enter your number (1-6)?'))
            rand = random.randint(1,6)
            if num == rand:
                print('Congrats. You bowled the AI out.')
                break
            else:
                com+=rand
                print('Computer score = ',com)
        print('You are batting. Get ',com,' runs.')
        while(True):
            num = int(input('Enter your number (1-6)?'))
            rand = random.randint(1,6)
            if num == rand:
                print('Oops. You were bowled out.')
                if com > user:
                    print('And you got beat by an AI')
                elif com==user:
                    print('A tie.')
                break
            else:
                user+=num
                print('User score = ',user)
                if user > com:
                    print('Congrats. You won')
                    break
else:
    print('Lost the toss. You are bowling')    
    while(True):    
        num = int(input('Enter your number (1-6)?'))
        rand = random.randint(1,6)
        if num == rand:
            print('Congrats. You bowled the AI out.')
            break
        else:
            com+=rand
            print('Computer score = ',com)
    print('You are batting. Get ',com,' runs.')
    while(True):
        num = int(input('Enter your number (1-6)?'))
        rand = random.randint(1,6)
        if num == rand:
            print('Oops. You were bowled out.')
            if com > user:
                print('And you got beat by an AI')
            elif com==user:
                print('A tie.')
            break
        else:
            user+=num
            print('User score = ',user)
            if user > com:
                print('Congrats. You won')
                break