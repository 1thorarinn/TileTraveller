# Forrit sem er leikur

# Leikmaður byrjar á 1.1 reitnum og þarf að komast á 3.1
# Leikmaður hefur um að velja norður, suður, austur og vestur.
# Valmöguleikarnir eru takmarkaðir eftir því á hvaða svæði hann er
# Til að 
# mynda á 1.1 getur hann bara farið norður


def available_directions(current_tile:str) -> str:
    return {
        '1,1': 'n',
        '1,2': 'nes',
        '1,3': 'se',
        '1,4': 'nes',
        '1,5': 'nes',
        '1,6': 'nes',
    }[current_tile]
    

def print_available_directions(directions:str) -> str:
    available_directions = ''
    for chr in directions:
        available_directions += {
            'n': '(N)orth',
            's': '(S)outh',
            'e': '(E)ast',
            'w': '(W)est',
        }[chr.lower()]
    print("You can travel: {}".format(available_directions))

def traverse(current_tile:str, direction:str) -> str:
        # splitta
        tpart = current_tile.split(',')
        if direction.lower() == 'n':
            tpart[1] = str(int(tpart[1]) + 1)
        if direction.lower() == 'e':
            tpart[0] = str(int(tpart[0]) + 1)
        if direction.lower() == 's':
            tpart[1] = str(int(tpart[1]) - 1)
        if direction.lower() == 'w':
            tpart[0] = str(int(tpart[0]) - 1)
        return tpart[0] + ',' + tpart[1]
   

run = True
current_tile = "1,1"
while run:
    print( print_available_directions( available_directions(current_tile) ) )
    direction = input("Direction: ")
    if direction in available_directions(current_tile):
        current_tile = traverse(current_tile, direction)
    else: 
        print("nope")
        return current_tile
    print(current_tile)
    
    