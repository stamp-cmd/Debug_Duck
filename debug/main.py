#Import Libraries
from time import sleep
from os import system
#main function
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
    #Ask if Run or not
    Play = False
    while (Play == False):
        run = input("Run (Y/n): ")
        if (run == "Y" or run == "y"):
            #Run
            system("cls||clear")
            Play = True
        elif (run == "N" or run == "n"):
            #Quit
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
            #Wrong choices
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
    #Step1: State
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
    #Step2: State
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
    #Ask if Use again
    Again = False
    while (Again == False):
        Repeat = input("\nAgain (Y/n): ")
        if (Repeat == "Y" or Repeat == "y"):
            #Repeat the code
            system("cls||clear")
            Play = True
            main()
        elif (Repeat == "N" or Repeat == "n"):
            #Not repeat the code
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
            #Wrong choices
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
#if name is main
if (__name__ == "__main__"):
    main()

"""
  __         _______________
<(o )___  __/ Quack! Quack! \
 ( ._> /    \_______________/
  '---'
  
  --Ducii
  The friendly Assistance.
 """
