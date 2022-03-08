import time
from habits import *
from instructions import instructions_message
#create daily
#create weekly
#delete

def main():
    instructions_message()
    exit = False
    commands = [
        'exit',
        'create daily',
        'create weekly',
        'delete'
    ]
    while exit != True:
        user_input = input(">> ").casefold()

        if user_input == commands[0]:
            print("\nThe program has ended.")
            exit = True
        elif user_input == commands[1]:
            description = input("Briefly describe the habit you wish to create: ")
            datetime_created = input("(24 hr clock) Around what time should the habit occur?: ")
            
            print(f"\nThe habit '{description}' was created.\nIt occurs at around {datetime_created} each day.")
        else:
            pass

if __name__ == '__main__':
    main()

'''
    quit = False
    start_of_streak = 0
    end_of_streak = 0
    while quit != True:
        x = input("> ")
        if x=="make daily":
            ok = time.localtime()
            start_of_streak = time.mktime(ok)
        elif x=="complete":
            nibba = time.localtime()
            end_of_streak = time.mktime(nibba)
            print("seconds from creation to completion: " + (end_of_streak - start_of_streak))
            x = time.strftime("%Y-%m-%d, %H:%M:%S") # givez date n time of completion
            quit = True
'''