class AulaExerciciosPython:
    @staticmethod
    def ex1() -> None:
        num: float = float(input("Digite um Número: "))
        if(num == 0):
            print("O Número é zero")
        elif(num > 0):
            print("O Número é positivo")
        else:
            print("O Número é Negativo")
    
    @staticmethod
    def ex2():
        lista: list = [float(input("Digite um Número: ")),float(input("Digite um Número: "))]
        print(max(lista))

    @staticmethod
    def ex3():
        print("Par") if(int(input("Digite um Número: ")) % 2 == 0) else print("Impar")

    @staticmethod
    def ex4():
        print("é bissexto") if(int(input("Digite o Ano: ")) % 4 == 0) else print("não é bissexto")
    
    @staticmethod
    def ex5():
        lista: list = [
            float(input("Digite um Número: ")),
            float(input("Digite um Número: ")),
            float(input("Digite um Número: "))
        ]

        print(max(lista))
    
    @staticmethod
    def ex6():
        print("pode votar") if(float(input("Digite uma Idade: ")) >= 18) else print("não pode votar")

    @staticmethod
    def ex7():
        print("Pode sair") if(bool(input("Digite 'True' ou 'False': "))) else print("Não pode Sair")

    @staticmethod
    def ex8():
        print("Senha Certa") if(input("Digite a Senha: ") == "1234") else print("Senha Errada")

    @staticmethod
    def ex9():
        num: float = float(input("Digite um Número: "))
        print("o número está entre 10 e 50") if(num >= 10 and num <= 50) else print("o número não está entre 10 e 50")

    @staticmethod
    def ex10():
        print("Alto") if(float(input("Digite um Número: ")) >= 100) else print("Baixo")

    @staticmethod
    def ex11():
        num1: float = float(input("Digite um Número: "))
        num2: float = float(input("Digite um Número: "))

        match int(input("1 - Soma\n2 - subtração\n3 - multiplicação\n4 - divisão\n")):
            case 1:
                print(num1 + num2)
            case 2:
                print(num1 - num2)
            case 3:
                print(num1 * num2)
            case 4:
                print(num1 / num2)

    @staticmethod
    def ex12():
        pass
    @staticmethod
    def ex1():
        pass
    @staticmethod
    def ex1():
        pass
    @staticmethod
    def ex1():
        pass
    @staticmethod
    def ex1():
        pass
    @staticmethod
    def ex1():
        pass
    @staticmethod
    def ex1():
        pass
    @staticmethod
    def ex1():
        pass
    @staticmethod
    def ex1():
        pass
    @staticmethod
    def ex1():
        pass
    @staticmethod
    def ex1():
        pass
    @staticmethod
    def ex1():
        pass
    @staticmethod
    def ex1():
        pass
    @staticmethod
    def ex1():
        pass
    @staticmethod
    def ex1():
        pass
    @staticmethod
    def ex1():
        pass
    @staticmethod
    def ex1():
        pass
    @staticmethod
    def ex1():
        pass
    @staticmethod
    def ex1():
        pass
    @staticmethod
    def ex1():
        pass
    @staticmethod
    def ex1():
        pass
    @staticmethod
    def ex1():
        pass
    @staticmethod
    def ex1():
        pass
    @staticmethod
    def ex1():
        pass
    @staticmethod
    def ex1():
        pass
    @staticmethod
    def ex1():
        pass
    @staticmethod
    def ex1():
        pass
    @staticmethod
    def ex1():
        pass
    @staticmethod
    def ex1():
        pass
    @staticmethod
    def ex1():
        pass
    @staticmethod
    def ex1():
        pass
    @staticmethod
    def ex1():
        pass
    @staticmethod
    def ex1():
        pass
    @staticmethod
    def ex1():
        pass
    @staticmethod
    def ex1():
        pass
    @staticmethod
    def ex1():
        pass
    @staticmethod
    def ex1():
        pass
    @staticmethod
    def ex1():
        pass
    @staticmethod
    def ex1():
        pass

    if __name__ == "__main__":
        ex11()