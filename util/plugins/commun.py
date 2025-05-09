import os
from colorama import Fore

# Color variables
w = Fore.WHITE
b = Fore.BLUE
y = Fore.YELLOW

def setTitle(title: str):
    """Set the console title."""
    if os.name == "nt":  # Windows
        import ctypes
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    else:  # Unix/Linux/MacOS
        print(f'\33]0;{title}\a', end='', flush=True)

def clear():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def nitrogentitle():
    """Print the Nitro Generator title."""
    print(f"""{y}[{w}#{y}]{w} Made by Zenxoxz
{y}[{w}#{y}]{w} Discord Nitro Generator and Checker""")
