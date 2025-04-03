# complexity

import subprocess

def main():
    while True:
        choice = input("Do you want to start a new game (n) or load one (l)? ").lower()
        
        if choice == 'n':
            # Call the script for starting a new game
            subprocess.run(['python', 'new_game.py'])
            break
        elif choice == 'l':
            # Call the script for loading a game
            subprocess.run(['python', 'load_game.py'])
            break
        else:
            print("Invalid choice. Please enter 'n' for new game or 'l' to load.")

if __name__ == "__main__":
    main()
