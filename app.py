from helpers.PopulaEnvironment import PopulaEnvironment
from algoritmo.AEstrela import AEstrela

def main():
    environment = PopulaEnvironment().make()
    search = AEstrela(environment)
    search.search('U', 'A')

main()