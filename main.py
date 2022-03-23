from datetime import datetime
from habits import *
from database import *
from instructions import message
from analyze import *

def main():
    '''
    Main loop of the program; takes commands from users, executes functions/methods.
    Creates instances of classes to achieve this.
    '''
    
    instructions = message()
    instructions.help()
    commands = ['exit', 'create daily', 'create weekly', 'delete', 'complete',
                'view daily', 'view weekly', 'view', 'view lifetime', 
                'streak best', 'streak', 'clear', 'help']
    
    exit = False
    while exit != True:
        user_input = input("\n>> ").casefold()

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
            viewLifetime()
            rowid = input("Which habit would you like to delete? (choose its number): ")
            habit = HabitChangeState(rowid, "Deleted")
            habit.delete()
        elif user_input == commands[4]:
            view()
            rowid = input("Which habit will you mark as complete?: ")
            date_completed = datetime.now()
            habit = HabitChangeState(rowid)
            habit.Completed(date_completed)
            
        elif user_input == commands[5]:
            viewDaily()
        elif user_input == commands[6]:
            viewWeekly()
        elif user_input == commands[7]:
            view()
        elif user_input == commands[8]:
            viewLifetime()
        elif user_input == commands[9]:
            streakBest()
        elif user_input == commands[10]:
            rowid = input("Which habit do you want to see the streak for?: ")
            streak(rowid)
        elif user_input == commands[11]:
            clear()
        elif user_input == commands[12]:
            instructions.help()
        else:
            print("Invalid command; the program will end now.")
            exit = True

if __name__ == '__main__':
    main()
