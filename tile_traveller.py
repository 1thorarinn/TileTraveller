# Forrit sem er leikur

# Leikmaður byrjar á 1.1 reitnum og þarf að komast á 3.1
# Leikmaður hefur um að velja norður, suður, austur og vestur.
# Valmöguleikarnir eru takmarkaðir eftir því á hvaða svæði hann er
# Til að mynda á 1.1 getur hann bara farið norður


def available_directions(current_tile:str) -> str:
     return {
        '1,1': 'n',
        '1,2': 'nes',
        '1,3': 'nes',
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
        }[chr]
    print("You can travel: {}".format(available_directions))
run = True
current_tile = "1,1"
while run:
    print(print_available_directions(available_directions(current_tile)))
    direction = input("Direction: ")
    
    