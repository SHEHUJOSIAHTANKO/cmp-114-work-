def welcome_person(age, height):
    if age >= 18 and height >= 160:
        print("Welcome.")
    else:
        print("Sorry, you do not meet the necessary age/height requirements.")

person_age = int(input("Enter your age: "))
person_height = int(input("Enter your height in centimeters: "))

welcome_person(person_age, person_height)
