# open ai 
import subprocess

def main()
    while True
        choice = input(Do you want to start a new game or load one (nl) ).strip().lower()
        
        if choice == 'n'
            subprocess.run([python, new_game.py])
            break
        elif choice == 'l'
            subprocess.run([python, load_game.py])
            break
        else
            print(Invalid choice. Please enter 'n' for new game or 'l' to load a game.)

if __name__ == __main__
    main()