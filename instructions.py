class text:
    '''Provide decoration and commands list for instructions message'''
    def line():
        return "________________________________________________"
    
    def commandList():
        print("* * Available Commands (without quotation marks):\n\n" +\
            "*Creates a daily habit             'create daily'\n" +\
            "*Creates a weekly habit            'create weekly'\n" +\
            "*Mark a habit as complete          'complete'\n" +\
            "*Delete a habit                    'delete'\n\n" +\
            "*View all current daily habits     'view daily'\n" +\
            "*View all current weekly habits    'view weekly'\n" +\
            "*View all currently tracked habits 'view'\n" +\
            "*View current and expired habits   'view lifetime'\n" +\
            "*See which habit you kept longest  'streak best'\n" +\
            "*See streak for a certain habit    'streak'\n\n" +\
            "*Clear all habit data              'clear'\n" +\
            "*Exit the program                  'exit'\n" +\
            "*See this command list again       'help'")
        
class message(text):
    '''
    Provide instructions 
    for the user for when they run main.py
    '''
    
    def help(self):
        '''Tells the user about the commands available to them.'''
        print("\n* * Habit Tracker Command Line Interface * *\n"+ text.line())
        
        text.commandList()
        
        print(text.line() + "\nThe program is running. Enter your command >>")


