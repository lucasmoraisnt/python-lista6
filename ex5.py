def ocorrencia(frase, palavra):
    contador = 0
    pos = frase.find(palavra, 0)
    while pos != -1:
        contador = contador + 1
        pos = frase.find(palavra, pos + 1)

    return contador

texto = "ANA E MARIANA GOSTAM DE BANANA"
word = "ANA"
resp = ocorrencia(texto, word)
print(resp)