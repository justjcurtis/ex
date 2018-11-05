from os import system, name
from tabulate import tabulate

def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def displayMenu(menu, available_commands):
    inputting = True
    while inputting:
        clear()
        inputting = False
        print(tabulate(menu[1:], menu[0]))
        print()
        print("enter help to see syntax and command options")
        print("enter back to go back to main menu")
        print("Please enter command below")
        print()
        command = input("=> ")
        if (command == "back" or command == "b"):
            return "back"
        if(command == "help" or command == "h"):
            inputting = True
            _help(available_commands)
            continue
        try:
            command = command.split(" ", 1)
            command[0] = command[0].lower()
            command[1] = int(command[1])-1
        except:
            inputting = True
            print()
            print("malformed command")
            input("press enter to continue")
            continue
        if(command[1] < 0 or command[1] > len(menu)-2):
            inputting = True
            print()
            print(menu[0][1] + " number not valid")
            input("press enter to continue")
            continue

    return command


def _help(available_commands):
    print()
    print("current commands are")
    print()
    print(available_commands)
    print()
    print("eg. => " + available_commands[0] + " 1")
    print("or     " + available_commands[0][0] + " 1")
    print()
    input("press enter to continue")
    print()
