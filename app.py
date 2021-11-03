from helpers.PopulaEnvironment import PopulaEnvironment
from algoritmo.AEstrela import AEstrela

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

        if(1 == choice):
            continue#profundidade
        if(2 == choice):
            continue#largura
        if(3 == choice):
            continue#gulosa
        if(4 == choice):
            environment = PopulaEnvironment().make()
            search = AEstrela(environment)
            search.search(root, destiny)
            continue
        else:
            continue


main()