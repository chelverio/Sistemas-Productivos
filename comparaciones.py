def comparar(a, b):
    if a > b:
        return 'mayor'
    elif a < b:
        return 'menor'
    else:
        return 'igual'

def pedir_mano():
    a = input('¿Quieres casarte? ')
    if a.lower() == 'si':
        return 'Me dijo que sí'
    else:
        return 'Ni de pedo'
