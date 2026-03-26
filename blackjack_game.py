import re 
import os
import deckofcards

SAVE_FILE = "save.txt"

def validate_user():
    pattern = re.compile(r"^[a-zA-Z0-9]{3,10}$")
    while True: 
        name = input("Enter name ")
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
                data = f.read().split(",")
                return data[0], int(data[1])
        return None, 1000

def get_hand_score(hand):
    values = [c.value() for c in hand]
    is_ace = [c.rank == 'A' for c in hand]
    total = sum(values)
    for i in range(len(values)):
        if total > 21 and is_ace[i]:
            total -= 10
    return total 

def play_game():
    name, balance = file_operations(mode='read')
    if not name or balance <= 0:
        name = validate_user()
        balance = 1000
        while balance > 0:
            file_operations(name, balance, mode='write')
            break

    deck = deckofcards.deck()
    print(f"\n-Welcome {name}. Balance: £{balance}-")
    while balance > 0:
        try:
            bet = int(input(f"\nEnter bet (Balance: £{balance}): "))
            if bet > balance or bet <= 0: raise ValueError
        except ValueError:
            print("Invalid bet.")
            continue
        player_hand = [deck.deal(), deck.deal()]
        dealer_hand = [deck.deal(), deck.deal()]

        while True:
            pscore = get_hand_score(player_hand)
            print(f"\nYour hand: {' '.join(map(str, player_hand))} - Score: {pscore}")
            print(f"Dealer shows: {dealer_hand[1]}")
            if pscore >= 21: break
            move = input("Hit or Stand? ").lower()
            if move == 'h':
                player_hand.append(deck.deal())
            elif move == 's':
                break

        pscore = get_hand_score(player_hand)
        if pscore > 21:
            print("Bust! Dealer wins.")
            balance -= bet
        else:
            dscore = get_hand_score(dealer_hand)
            print(f"\nDealer shows:{' '.join(map(str, dealer_hand))}")
            while dscore < 17:
                print("Dealer hits.")
                dealer_hand.append(deck.deal())
                dscore = get_hand_score(dealer_hand)
                print(f"Dealer has: {' '.join(map(str, dealer_hand))} (Score: {dscore})")

            if dscore > 21:
                print("Dealer Busts! You win!")
                balance += bet
            elif pscore > dscore:
                print("You win.")
                balance +=bet
            elif dscore > pscore:
                print ("Dealer wins.")
                balance -=bet
            else:
                print("Push.")
        
        file_operations(name, balance, mode='write')
        again = input(f"\nDare to play again? (y/n): ").lower() 
        if again != 'y':
            print(f"Well played {name}. Final Balance: £{balance}")
            break
        if balance <= 0:
            print("The house won. Game Over.")
            name = None
            break
            
if __name__ == "__main__":
    play_game()