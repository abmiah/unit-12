import getpass
import random
import string
import hashlib as hash

#Password Manager Classes section
class PasswordManager:
    """ Main class to declare the initialiser for the Password Manager.
    Since it requires user input with 'self', it does not require any arguments. """
    def __init__(self):
        self.master_password_hash = None
        """ An empty dictionary is created to sort the user password input. 
        This is further developed in 'show_entries' method. """
        self.password = {}

    """ The method below sets up the 'Master Password' if the user has not already 
    set one. The 'password' variable is stored in 'self.master_password', which is 
    taken from the above initialiser. """
    def set_master_password(self, master_password):
        self.master_password_hash = hash.sha256(master_password.encode()).hexdigest()
        print(f"\nMaster password has been set.\nMaster Password Encrypted: {self.master_password_hash}\n")

    """ Method section that adds the entry to the password manager, first it checks if 
    user has set a 'master password' before accepting any entries. The password is also
    saved as an encryption using the 'hashlib - sha256' module to add an additional layer of 
    security in case of a breach. """
    def add_entry(self, website, username, password):
        if self.master_password_hash is None:
            print("Please enter Master Password.\n")
            return

        password_hash = hash.sha256(password.encode()).hexdigest()
        self.password[website] = {
            "username": username,
            "password": password
        }

        print(f"\nEntry for has been added.")
        print(f"Website: {website}")
        print(f"Username: {username}")
        print(f"Password encrypted: {password_hash}\n")

    """ Method that shows the stored entries, first it checks whether the 'Master Password' has 
    been set, and checks if there are any stored entries. Any stored entries will
    be saved in a dictionary in the 'self.password' initialiser. """
    def show_entries(self):

        if self.master_password_hash is None:
            print("\nEnter Master Password\n")
            return

        if not self.password:
            print("\nNo entry was found.\n")
            return

        for website, data in self.password.items():
            print(f"\nWebsite: {website}")
            print(f"Username: {data['username']}")
            print(f"Password: {data['password']}")
            print("\n")


#Password Generator Class
class RandomPasswordGenerator:
    """ This class will generate a random password that has a mixture of letters (A to Z),
    numbers (0 - 9) and symbols obtained from the 'string' and 'random' modules. """
    def __init__(self):
        """ The initialiser below is obtained from 'string' module, reference taken from
        https://docs.python.org/3/library/string.html """
        self.letters = list(string.ascii_letters)
        self.numbers = list(string.digits)
        self.punctuation = list(string.punctuation) #"!@£#$%^&*()_+"
    
    def user_password_input(self):
        """ This section allows users to enter the password length using a while loop.
        The loop also checks that users entries a number with a 'try' and 'except' function. """
        while True:
            try:
                user_input = int(input("\nPlease enter the length of your password: "))
                number_of_characters = user_input
                if number_of_characters < 8:
                    print("Password should be at least 8 characters long")
                else:
                    return number_of_characters
            except ValueError:
                print(f"Please only use numbers.\n")

    def generate_password(self):
        characters = self.letters + self.numbers + self.punctuation
        password = "".join(random.choice(characters)
                                      for _ in range(self.user_password_input()))
        return password


#Terminal Demo
if __name__ == "__main__":
    password_manager = PasswordManager()
    password_generator = RandomPasswordGenerator()

    """ The while loop below is taken in the user option for the pass manager program. """
    while True:
        print("1. Enter Master Password")
        print("2. Add Entry")
        print("3. Get Account & Password Entries")
        print("4. Generate a password")
        print("5. Exit", end="\n")

        users_choice = input("Please enter you choice: ")

        if users_choice == "1":
            if password_manager.master_password_hash is None:
                print("\nMaster Password is not set.")
                master_password = getpass.getpass("Please set your Master Password: ")
                password_manager.set_master_password(master_password)
            else:
                print("Master password is already set.")
                password_manager.show_entries()

        elif users_choice == "2":
            while True:
                if password_manager.master_password_hash is None:
                    print("\nPlease set Master Password\n")
                    master_password = getpass.getpass("Password: ")
                    password_manager.set_master_password(master_password)

                else:
                    website = input("\nEnter website name: ")
                    username = input("Enter username: ")
                    password = password_generator.generate_password()
                    password_manager.add_entry(website, username, password)
                    break

        elif users_choice == "3":
            password_manager.show_entries()

        elif users_choice == "4":
            password = password_generator.generate_password()
            print(f"\nGenerated Password: {password}\n")


        elif users_choice == "5":
            print("\nThank you for using Password Manager")
            break

        else:
            print("\nPlease try again, that is an invalid choice")