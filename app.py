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
        checker1: 1
    else:
        print('Enter either K or L for Kg and lbs respectively')



exercise = "Prafull's Yoga Program"
print('We are adding you to ' + exercise + ". It's absolutely FREE!")
print(f'thank you for choosing {exercise}')