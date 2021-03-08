name = input('What is your name? ')
print('Hi '+ name)
color = input('what is your favourite colour? ')
print(color + '! Nice Choice '+ name)
birth_year = input('what was your birth year (eg. 1988)? ')
age = 2021 - int(birth_year)
print('Hey ' + name + ' in 2021 you are ' + str(age) + ' years old.')
checker1 = 0
while checker1 == 0:
    weight = int(input('How much is your weight? '))
    unit = input('Is it in (K)g or (L)bs: ')
    if unit.upper() == 'K':
        weight_lbs = weight / 0.45
        print(f"That's nice! did you know your Mr. {color} lover that your weight in lbs is {weight_lbs} pounds.")
        checker1 = 1
    elif unit.upper() == 'L':
        weight_kg = weight * 0.45
        print(f"That's nice! did you know Mr. {color} lover that your weight in kg is {weight_lbs} kilos.")
        checker1 = 1
    else:
        print('Enter either K or L for Kg and lbs respectively')

print(f"Hey {name} Let's play a game.")
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input(f'Guess a number({3-guess_count} attempts left): '))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
    print(f'Sorry {name} but you failed.')

print("Let's play another one.")

print("""Following are rules of game: 
Type any of following as many times as you want and have fun.
start --> to start the car
stop --> stop the car
quit --> quit the game
help --> seek help on how to play""")
command = ""
started = False
while True:
    command = input("Enter Your Command > ").lower()
    if command == "start":
        if not started:
            print("Car started..")
            started = True
        else:
            print("Car has already started")
    elif command == "stop":
        if started:
            print("Car stopped..")
            started = False
        else:
            print("Car has already stopped")
    elif command == "help":
        print("""
start --> to start the car
stop --> stop the car
quit --> quit the game
help --> seek help on how to play
        """)
    elif command == "quit":
        break
    else:
        print("I didn't understand.")


exercise = "Prafull's Yoga Program"
print('We are adding you to ' + exercise + ". It's absolutely FREE!")
print(f'thank you for choosing {exercise}')