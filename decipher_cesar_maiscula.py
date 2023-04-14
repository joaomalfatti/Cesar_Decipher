def decifrar_criptografia_cesar(texto_cifrado, chave):
    alfabeto_maiusculo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alfabeto_minusculo = "abcdefghijklmnopqrstuvwxys"
    texto_decifrado = ""
    for letra in texto_cifrado:

        if letra in alfabeto_maiusculo:
            indice = alfabeto_maiusculo.index(letra)
            nova_letra = alfabeto_maiusculo[(indice - chave) % 26]
            texto_decifrado += nova_letra

        elif letra in alfabeto_minusculo:
            indice = alfabeto_minusculo.index(letra)
            nova_letra = alfabeto_minusculo[(indice - chave) % 26]
            texto_decifrado += nova_letra
        else:
            texto_decifrado += letra
    return texto_decifrado

texto_cifrado = "T BFTGXGVBT WH LXK "
#texto_cifrado = "t bftgxgvbt wh lxk"
chave = 19  # Chave de deslocamento utilizada na criptografia
texto_decifrado = decifrar_criptografia_cesar(texto_cifrado, chave)
print(texto_decifrado)
