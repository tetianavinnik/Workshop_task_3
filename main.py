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
            print("Generating a new...")
    return users_field

def main():
    # main function with gameplay



if __name__ == '__main__':
    main()