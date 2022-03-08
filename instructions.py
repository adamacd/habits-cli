'''The purpose of this file is to create instructions 
for the user when they run main.py'''

class text:
    '''Provide decoration and commands list for welcome message'''
    def line():
        return "________________________________________________"
    
    def commandList():
        print("* * Available Commands (without quotation marks):\n\n" +\
            "*Creates a daily habit             'create daily'\n" +\
            "*Creates a weekly habit            'create weekly'\n" +\
            "*Delete a habit                    'delete'\n\n" +\
            "*View all current daily habits     'view daily'\n" +\
            "*View all current weekly habits    'view weekly'\n" +\
            "*View all currently tracked habits 'view current'\n" +\
            "*View current and expired habits   'view lifetime'\n" +\
            "*See which habit you kept longest  'streak best'\n" +\
            "*See streak for a certain habit    'streak'\n\n" +\
            "*Exit the program                  'exit'\n" +\
            "*See this command list again.      'help'")
        
class instructions_message(text):
    print("\n* * Habit Tracker Command Line Interface * *\n"+ text.line())
    
    text.commandList()
    
    print(text.line() + "\nThe program is running. Enter your command >>")

def exit_message(text):
    print("\nThe program has ended.")
