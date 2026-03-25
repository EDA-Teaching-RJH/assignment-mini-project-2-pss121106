import re 
import os
import deckofcards

SAVE_FILE = "save.txt"

def validate_user():
    pattern = re.compile(r"^[a-zA-Z0-9]{3,10}$")
    while True: 
        name = input("Enter name")
        if pattern.fullmatch(name):
            return name
        print("Invalid name. Letters or Numbers only!")

def file_operations(name=None, balance=None, mode='read'):
    if mode == 'write':
        with open(SAVE_FILE, "w") as f:
            f.write(f"{name},{balance}")
    else:
        if os.path.exists(SAVE_FILE):
            with open(SAVE_FILE,"r") as f:
                data = f.read().split(,)
                return data[0], int(data[1])
        return None, 1000
        