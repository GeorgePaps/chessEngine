from bin.initializeBoard import initializeBoard 

def start_new_game():
    print("Starting a new game...")
    move = input("Enter your move: ")
    
def load_game():
    print("Loading a saved game...")

def main():

    print("Welcome to the Chess Game!")
    while True:
        choice = input("Do you want to start a new game or load one? (n/l): ").strip().lower()
        if choice == 'n':
            print(">>> start_new_game()")
            # print(initializeBoard())
            start_new_game()
            break
        elif choice == 'l':
            print(">>> load_game()")
            load_game()
            break
        else:
            print("Please enter 'n' for new game or 'l' to load a game.")

if __name__ == "__main__":
    main()