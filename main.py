
#importing our module library.py


from library import Library
import pyfiglet
from colorama import Fore, Style, init


init(autoreset=True) # Initialize Colorama with auto-reset enabled

#creating obj
lib = Library()


#display welcome banner
print(Fore.YELLOW + pyfiglet.figlet_format('!!  Welcome To our Lib MGMT SYS !!'))


#lopp - while 

while True:
    print(Fore.RED + '\nPlease Choose From Menu Items:')
    print('1. Login')
    print('2. Logout')
    print('3. Check Login Status')
    print('3. Add Book To Lib')
    print('3. View All Books')
    print('4. Exit')
    
    
    try:
        choice = int(input('Select The Menu Items: '))
        
        if choice == 1:
            username = input('Please Enter your Username: ')
            lib.login(username)
        elif choice == 2:
            lib.logout()
        elif choice == 3:
            lib.check_status()
        elif choice == 4:
            print(Fore.GREEN + f'{username} Exiting the MATRIX! GOODBYE!!') 
            break
        else:
            print(Fore.RED + 'Invalid Choice- Please Choose Form 1 - 4')
    
    except ValueError:
        print(Fore.RED + 'Please Enter a Valid Number....')
        
        

            

