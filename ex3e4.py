
def substitui(frase, letra):
    aux = ""
    frase_aux = frase.lower()
    letra = letra.lower()

    i = 0
    while i < len(frase):
        if frase_aux[i] == letra:
            aux = aux + '*'
        else:
            aux= aux + frase[i]
        i = i + 1

    return aux

def troca(frase, letra):
    for c in letras:
        frase = substitui(frase, c)
    return frase

texto = '''
I can only show the door.
You're the one that has to walk through it.
'''
letras = 'aro'

print(letras)