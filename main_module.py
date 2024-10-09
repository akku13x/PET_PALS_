# from entity.pet import Pet
# from entity.dog import Dog
# from entity.cat import Cat
# from entity.cash_donation import *
# from entity.donation import *
# from entity.item_donation import *
# from entity.pet_shelter import *
from util.db_conn_util import *
# from exception.adoption_exception import *
from exception.file_handling_exception import *
from entity.pet_shelter import PetShelter
from entity.pet_shelter import *
from entity.donation import *

def display_menu():
    print("\nPet Adoption System")
    print("1. Add Pet")
    print("2. Remove Pet")
    print("3. View Available Pets")
    print("4. Make Donation")
    print("5. View Donations")
    print("6. Adopt Pet")
    print("7. Read Pets from File")
    print("8. Exit")


# Main program loop
def main():
    shelter = PetShelter()  # Fetch pets from DB on initialization
    setup_database()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_pet_to_shelter(shelter)
        elif choice == '2':
            remove_pet_from_shelter(shelter)
        elif choice == '3':
            list_available_pets(shelter)
        elif choice == '4':
            make_donation()
        elif choice == '5':
            display_donations()
        elif choice == '6':
            adopt_pet(shelter)
        elif choice == '7':
            file_path = input("Enter the file path: ")
            try:
                pets_from_file = read_pets_from_file(file_path)
                for pet in pets_from_file:
                    shelter.add_pet(pet)
                print("Pets added from file.")
            except FileReadingException as e:
                print(f"Error: {e}")
        elif choice == '8':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()