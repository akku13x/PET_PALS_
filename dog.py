from entity.pet import Pet

class Dog(Pet):
    def __init__(self, name: str, age: int, breed: str, dog_breed: str):
        super().__init__(name, age, breed)
        self.dog_breed = dog_breed

    def get_dog_breed(self):
        return self.dog_breed

    def set_dog_breed(self, dog_breed: str):
        self.dog_breed = dog_breed

    def __str__(self):
        return super().__str__() + f", DogBreed: {self.dog_breed}"