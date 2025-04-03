# grok

def start_new_game():
    print("Starting a new game...")

def load_game():
    print("Loading a saved game...")

def main():
    while True:
        choice = input("Do you want to start a new game or load one? (n/l): ").lower()
        if choice == 'n':
            print(">>> start_new_game()")
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