#lets create vir env - libmgmt
#activate - source venv/bin/activate
#installing colorama pyfiglet

from colorama import Style, Fore, init # pyright: ignore[reportMissingImports]
import os

init(autoreset=True) # Initialize Colorama with auto-reset enabled

# class to represent a user

class User:
    def __init__(self, username):
        self.username = username
        
        
# lib class 
class Library:
    def __init__(self, file_name="users.txt"):
        self.file_name = file_name
        self.logged_in_user = None
        
    def login(self, username):
        try:
            
            if not os.path.exists(self.file_name):
                open(self.file_name, 'w').close()
                
            with open(self.file_name, 'r') as file:
                users = file.read().splitlines()
            
            if username in users:
                self.logged_in_user = User(username)
                print(Fore.GREEN + f'Welcome Back, {username}!')
            else:
                print(Fore.YELLOW + f'Username: {username} that you are looking for doesnt exits. Creating New One')
                with open(self.file_name, 'a') as file:
                    file.write(username + '\n')
                self.logged_in_user = User(username)
                print(Fore.GREEN + f'Username: {username} Successfully Created & Logged IN!')
        # handles any exception (raise)
        except Exception as e:
            print(Fore.RED + f'Sorry Login Failed ! {e}')
            
    def logout(self):
        if self.logged_in_user:
            print(Fore.CYAN + f'Thankyou See ya Later!,  {self.logged_in_user.username}')
            self.logged_in_user = None
        else:
            print(Fore.YELLOW + f'No User Online!')
    
    def check_status(self):
        if self.logged_in_user:
            print(Fore.BLUE + f'User Online!: !,  {self.logged_in_user.username}')
        else:
            print(Fore.YELLOW + f'No User Online!')
        
            
                