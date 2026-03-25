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
        