class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} издает звук.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print(f"{self.name} ({self.breed}) лает.")

animal = Animal("Животное")
animal.speak()  # Выводит "Животное издает звук."

dog = Dog("Бобик", "Дворняга")
dog.speak()  # Выводит "Бобик (Дворняга) лает."