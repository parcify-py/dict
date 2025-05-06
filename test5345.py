def create_shelter(first_animal_name,first_animal_age, first_animal_type):
    return {first_animal_name:{'type':first_animal_type,'age':first_animal_age}}

def add_animal(shelter: dict, name: str, type: str, age: int):
    shelter[name] = {'age': age, 'type': type}

def print_animals(shelter: dict):
    for name, info in shelter.items():
        print(f"{name} is a {info['type']}, and it is {info['age']} years old")

def print_animals_by_type(shelter: dict, type):
    for name, info in shelter.items():
        if info['type'] == type:
            print(name)


first_animal_name = input("Enter the first animal name: ")
first_animal_type = input("Enter the animal type: ")
first_animal_age = int(input("Enter the animal's age: "))

shelter = create_shelter(first_animal_name,first_animal_age, first_animal_type)


add_animal(shelter, 'Mdk', 'dog', 8)

print_animals(shelter)

print_animals_by_type(shelter, 'cat')


