class Person:
    def __init__(self, name, age, weight, height):
        self.age = age
        self.weight = weight
        self.height = height
        self.name = name

    def hello(self):
        print(f"Hello {self.name.capitalize()}")

    def information(self):
        print(
            f"Hello {self.name}! Your Age is {self.age}, Your Weight is {self.weight}, your height is {self.height}"
        )


def user_input():
    user1_name = input("Name: ")
    while True:
        user1_age = input("Age: ")
        if user1_age.isdigit():
            age = int(user1_age)
            if age > 0 and age < 120:
                break
            else:
                print("Please input the correct age (min 1 years old)")
        else:
            print("Enter a number")
    while True:
        user1_weight = input("Weight: ")
        if user1_weight.isdigit():
            weight = int(user1_weight)
            if weight > 0:
                break
        else:
            print("Enter a number")
    while True:
        user1_height = input("Height: ")
        if user1_height.isdigit():
            height = int(user1_height)
            if height > 0:
                break
        else:
            print("Enter a number")
    kenneth = Person(user1_name.capitalize(), user1_age, user1_weight, user1_height)
    information = kenneth.information()

    return information


user_input()
