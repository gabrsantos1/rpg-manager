from scripts import rpgManager

def menu():
    manager = rpgManager()
    while True:
        print("\n-- Criador de Personagens --")
        print("1. Cadastrar Personagem                 |")
        print("2. Cadastrar Item Mágico                |")
        print("3. Listar Personagens                   |")
        print("4. Buscar Personagem por ID             |")
        print("5. Atualizar Nome de Aventureiro        |")
        print("6. Remover Personagem                   |")
        print("7. Listar Itens Mágicos                 |")
        print("8. Buscar Item por ID                   |")
        print("9. Adicionar Item ao Personagem         |")
        print("10. Listar Itens do Personagem          |")
        print("11. Remover Item do Personagem          |")
        print("12. Buscar Amuleto do Personagem        |")
        print("0. Sair                                 |")
        option = input("Escolha uma opção: ")

        if option == "1":
            name = input("Nome: ")
            charName = input("Nome Aventureiro: ")
            classType = input("Classe (Guerreiro, Mago, Arqueiro, Ladino, Bardo): ")
            level = int(input("Level: "))
            power = int(input("Força (soma com defesa deve ser 10): "))
            armor = int(input("Defesa (soma com força deve ser 10): "))
            print(manager.createPlayer(name, charName, classType, level, power, armor))

        elif option == "2":
            name = input("Nome do Item: ")
            type = input("Tipo (Arma, Armadura, Amuleto): ")
            power = int(input("Força: "))
            armor = int(input("Defesa: "))
            print(manager.createItem(name, type, power, armor))

        elif option == "3":
            for p in manager.showChar():
                print(p)

        elif option == "4":
            playerId = int(input("ID do Personagem: "))
            print(manager.searchChar(playerId))

        elif option == "5":
            playerId = int(input("ID do Personagem: "))
            newName = input("Novo Nome Aventureiro: ")
            print(manager.attChar(playerId, newName))

        elif option == "6":
            playerId = int(input("ID do Personagem: "))
            print(manager.deleteChar(playerId))

        elif option == "7":
            for i in manager.listItens():
                print(i)

        elif option == "8":
            itemId = int(input("ID do Item: "))
            print(manager.searchItem(itemId))

        elif option == "9":
            playerId = int(input("ID do Personagem: "))
            itemId = int(input("ID do Item: "))
            print(manager.addItemChar(playerId, itemId))

        elif option == "10":
            playerId = int(input("ID do Personagem: "))
            itens = manager.listItemChar(playerId)
            if isinstance(itens, list):
                for i in itens:
                    print(i)
            else:
                print(itens)

        elif option == "11":
            playerId = int(input("ID do Personagem: "))
            itemId = int(input("ID do Item: "))
            print(manager.deleteItemChar(playerId, itemId))

        elif option == "12":
            playerId = int(input("ID do Personagem: "))
            print(manager.searchAmuletChar(playerId))

        elif option == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()