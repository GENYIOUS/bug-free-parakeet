#get's person's year of birth
#subtract's person's year from current year to get age

print("This is the Age Calculator!")
print(" ")
person_name = input('Type in the name of the person: ')
print("Okay, then lets find", person_name, 'age!!')


def calculate_age(age):
    year = int(input('Type in the year: '))
    print(' ')
    curr_year = int(input('Type in the current year your in: '))

    if (year > curr_year):
        print('Not Valid year')
        print('Please try again.')
        quit()

    else:
        age = int(curr_year - year)
        print(person_name, ' age is :', age, 'years old.')

calculate_age('age')        