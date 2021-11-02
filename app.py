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
        choice = int(input())
        # print("Digite a sala de origim:")
        # root = input()
        # print("Digite a sala de destino")
        # destiny = input()
        if(1 == choice):
            pass#profundidade
        if(2 == choice):
            pass#largura
        if(3 == choice):
            pass#gulosa
        if(4 == choice):
            environment = PopulaEnvironment().make()
            search = AEstrela(environment)
            search.search('A', 'U')
            pass
        if(0 == choice):
            pass
        else:
            pass


main()