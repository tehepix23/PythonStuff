class Fighter:
    def __init__(self, name, attack, defense, speed):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.speed = speed
        
    def getName(self) -> str:
        return self.name
    
    def getAttack(self) -> int:
        return self.attack
    
    def getDefense(self) -> int:
        return self.defense
    
    def getSpeed(self) -> int:
        return self.speed