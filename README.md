<h1>Unit 12 – End of Module Assignment: EMA: OOP application of principles and concepts</h1>


<strong>Project Description and Background:</strong>
To execute a programme base written assignment, which you can find on the following e-portfolio page: [https://abmiah.github.io/eportfolio/posts/individual-essay-unit9.html] (https://abmiah.github.io/eportfolio/posts/individual-essay-unit9.html]) The client is based in East London and recently opened a new store a few miles away to cater to the increasing demand. They want to scale their sales using the latest technology and online shopping system (OSS). However, they are seeking clarification about the setup process and are concerned about the risk of cybercrime. A single cyberattack can severely impact the business, its reputation, and the trust of its customers.

To comply with GDPR, it is advisable to leverage an established delivery service, like Uber Eats, to avoid handling and storing customer data.  Regarding the security proposal, the document emphasises two efficient threat modelling techniques: implementing a password manager and two-factor authentication (2FA). Both measures are both easy to implement and pertinent to a cost-effective solution.


**The program proposal** 
The program uses Python library classes to assist users with creating and storing passwords using a password manager. The program uses the following libraries to allow better efficiency and performance: **getpass**, **random**, **string** and **hashlib**; documentation of these libraries can be found on the following site [https://docs.python.org/] (https://docs.python.org/) and will be further explained in the code section listed below. 

The program's overall objective is to provide users with a way to securely store their passwords while also allowing the program to generate strong passwords not based on common dictionary words.

**OOP Code Explanation** 

All library modules can be found on the Python documentation page on their website: [https://docs.python.org/] (https://docs.python.org/)

1.	The code starts with implementing four Python modules: **getpass**, **random**, **string** and **hashlib**. 

**getpass** module [https://docs.python.org/3/library/getpass.html]( https://docs.python.org/3/library/getpass.html) is used to allow users to input a password without it being displayed. 

**random** module [https://docs.python.org/3/library/random.html]( https://docs.python.org/3/library/random.html) is used to select random elements from a **list** using the **choice()** method. 
**string** module [https://docs.python.org/3/library/string.html]( https://docs.python.org/3/library/string.html) is use alongside the **random.choice()** method as the library has pre-defined **strings**, **integers** and a set of **symbols**, which can be accessed by using **string.punctuation**, with has the following set of symbol **!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~**. 

The **hashlib** module [https://docs.python.org/3/library/hashlib.html]( https://docs.python.org/3/library/hashlib.html) with the use of **sha256** method encrypts string or bytes that produce a hexadecimal string resulting in encryption of any random password created from the **string** module. 

2.	The `class PasswordManager` is declared with the main initializers without the use of any argument, this is solely to allow the users to be able to store and generate passwords from an `input()` function. There are two initializers `self.master_password_hash` which is set to `None` this is to allow users to set a master password that would be encrypted using `hashlib.sha256()` method. The second initializer `self.password = {}` is set with an empty dictionary, this will allow users to implement the website name, username, and password to be stored in a dictionary.  

3.	A class method setter is created `def set_master_password(self, master_password)` to store the encrypted master password `hash.sha256(master_password.encode()).hexdigest()`  in the variable of `self.master_password_hash` from the main initializers. The `hexdidest()` function is used to return the string password in a hexadecimal.

4.	The `def add_entry(self, website, username, password)` method within the `class PasswordManager` first checks if a master password has been set
