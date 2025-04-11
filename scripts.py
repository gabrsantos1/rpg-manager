from class_mng import magicItem, charStats

class rpgManager:
    def __init__(self):
        self.player = []
        self.itens = []
        self.playerId = 1
        self.itemId = 1

    def checkPowerArmor(self, power, armor):
        return power + armor == 10 and power >= 0 and armor >= 0
    
    def checkClass(self, classType):
        return classType in ["Guerreiro", "Mago", "Arqueiro", "Ladino", "Bardo"]
    
    def checkItem(self, type, power, armor):
        if type not in ["Arma", "Armadura", "Amuleto"]:
            return False
        if power == 0 and armor == 0:
            return False
        if type == "Arma" and armor != 0:
            return False
        if type == "Armadura" and power != 0:
            return False
        if power > 10 or armor > 10 or power < 0 or armor < 0:
            return False
        return True
    
    def createPlayer(self, name, charName, classType, level, power, armor):
        if not self.checkClass(classType):
            return "Selecione uma classe válida."
        if not self.checkPowerArmor(power, armor):
            return "A soma de força e defesa DEVE ser 10."
        character = charStats(self.playerId, name, charName, classType, level, power, armor)
        self.player.append(character)
        self.playerId += 1
        return "Personagem cadastrado!"
    
    def createItem(self, name, type, power, armor):
        if not self.checkItem(type, power, armor):
            return "Item inválido."
        item = magicItem(self.itemId, name, type, power, armor)
        self.itens.append(item)
        self.itemId += 1
        return "Item cadastrado!"
    
    def showChar(self):
        return [str(p) for p in self.player]
    
    def searchChar(self, playerId):
        for p in self.player:
            if p.ownId == playerId:
                return str(p)
        return "Personagem n'ao encontrado."
    
    def attChar(self, playerId, newName):
        for p in self.player:
            if p.ownId == playerId:
                p.charName = newName
                return "Nome de aventureiro atualizado!"
        return "Personagem não encontrado!"
    
    def deleteChar(self, playerId):
        for p in self.player:
            if p.ownId == playerId:
                self.player.remove(p)
                return "Personagem removido!"
        return "Personagem não encontrado!"
    
    def listItens(self):
        return [str(i) for i in self.itens]

    def searchItem(self, itemId):
        for i in self.itens:
            if i.ownId == itemId:
                return str(i)
        return "Item não encontrado!"
    
    def addItemChar(self, playerId, itemId):
        character = None
        for p in self.player:
            if p.ownId == playerId:
                character = p
                break
        if not character:
            return "Personagem não encontrado!"

        item = None
        for i in self.itens:
            if i.ownId == itemId:
                item = i
                break
        if not item:
            return "Item não encontrado!"

        if item.type == "Amuleto":
            for i in character.itens:
                if i.type == "Amuleto":
                    return "Personagem já possui um amuleto!"

        character.itens.append(item)
        return "Item adicionado ao personagem!"
    
    def listItemChar(self, playerId):
        for p in self.player:
            if p.ownId == playerId:
                return [str(i) for i in p.itens]
        return "Personagem não encontrado!"

    def deleteItemChar(self, playerId, itemId):
        for p in self.player:
            if p.ownId == playerId:
                for i in p.itens:
                    if i.ownId == itemId:
                        p.itens.remove(i)
                        return "Item removido do personagem!"
                return "Item não encontrado no personagem!"
        return "Personagem não encontrado!"

    def searchAmuletChar(self, playerId):
        for p in self.player:
            if p.ownId == playerId:
                for i in p.itens:
                    if i.type == "Amuleto":
                        return str(i)
                return "Nenhum amuleto encontrado!"
        return "Personagem não encontrado!"
