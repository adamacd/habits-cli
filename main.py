from datetime import datetime
from habits import *
from database import *
from instructions import instructions_message

def main():
    instructions_message()
    commands = ['exit', 'create daily', 'create weekly', 'delete', 'complete',
                'view daily', 'view weekly', 'view', 'view lifetime', 
                'streak best', 'streak', 'clear', 'help'
    ]
    
    exit = False
    while exit != True:
        user_input = input(">> ").casefold()

        if user_input == commands[0]:
            print("\nThe program has ended.")
            exit = True
        elif user_input == commands[1]:
            description = input("Briefly describe the habit you want to create: ")
            created = datetime.now()
            habit = Habit(description, created)
            habit.createDaily()
        elif user_input == commands[2]:
            description = input("Briefly describe the habit you want to create: ")
            created = datetime.now()
            habit = Habit(description, created)
            habit.createWeekly()
        elif user_input == commands[3]:
            pass
        elif user_input == commands[4]:
            pass
        elif user_input == commands[5]:
            pass
        elif user_input == commands[6]:
            pass
        elif user_input == commands[7]:
            #view
            pass
        elif user_input == commands[8]:
            pass
        elif user_input == commands[9]:
            pass
        elif user_input == commands[10]:
            pass
        elif user_input == commands[11]:
            pass
        elif user_input == commands[12]:
            pass
        elif user_input == commands[13]:
            pass
        else:
            print("Bad Input")
            exit = True

if __name__ == '__main__':
    main()
