class Forca():
    if __name__ == "__main__":
        vida: int = 5
        palavra: str = input("Digite uma palavra: ").lower()
        palavraEscondida = ["-" for _ in palavra]
        letraErr: list = []

        print(f"Essa é a palavra: {''.join(palavraEscondida)}")

        while(True):
            letra: chr = input("Digite uma letra: ").lower()

            if(palavra.count(letra) != 0):
                for i, c in enumerate(palavra):
                    if(letra == c):
                        palavraEscondida[i] = c
                print("".join(palavraEscondida))
                if(palavraEscondida.count("-") == 0):
                    print("\t*** Vc Ganhou ***")
                    break
            else:
                if(vida == 0):
                    print("\t*** Vc Perdeu ***")
                    break
                else:
                    letraErr.append(letra)
                    print(f"Errou, Não tem essa Letra\n\tLetra: {letra}\n\tVida: {vida}\n\tLetras Erradas: {letraErr}")
                    vida -= 1
                
