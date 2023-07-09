def welcome(age, height):
    if age >= 18 and height >= 170:
        print("Welcome.")
    elif age < 18:
        print("Sorry, you must be at least 18 years old to enter.")
    else:
        print("Sorry, you must be at least 170 cm tall to enter.")

user_age = int(input("Enter your age: "))
user_height = int(input("Enter your height in cm: "))

welcome(user_age, user_height)