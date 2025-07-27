
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
    print('4. Add Book To Library')
    print('5. View Books')
    print('6. Exit')
    
    
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
            title = input('Enter A Title: ')
            lib.add_book(title)
        elif choice == 5:
            lib.view_books()
        elif choice ==6:
            print(Fore.GREEN + 'Exiting the Library! GOODBYE!!') 
            break
        else:
            print(Fore.RED + 'Invalid Choice- Please Choose Form 1 - 4')
    
    except ValueError:
        print(Fore.RED + 'Please Enter a Valid Number....')
        
        

            

