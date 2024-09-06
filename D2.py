"2) Escreva um programa que verifique, em uma string, a existência da letra a, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre."
def contador_de_letra(texto):
    texto = texto.lower()
    contagem = texto.count('a')
    existe_a = contagem > 0

    return existe_a, contagem

entrada = input("Digite um texto: ")

existe_a, contagem = contador_de_letra(entrada)

if existe_a:
    print(f"A letra 'a' ou 'A' ocorre {contagem} vez(es) no texto.")
else:
    print("Não corresponde.")
