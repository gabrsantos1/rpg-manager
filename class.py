class magicItem:
    def __init__(self, ownId, name, type, power, armor):
        self.ownId = ownId
        self.name = name
        self.type = type
        self.power = power
        self.armor = armor

    def __str__(self):
        return f"ID: {self.ownId}, Nome: {self.name}, Tipo: {self.type}, Força: {self.power}, Defesa: {self.armor}"

class charStats:
    def __init__(self, ownId, name, charName, classType, level, power, armor):
        self.ownId = ownId
        self.name = name
        self.charName = charName
        self.classType = classType
        self.level = level
        self.power = power
        self.armor = armor
        self.itens = []

    def maxPower(self):
        return self.power + sum(item.power for item in self.itens)
    
    def maxArmor(self):
        return self.armor + sum(item.amor for item in self.itens)
    
    def __str__(self):
        return (f"ID: {self.ownId}, Nome: {self.name}, Aventureiro: {self.charName}, "
                f"Classe: {self.classType}, Level: {self.level}, Força Total: {self.maxPower()}, "
                f"Defesa Total: {self.maxArmor()}")
