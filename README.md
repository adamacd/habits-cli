# Habit Tracker CLI
This command line interface allows you to create, view, and delete habits. You can accumulate streaks if you mark them as complete in the given time (24 hrs if daily, 168 hrs if weekly). The habits are stored locally in a SQLite database.

# Starting the program
Run main.py from the command line.

Alternatively:
1. Navigate to where you downloaded the files
2. shift+right click to open a powershell window
3. type python3 main.py

# Using the program
When you run the program, the command list will appear. Type a command, and follow the instructions on the screen.
| Command | Description |
| ----------- | ----------- |
| create daily | Creates a daily habit |
| create weekly | Creates a weekly habit |
| complete | Mark a habit as complete |
| delete | Delete a habit |
| | |
| view daily | View all current daily habits |
| view weekly | View all current weekly habits |
| view | View all currently tracked habits |
| view lifetime | View current and expired habits |
| streak best | See which habit you kept longest |
| streak | See streak for a certain habit |
| | |
| clear | Clear all habit data |
| exit | Exit the program |
| help | See the list of commands |

### Examples

create daily

(The program will ask you to describe the habit) Briefly describe the habit you want to create: (Type the habit here)

(Use another command or type exit to stop the program)

---

view daily

(A list of your daily habits will appear)

---

streak

(The program will ask you to select a streak by its ID number)

## Author
[@AdamACD](https://github.com/adamacd)

I created this project for an assignment in my OOP course.
