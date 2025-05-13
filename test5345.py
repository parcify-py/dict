films = {"Matrix":2004,"Drive":2010,"Last of Us":2017,"Jumanji":2022}

player = {'name':'Adolf','level':'6','inventory':['water','gun','book']}

player['inventory'].append('key')

def atack(player1=str,player2=str):
    global characters
    characters[player1]['hp'] -= characters[player2]['damage']
    print(f"{player2.capitalize()} atack {player1}\n ")

def print_hp():
    print(f"Player one hp: {characters['player1']['hp']} Player two hp: {characters['player2']['hp']} \n")

    

characters = {'player1':{'hp':100,'damage':20,'superpower':['magick','fly','teleport']},'player2':{'hp':120,'damage':15,'superpower':['magick','fly','teleport']}}


print_hp()
atack('player1','player2')
print_hp()



