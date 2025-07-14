\import time

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def intro():
    slow_print("Welcome to 'Escape from Techno-Lab'!")
    name = input("What's your name, hero? ")
    slow_print(f"Alright {name}, you’re a hacker who broke into Techno-Lab...")
    slow_print("But now the doors are locked. Security is on the way. You need to escape!")
    first_choice()

def first_choice():
    slow_print("\nYou see two paths:")
    slow_print("1. Left hallway (looks dark and quiet)")
    slow_print("2. Right hallway (you hear robot sounds)")
    choice = input("Where do you go? (1 or 2): ")
    if choice == "1":
        dark_room()
    elif choice == "2":
        robot_guard()
    else:
        slow_print("Invalid choice. Try again.")
        first_choice()

def dark_room():
    slow_print("\nYou’re in a pitch-black server room.")
    slow_print("You hear electric humming. You find a switch on the wall.")
    slow_print("1. Flip the switch")
    slow_print("2. Walk forward slowly")
    choice = input("What do you do? (1 or 2): ")
    if choice == "1":
        slow_print("Zzzap! You turned on the backup power. A hidden door opens!")
        secret_lab()
    elif choice == "2":
        slow_print("You trip on a cable and fall on a laser grid... Game Over ")
        play_again()
    else:
        slow_print("Choose properly.")
        dark_room()

def robot_guard():
    slow_print("\nA robot guard sees you and starts chasing!")
    slow_print("1. Run back and hide")
    slow_print("2. Fight the robot with a nearby metal rod")
    choice = input("What do you do? (1 or 2): ")
    if choice == "1":
        slow_print("You run and barely escape into the vents!")
        vent_escape()
    elif choice == "2":
        slow_print("The robot zaps you with a taser. Game Over ")
        play_again()
    else:
        slow_print("Choose properly.")
        robot_guard()

def secret_lab():
    slow_print("\nYou enter a hidden lab. A computer shows: 'Override door lock?'")
    slow_print("1. Yes")
    slow_print("2. No")
    choice = input("Hack the system? (1 or 2): ")
    if choice == "1":
        slow_print("Access granted! The main exit opens. You win!")
        play_again()
    elif choice == "2":
        slow_print("Why did you come this far then? The lab self-destructs. Game Over ")
        play_again()
    else:
        slow_print("Type 1 or 2.")
        secret_lab()

def vent_escape():
    slow_print("\nYou crawl through the vents. You see a light below a grate.")
    slow_print("1. Jump down")
    slow_print("2. Keep crawling")
    choice = input("What do you do? (1 or 2): ")
    if choice == "1":
        slow_print("You land inside a security control room!")
        secret_lab()
    elif choice == "2":
        slow_print("You keep crawling... and fall through a broken vent. Game Over ")
        play_again()
    else:
        slow_print("Choose properly.")
        vent_escape()

def play_again():
    choice = input("\nDo you want to try again? (yes or no): ").lower()
    if choice == "yes":
        intro()
    elif choice == "no":
        slow_print("Thanks for playing! Goodbye, hacker")
    else:
        play_again()

# Start the game
intro()
