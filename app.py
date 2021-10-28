from helpers.PopulaEnvironment import PopulaEnvironment

def main():
    environment = PopulaEnvironment().make()
    environment.visit()

main()