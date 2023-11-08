class Monster:
    
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy
        
        # private attributes
        self._id = 5
    
    def attack(self, amount):
        pass
    
    def move(self, speed):
        pass
    
    def update_energy(self, amount):
        self.energy += amount
        
    
# monster = Monster()

# To find method and functions use the dir() function

class Shark(Monster):
    def __init__(self, speed, health, energy):
        super().__init__(health, energy)
        self.speed = speed
        
    def bite(self):
        pass
    
    def move(self):
        print(f'The speed of the shark is {self.speed}')
        
class Scorpion(Monster):
    def __init__(self, poison_damage, health, energy):
        super().__init__(health, energy)
        self.poison_damage = poison_damage
        
    def attack(self):
        print(f'The damage is {self.poison_damage}')
    
 
monster = Monster(20, 10)   

# hasattr and setattr
print(hasattr(monster, 'health'))
    
# setattr(object, 'attribute', value)
print(monster.__doc__)
help(monster)