from os import system

def PregntaRecistencia():
    print("""
               ¿R?
        ┌──────W─────┐      
        │            │
    12v─┴─           │
        ┬            │
        └────────────┘ I = 6
    
    """) 
    opcion = int(input("Cuanto Vale la Resistencia:")) 
    if opcion == 2:
        print("Correcto")
        OpcionList.append(1)
    else:
        print("Incorrecto")

def PregntaRecistencia():
    print("""
               R = 3
        ┌──────W─────┐      
        │            │
    12v─┴─           │
        ┬            │
        └────────────┘ I = ¿?
    
    """) 
    opcion = int(input("Cuanto Vale la Resistencia:")) 
    if opcion == 2:
        print("Correcto")
        OpcionList.append(1)
    else:
        print("Incorrecto")


def Room():
    Room = """
    ########=#######
    #       4-door #
   #3-R        1-I#
    #    2-v       #
    ################
    10 - Exit
    """
    print(Room) 
    opcion = int(input("Slect the tematic of question:"))
    return opcion

def menu():
    menu = """
    /
    /  1 - Start
    /  2 - help
    /  2 - Exit
    /
    """
    print(menu)
    opcion = int(input("Option:"))
    if opcion <= 1:
        return True 
    elif opcion == 2:
        print("""
        # = Wall
        + = Door
        R = Recitance
        v = Volt
        I = Intensity      
        
        """)
    elif opcion == 3:
        return False
main = menu()
system("cls")

OpcionList = []

while main:
    try:
        system("cls")
        opcion = Room()
        if opcion == OpcionList:
           print("Ya as echo esta respuesta")
        else:
            if opcion == 1:
                exit()
            elif opcion == 2:
                exit()
            elif opcion == 3:
                PregntaRecistencia()
    except ValueError:
        print("ERROR")
        exit()