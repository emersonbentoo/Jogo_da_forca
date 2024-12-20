import random 
print("Ola vamos jogar o jogo da forca ?")
possibilidades = ['brasil', 'python','programação','logica','foco']
palavra = random.choice(possibilidades)
letra_usuario=[]
chances = 3
ganhou=False
while True:

    for letra in palavra:
        if letra in letra_usuario:
            print(letra, end=" ")
        
        else:
            print('_', end=" ")
    print(f" Voce tem {chances} chances")
    tentativa =input("Digite uma letra para adivinhar: ")
    letra_usuario.append(tentativa)
    

    if tentativa not in palavra:
        chances -=1

        
        if chances == 0:
            break
    ganhou= True
    for letra in palavra:
        if letra not in letra_usuario:
            ganhou=False
    if chances == 0 or ganhou:
        break
if ganhou:
    print(f"Voce ganhou, a palavra era {palavra}")
else:
    print(f"Voce perdeu a palavra era {palavra}")