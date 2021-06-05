# Example for multilevel inheritance

# Base class
class Animals:
    def __init__(self) -> None:
        pass

    def showDetails(self):
        print("The animals you have are:")

# Derived class
class Pet(Animals):
    def __init__(self) -> None:
        pass

    def showDetails(self):
        super().showDetails()
        print("\tThe details of your pets are:")

# Sub derived class
class Dog(Pet):
    name = "Chinna"
    action = "Bow Bow!"

    def __init__(self, name):
        self.name = name

    def bark(self):
        super().showDetails()
        print(
            f"\t\tYou have a dog and his name is {self.name} and the action is {self.action}")


animal1 = Dog("Moti")
animal1.bark()
