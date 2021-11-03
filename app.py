from helpers.PopulaEnvironment import PopulaEnvironment
from algoritmo.AEstrela import AEstrela
from algoritmo.AlgoritmoGuloso import AGuloso

def main():
    choice = 1
    while choice != 0:
        print("Escolha:")
        print("1 - para busca em Profundidade")
        print("2 - para busca em Largura")
        print("3 - para busca Gulosa")
        print("4 - para busca A*")
        print("0 - para sair")

        choice = int(input())

        if(0 == choice):
            continue

        print("Digite a sala de origem:")
        root = input()
        print("Digite a sala de destino")
        destiny = input()

        if(1 == choice):#profundidade
            continue
        if(2 == choice):#largura
            continue
        if(3 == choice):#gulosa
            environment = PopulaEnvironment().make()
            search = AGuloso(environment)
            search.search(root, destiny)
            continue
        if(4 == choice):#A*
            environment = PopulaEnvironment().make()
            search = AEstrela(environment)
            search.search(root, destiny)
            continue
        else:
            continue


main()