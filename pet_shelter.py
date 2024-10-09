from entity.pet import Pet
from entity.dog import Dog
from entity.cat import Cat
from util.db_conn_util import connect_db
from exception.adoption_exception import AdoptionException
import pyodbc

class PetShelter:
    def __init__(self):
        self.available_pets = self.fetch_pets_from_db()

    def fetch_pets_from_db(self):
        connection = connect_db()
        pets = []
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT name, age, breed FROM pets")
                rows = cursor.fetchall()
                for row in rows:
                    pets.append(Pet(row[0], row[1], row[2]))
            except pyodbc.Error as e:
                print(f"Error retrieving pets: {e}")
            finally:
                connection.close()
        return pets

    def add_pet(self, pet: Pet):
        self.available_pets.append(pet)

    def remove_pet(self, pet: Pet):
        self.available_pets.remove(pet)

    def list_available_pets(self):
        return [pet for pet in self.available_pets]
    
def record_pet(name: str, age: int, breed: str):
    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO pets (name, age, breed) VALUES (?, ?, ?)", (name, age, breed))
            connection.commit()
            print("Pet recorded successfully.")
        except pyodbc.Error as e:
            print(f"Error recording pet: {e}")
        finally:
            connection.close()

def add_pet_to_shelter(shelter: PetShelter):
    try:
        name = input("Enter the pet's name: ")
        age = int(input("Enter the pet's age: "))
        if age < 0:
            raise ValueError("Age must be a positive integer.")
        breed = input("Enter the pet's breed: ")

        pet_type = input("Is it a Dog or Cat? (D/C): ").strip().upper()
        if pet_type == 'D':
            dog_breed = input("Enter the dog's breed: ")
            pet = Dog(name, age, breed, dog_breed)
        elif pet_type == 'C':
            cat_color = input("Enter the cat's color: ")
            pet = Cat(name, age, breed, cat_color)
        else:
            print("Invalid pet type selected. Please choose 'D' for Dog or 'C' for Cat.")
            return

        shelter.add_pet(pet)
        print(f"Added pet: {pet}")

        # Record the pet in the database
        record_pet(name, age, breed)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def remove_pet_from_shelter(shelter: PetShelter):
    try:
        name = input("Enter the name of the pet to remove: ")
        pet_to_remove = next((pet for pet in shelter.available_pets if pet.get_name() == name), None)
        if pet_to_remove:
            shelter.remove_pet(pet_to_remove)
            print(f"Removed pet: {pet_to_remove}")
        else:
            print("Pet not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def adopt_pet(shelter: PetShelter):
    try:
        name = input("Enter the name of the pet to adopt: ")
        pet_to_adopt = next((pet for pet in shelter.available_pets if pet.get_name() == name), None)
        if not pet_to_adopt:
            raise AdoptionException(f"No available pet found with the name '{name}'.")

        shelter.remove_pet(pet_to_adopt)
        print(f"Adopted pet: {pet_to_adopt}")
        delete_pet_from_db(name)
    except AdoptionException as e:
        print(f"Adoption error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def delete_pet_from_db(name: str):
    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM pets WHERE name = ?", (name,))
            connection.commit()
            print(f"Pet '{name}' is successfully adopted.")
        except pyodbc.Error as e:
            print(f"Error deleting pet from database: {e}")
        finally:
            connection.close()

def display_pet_listings():
    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM pets")
            pets = cursor.fetchall()
            for pet in pets:
                print(pet)
        except pyodbc.Error as e:
            print(f"Error retrieving pets: {e}")
        finally:
            connection.close()

def list_available_pets(shelter: PetShelter):
    try:
        available_pets = shelter.list_available_pets()
        if not available_pets:
            print("No pets available for adoption.")
        else:
            print("Available Pets:")
            for pet in available_pets:
                print(pet)
    except Exception as e:
        print(f"An error occurred while listing pets: {e}")