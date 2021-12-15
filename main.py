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
    def Random_field(n):
        # filling the playing field
        field = []
        for i in range(12):
            temp = []
            for j in range(12):
                temp.append('.')
            field.append(temp)

        ships = [4, 3, 2, 1]
        for k in range(3, -1, -1):
            t = ships[k]
            while t > 0:
                t -= 1
                done = False
                while (done == False):
                    napr = random.randint(1, 2)
                    if napr == 1:
                        I = random.randint(1, 10)
                        J = random.randint(1, 7)
                        chek = True
                        for i in range(I - 1, I + 2):
                            for j in range(J - 1, J + k + 2):
                                if field[i][j] == '#':
                                    chek = False
                                    break
                        if chek == True:
                            temp = []
                            for j in range(J, J + k + 1):
                                field[I][j] = '#'
                                temp.append((I, j))
                            if n == 1: comp_ships_list.append(temp)

                            done = True
                    else:
                        I = random.randint(1, 6)
                        J = random.randint(1, 10)
                        chek = True
                        for i in range(I - 1, I + k + 3):
                            for j in range(J - 1, J + 2):
                                if field[i][j] == '#':
                                    chek = False
                                    break
                        if chek == True:
                            temp = []
                            for i in range(I, I + k + 1):
                                field[i][J] = '#'
                                temp.append((i, J))
                            if n == 1: comp_ships_list.append(temp)
                            done = True
        return field


def Choise():
    """
    function in which the user selects his playing field
    """
    great_field = False
    while great_field == False:
        users_field = Random_field(0)
        for i in range(1, 11):
            for j in range(1, 11):
                print(users_field[i][j], end=' ')
            print()
        print("""Do you agree with this field?
1 - Yes
2 - No""")
        a = input(">>> ")
        while a != '1' and a != '2':
            print("Error. Try again")
            a = input(">>> ")
        a = int(a)

        if a == 1:
            great_field = True
            print("Great!")
        else:
            print("Generating a new....")
    return users_field

def main():
    # main function with gameplay



if __name__ == '__main__':
    main()