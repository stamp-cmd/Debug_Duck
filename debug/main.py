from time import sleep; from os import system
def main():
    system("cls||clear")
    print("  __       _______________")
    print("<(o )___ _/ Quack! Quack! \\")
    print(" ( ._> /  \\_______________/")
    print("  '---'")
    print("+------------------------------------+")
    print("| Message:                           |")
    print("| Hi. I'm Ducii. I'm your assistance.|")
    print("| I'm you guide for this Application.|")
    print("+------------------------------------+")
    Play = False
    while (Play == False):
        run = input("Run (Y/n): ")
        if (run == "Y" or run == "y"):
            system("cls||clear")
            Play = True
        elif (run == "N" or run == "n"):
            system("cls||clear")
            print("  __       _______________")
            print("<(o )___ _/ Quack! Quack! \\")
            print(" ( ._> /  \\_______________/")
            print("  '---'")
            print("+------------------------------------+")
            print("| Message:                           |")
            print("| Hi. I'm Ducii. the assistance.     |")
            print("| Bye User. Thanks for trying. Bye!  |")
            print("+------------------------------------+")
            sleep(3)
            run = True
            quit()
        else:
            system("cls||clear")
            run = False
            print("  __       _______________")
            print("<(o )___ _/ Quack! Quack! \\")
            print(" ( ._> /  \\_______________/")
            print("  '---'")
            print("+---------------------------------+")
            print("| Message:                        |")
            print("| Hi. I'm Ducii. the assistance.  |")
            print("| Sorry! You enter wrong choice.  |")
            print("+---------------------------------+")
    system("cls||clear")
    print("  __       _______________")
    print("<(o )___ _/ Quack! Quack! \\")
    print(" ( ._> /  \\_______________/")
    print("  '---'")
    print("+------------------------------------+")
    print("| Message:                           |")
    print("| Hi. I'm Ducii. the assistance.     |")
    print("| Step 1: Explain code line by line  |")
    print("+------------------------------------+")
    Message = input("Explain code line by line: ")
    system("cls||clear")
    print("  __       _______________")
    print("<(o )___ _/ Quack! Quack! \\")
    print(" ( ._> /  \\_______________/")
    print("  '---'")
    print("+------------------------------------+")
    print("| Message:                           |")
    print("| Hi. I'm Ducii. the assistance.     |")
    print("| Step 2: Read the code line by line |")
    print("+------------------------------------+")
    print("Message: " + Message)
    Again = False
    while (Again == False):
        Repeat = input("Again (Y/n): ")
        if (Repeat == "Y" or Repeat == "y"):
            system("cls||clear")
            Play = True
            main()
        elif (Repeat == "N" or Repeat == "n"):
            system("cls||clear")
            print("  __       _______________")
            print("<(o )___ _/ Quack! Quack! \\")
            print(" ( ._> /  \\_______________/")
            print("  '---'")
            print("+------------------------------------+")
            print("| Message:                           |")
            print("| Hi. I'm Ducii. the assistance.     |")
            print("| Bye User. Thanks for using. Bye!   |")
            print("+------------------------------------+")
            sleep(3)
            run = True
            quit()
        else:
            system("cls||clear")
            run = False
            print("  __       _______________")
            print("<(o )___ _/ Quack! Quack! \\")
            print(" ( ._> /  \\_______________/")
            print("  '---'")
            print("+---------------------------------+")
            print("| Message:                        |")
            print("| Hi. I'm Ducii. the assistance.  |")
            print("| Sorry! You enter wrong choice.  |")
            print("+---------------------------------+")
if (__name__ == "__main__"):
    main()

#Almost there...

"""
  __         _______________
<(o )___  __/ Quack! Quack! \
 ( ._> /    \_______________/
  '---'
 """