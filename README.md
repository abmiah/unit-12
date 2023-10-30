# Unit 12 – End of Module Assignment: EMA: OOP application of principles and concepts


**The program proposal** 
The program uses Python libraries to create and store passwords for the password manager program. For more details, refer to the documentation on this site [https://docs.python.org/](https://docs.python.org/) and the code section below.

The goal is to store and generate strong passwords securely.

**Code Explanation**
1.	The code starts with implementing four Python modules: 

`getpass` allows users to input a password without it being displayed. 

`random` selects elements from a `list` using the `choice()` method. 

The `string` module is used alongside the `random.choice()` method as the library has pre-defined `strings`, `integers` and symbols. 

The `hashlib` module uses the `sha256()` method to produce a hexadecimal `string` resulting in the encryption of any random password created from the `string` module. 

2.	The `PasswordManager` class has two initialisers allowing users to store and generate passwords. `self.master_password_hash` is set to `None` allowing users to encrypt their master password using `hash.sha256()`. `self.password = {}` is an empty dictionary that allows users to input a website name, username, and password.  

3.	A setter method `set_master_password()` is created to store the encrypted master password in `self.master_password_hash`. It uses `hash.sha256(master_password.encode()).hexdigest()` to convert the password string to hexadecimal.

4.	The `add_entry()` method in the `PasswordManager` class checks for a master password before storing the website, username and password in an empty dictionary `self.password`. The password is hashed using `sha256()` and saved in the `password_hash` variable. `

5.	The method `def show_entries(self)`, stored within the `PasswordManager` class, gets the stored entries from the `def add_entry` method, checking first for a master password in an `if` statement, once the master password has been established a `for loop` will loop through the `self.password` dictionary and output the stored data. 

6.	A new `class RandomPasswordGenerator` is created to produce a random password using a mixture of `string` (uppercase and lowercase) `integers` and symbols obtained from the `string` module. The class initialisers are assigned to a `list`. 

7.	A method of `def user_password_input(self)` uses a combination of `while loop` to get the user input of the length of the password and `try` and `except` block, which handles any error that the user may cause for example entering a password length that less than eight characters long or entering a non `integer` input. 

8.	The final method within the class `def generate_password(self)` obtains the data from the `list` variables saved in the main initialisers to `characters` and then the variable `password` using the `.join()` function that converts `list` items into a single string with `random.choice(characters)`. This is then looped using the input from `user_password_input` to return the final password.

9.	The final test phase first initialises `if __name__ == “__main__”:` so the file will run as a script. The two classes are saved as two objects, `password_manager = PasswordManager()` and `password_generator = RandomPasswordGenerator()` a `while loop`, with `if`, `elif` and `else` statements asking the user to select from five options. 

•	Option 1 sets the master password obtained from the object `password_manager = PasswordManager()` with an `if` and `else` statement checking the master password and entries. 

•	Option 2 adds an entry; it runs a `while loop` checking for the master password within an `if` and `else` statement. The password is generated from the `password_generator` object.

•	Option 3  shows the user entries from the `show_entries()` method.

•	Option 4 generates a random password from the `password_generator = RandomPasswordGenerator()` object. 

•	Option 5 exits the programme with a `break` function to stop the `while loop`.

•	A final `else` statement checks if a user enters a wrong input.