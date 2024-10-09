from entity.pet import Pet

class FileReadingException(Exception):
    pass

def read_pets_from_file(file_path: str):
    try:
        with open(file_path, 'r') as file:
            pets = []
            for line in file:
                name, age, breed = line.strip().split(',')
                pets.append(Pet(name, int(age), breed))
            return pets
    except FileNotFoundError:
        print("Error: File not found.")
        raise FileReadingException("File not found.")
    except Exception as e:
        print(f"Error reading file: {e}")
        raise FileReadingException("Error reading file.")