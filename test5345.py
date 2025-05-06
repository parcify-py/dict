
def create_shelter(name,dict):
    shelter = {name:dict}
    return shelter 

def add_animal(shelter: dict, name: str,type: str,old: int):
    global shelter
    shelter[name] = {'old':old,'type':type}
    
def print_animals():
    global shelter
    key = shelter.keys()
    for i in range(len(shelter)):
        print(f"{list(key)[i]} is a {shelter[list(key)[i]]['type']}, and it is {shelter[list(key)[i]]['old']} years old")
        
def print_animalstype(type):
    global shelter
    key = shelter.keys()
    for i in range(len(shelter)):
        if shelter[list(key)[i]]['type'] == type:
            print(list(key)[i])

name = 'Lala'
lala = {'old':5,'type':'cat'} 

shelter = create_shelter(name,lala)

add_animal('Mdk','dog',8)
print_animals()
print_animalstype('cat')









