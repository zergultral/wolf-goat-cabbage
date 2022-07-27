master = 0
wolf = 0
goat = 0
cabbage = 0
day = 0
while True:
    day += 1
    print(day)
    print('===============')
    if master == 0:
        print(' __M ----- ___ ')
    else:
        print(' ___ ----- M__ ')
    if wolf == 0:
        print(' __W ----- ___ ')
    else:
        print(' ___ ----- W__ ')
    if goat == 0:
        print(' __G ----- ___ ')
    else:
        print(' ___ ----- G__ ')
    if cabbage == 0:
        print(' __C ----- ___ ')
    else:
        print(' ___ ----- C__ ')
    print('===============')
    if master == wolf == goat == cabbage == 1:
        print('YOU WIN!')
        break
    elif wolf == goat != master:
        print('WOLF ATE GOAT! YOU LOSE!')
        break
    elif goat == cabbage != master:
        print('GOAT ATE CABBAGE! YOU LOSE!')
        break
    command = input()
    if command == '0':
        if master == 0:
            master = 1
        else:
            master = 0
    elif command == 'w':
        if master == wolf == 0:
            master = wolf = 1
        elif master == wolf == 1:
            master = wolf = 0
        else:
            print('wolf not available')
    elif command == 'g':
        if master == goat == 0:
            master = goat = 1
        elif master == goat == 1:
            master = goat = 0
        else:
            print('goat not available')
    elif command == 'c':
        if master == cabbage == 0:
            master = cabbage = 1
        elif master == cabbage == 1:
            master = cabbage = 0
        else:
            print('cabbage not available')
    else:
        day -= 1
        print('unknown command')