# printing texts in different colors using termcolor package

import os#this and the next line is also needed to print the color for windows
os.system('color')
from termcolor import colored
print(colored('Hello, World!','red'))
print(colored('Hello, World!','yellow'))
print(colored('Hello, World!','cyan'))
print(colored('Hello, World!','green'))
print(colored('Hello, World!','blue'))
print(colored('Hello, World!','magenta'))
