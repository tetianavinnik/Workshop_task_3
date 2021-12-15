import random

comp_field = []
users_field = []
comp_field_for_display = []
comp_ships_list = []
kil_field = []
alf = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
memory = []
q = []


def Random_field(n):
    # filling the playing field
    pass


def Choise():
    # function in which the user selects his playing field


def main():
    # main function with gameplay
    print("Hi welcome to the best Battleship game ever.There are some rules you have to know: ")
    print("1. You will have 2 field: one yours and another computers")
    print("2. you have to shoot on ships like that: H6")
    print("Have a nice game!!!")

        users_field = Choise()
    comp_field = Random_field(1)
    for i in range(12):
        temp = []
        for j in range(12):
            temp.append('.')
        comp_field_for_display.append(temp)
    user_field_for_comp = []
    for i in range(12):
        temp = []
        for j in range(12):
            temp.append('.')
        user_field_for_comp.append(temp)

    print("Good luck!")
    comp_ships = 20
    users_ships = 20
    while (True):

        correct = False
        I = 0
        J = 0
        while (correct == False):
            # input of coordinates
            rez = ''
            rezComp = ''
            print("Please enter coordinates:")
            st = input(" ")
            if st == 'exit':
                print("Bye")  # quitting the game
                return
            if len(st) > 2 or len(st) < 2 or (not (st[0] >= 'A' and st[0] <= 'J')) or (
            not (st[1] >= '0' and st[1] <= '9')):
                print("Error, please try again. Your coordinates shood be like this: A7")
            else:
                repet = False
                for i in range(len(memory)):
                    if memory[i] == st:
                        repet = True
                if repet == False:
                    correct = True
                    for i in range(10):
                        if alf[i] == st[0]:
                            J = i + 1
                            break
                    I = int(st[1]) + 1
                    memory.append(st)
                else:
                    print("You have already shot in this area")
        # shot at coordinates
        if comp_field[I][J] == '.':
            comp_field_for_display[I][J] = '+'
            rez = 'Miss'
        else:
            if comp_field[I][J] == '#':
                tempI = 0
                for i in range(10):
                    for j in range(len(comp_ships_list[i])):
                        if comp_ships_list[i][j][0] == I and comp_ships_list[i][j][1] == J:
                            comp_ships_list[i].remove((I, J))
                            tempI = i
                            break
                comp_ships -= 1
                comp_field_for_display[I][J] = 'X'
                if len(comp_ships_list[tempI]) == 0:
                    rez = 'Kill'
                    comp_field[I][J] = '.'
                    for i in range(1, 11):
                        for j in range(1, 11):
                            if comp_field_for_display[i][j] == 'X' and comp_field[i - 1][j] != '#' and comp_field[i + 1][j] != '#' and comp_field[i][j - 1] != '#' and comp_field[i][j + 1] != '#' and comp_field[i - 1][j - 1] != '#' and comp_field[i - 1][j + 1] != '#' and comp_field[i + 1][j - 1] != '#' and comp_field[i + 1][j + 1] != '#':
                                if comp_field_for_display[i - 1][j] != 'X': comp_field_for_display[i - 1][j] = '+'
                                if comp_field_for_display[i + 1][j] != 'X': comp_field_for_display[i + 1][j] = '+'
                                if comp_field_for_display[i][j - 1] != 'X': comp_field_for_display[i][j - 1] = '+'
                                if comp_field_for_display[i][j + 1] != 'X': comp_field_for_display[i][j + 1] = '+'
                                if comp_field_for_display[i - 1][j - 1] != 'X': comp_field_for_display[i - 1][
                                    j - 1] = '+'
                                if comp_field_for_display[i - 1][j + 1] != 'X': comp_field_for_display[i - 1][
                                    j + 1] = '+'
                                if comp_field_for_display[i + 1][j - 1] != 'X': comp_field_for_display[i + 1][
                                    j - 1] = '+'
                                if comp_field_for_display[i + 1][j + 1] != 'X': comp_field_for_display[i + 1][
                                    j + 1] = '+'
                else:
                    rez = 'Damage'
                    comp_field[I][J] = '.'

        # computer step
        if len(q) == 0:
            no_shoot_yet = False
            I = 0
            J = 0
            while no_shoot_yet == False:
                I = random.randint(1, 10)
                J = random.randint(1, 10)
                if users_field[I][J] != 'X' and users_field[I][J] != '+':
                    no_shoot_yet = True
            if users_field[I][J] == '.':
                user_field_for_comp[I][J] = '*'
                users_field[I][J] = '+'
                rezComp = 'Miss'
            else:
                users_field[I][J] = 'X'
                users_ships -= 1
                flag = False
                if users_field[I - 1][J] == '#':
                    q.append((I - 1, J))
                    user_field_for_comp[I - 1][J] = '*'
                    flag = True
                if users_field[I + 1][J] == '#':
                    q.append((I + 1, J))
                    user_field_for_comp[I + 1][J] = '*'
                    flag = True
                if users_field[I][J - 1] == '#':
                    q.append((I, J - 1))
                    user_field_for_comp[I][J - 1] = '*'
                    flag = True
                if users_field[I][J + 1] == '#':
                    q.append((I, J + 1))
                    user_field_for_comp[I][J + 1] = '*'
                    flag = True
                if flag == False and len(q) == 0:
                    rezComp = 'Kill'
                    if users_field[I - 1][J] != 'X': users_field[I - 1][J] = '+'
                    if users_field[I + 1][J] != 'X': users_field[I + 1][J] = '+'
                    if users_field[I][J - 1] != 'X': users_field[I][J - 1] = '+'
                    if users_field[I][J + 1] != 'X': users_field[I][J + 1] = '+'
                    if users_field[I - 1][J - 1] != 'X': users_field[I - 1][J - 1] = '+'
                    if users_field[I - 1][J + 1] != 'X': users_field[I - 1][J + 1] = '+'
                    if users_field[I + 1][J - 1] != 'X': users_field[I + 1][J - 1] = '+'
                    if users_field[I + 1][J + 1] != 'X': users_field[I + 1][J + 1] = '+'
                    user_field_for_comp[I - 1][J] = '*'
                    user_field_for_comp[I + 1][J] = '*'
                    user_field_for_comp[I][J - 1] = '*'
                    user_field_for_comp[I][J + 1] = '*'
                    user_field_for_comp[I - 1][J - 1] = '*'
                    user_field_for_comp[I - 1][J + 1] = '*'
                    user_field_for_comp[I + 1][J - 1] = '*'
                    user_field_for_comp[I - 1][J + 1] = '*'

                else:
                    rezComp = 'Damage'
        else:
            a = q.pop(0)
            users_ships -= 1
            I = a[0]
            J = a[1]

            users_field[I][J] = 'X'
            flag = False
            if users_field[I - 1][J] == '#':
                q.append((I - 1, J))
                user_field_for_comp[I - 1][J] = '*'
                flag = True
            if users_field[I + 1][J] == '#':
                q.append((I + 1, J))
                user_field_for_comp[I + 1][J] = '*'
                flag = True
            if users_field[I][J - 1] == '#':
                q.append((I, J - 1))
                user_field_for_comp[I][J - 1] = '*'
                flag = True
            if users_field[I][J + 1] == '#':
                q.append((I, J + 1))
                user_field_for_comp[I][J + 1] = '*'
                flag = True
            if flag == False and len(q) == 0:
                rezComp = 'Kill'
                for i in range(1, 11):
                    for j in range(1, 11):
                        if users_field[i][j] == 'X':
                            if users_field[i - 1][j] != 'X': users_field[i - 1][j] = '+'
                            if users_field[i + 1][j] != 'X': users_field[i + 1][j] = '+'
                            if users_field[i][j - 1] != 'X': users_field[i][j - 1] = '+'
                            if users_field[i][j + 1] != 'X': users_field[i][j + 1] = '+'
                            if users_field[i - 1][j - 1] != 'X': users_field[i - 1][j - 1] = '+'
                            if users_field[i - 1][j + 1] != 'X': users_field[i - 1][j + 1] = '+'
                            if users_field[i + 1][J - 1] != 'X': users_field[i + 1][j - 1] = '+'
                            if users_field[i + 1][j + 1] != 'X': users_field[i + 1][j + 1] = '+'
                            user_field_for_comp[i - 1][j] = '*'
                            user_field_for_comp[i + 1][j] = '*'
                            user_field_for_comp[i][j - 1] = '*'
                            user_field_for_comp[i][j + 1] = '*'
                            user_field_for_comp[i - 1][j - 1] = '*'
                            user_field_for_comp[i - 1][j + 1] = '*'
                            user_field_for_comp[i + 1][j - 1] = '*'
                            user_field_for_comp[i - 1][j + 1] = '*'
            else:
                rezComp = 'Damage'

        # playing field output
        print('  A B C D E F G H I J             A B C D E F G H I J')
        for i in range(1, 11):
            print(i - 1, end=' ')
            for j in range(1, 11):
                print(comp_field_for_display[i][j], end=' ')

            print('         ', end=' ')

            print(i - 1, end=' ')
            for j in range(1, 11):
                print(users_field[i][j], end=' ')

            print()

        print(rez, ': ', st, '                             ', rezComp, ': ', alf[J - 1], I - 1, sep='')

        if comp_ships == 0:
            # displaying the result of the game when the player wins
            print("""YOU WON! GOOD JOB!!!""")
            return

        if users_ships == 0:
            # displaying the result of the game when the computer wins
            print("""YOU LOST.Try again(""")



if __name__ == '__main__':
    main()