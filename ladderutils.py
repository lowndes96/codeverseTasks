#question - would you like 'type' to refer to the type of animal or the datatype? I have left this as datatype. 
# class NoAnimal:
#     def __init__(self):
#         self.eyes = 0
#         self.hands = 0
#         self.legs = 0

#     def __str__(self):
#         return "None"
    
#     def fly(self):
#         return False

class Monkey:
    def __init__(self):
        self.eyes = 2
        self.hands = 2
        self.legs = 2

    def __str__(self):
        return "Monkey <eyes: 2, legs: 2, hands: 2>" # matched to format from example, if more classes, would use an f string for ease 
    
    def fly(self):
        return False

class Squirrel:
    def __init__(self):
        self.eyes = 2
        self.legs = 4

    def __str__(self):
        return "Squirrel <eyes: 2, legs: 4>"
    def fly(self):
        return False

class Pigeon:
    def __init__(self):
        self.eyes = 2
        self.wings = 2
        self.legs = 2
        self.can_fly = True

    def __str__(self):
        return "Pigeon <fly: True, eyes: 2, legs: 2, wings: 2>"
    
    def fly(self):
        return True

class Eagle:
    def __init__(self):
        self.eyes = 2
        self.wings = 2
        self.legs = 2
        self.can_fly = True

    def __str__(self):
        return "Eagle <fly: True, eyes: 2, legs: 2, wings: 2>"
    
    def fly(self):
        return True

class Ladder:
    def __init__(self):
        self.animals = {
            3: Monkey(),
            5: Squirrel(),
            8: Pigeon(),
            15: Eagle(),
            17: Monkey(),
        } # chose to use a dictionary, but presume there are many possible ways to do this 

    def animal_at_rung(self, rung):
        animal = self.animals.get(rung, None) #if there is no animal on the rung NoAnimal() is called 
        return animal

    def get_animals_count(self):
        return len(self.animals)
    
    def hop(self, rung): 
        if (self.animal_at_rung(rung) == None):
            return 'No animal there' #edge case not covered by example, but have covered here. 
        else: 
            if self.animals.get(rung +1) is None: 
                self.animals[rung + 1] = self.animal_at_rung(rung)
                self.animals.pop(rung)
            else: 
                return 'Not empty'
ladder = Ladder()

print(ladder.animal_at_rung(3)) # Monkey <eyes: 2, legs: 2, hands: 2>
print(ladder.animal_at_rung(5)) # Squirrel <eyes: 2, legs: 4>
print(ladder.animal_at_rung(8)) # Pigeon <fly: True, eyes: 2, legs: 2, wings: 2>
print(ladder.animal_at_rung(15)) # Eagle <fly: True, eyes: 2, legs: 2, wings: 2>
print(ladder.animal_at_rung(10)) # None
print(ladder.get_animals_count()) # 5
print(ladder.animal_at_rung(3) == ladder.animal_at_rung(17)) # False
print(type(ladder.animal_at_rung(3)) == type(ladder.animal_at_rung(17))) # True
print(ladder.animal_at_rung(8).fly()) # True
print(ladder.animal_at_rung(3).fly()) # False
print(ladder.hop(3)) # None
print(ladder.animal_at_rung(3)) # None
print(ladder.animal_at_rung(4)) # Monkey <eyes: 2, legs: 2, hands: 2>
print(ladder.hop(4)) # Not empty
print(ladder.animal_at_rung(4)) # Monkey <eyes: 2, legs: 2, hands: 2>

del ladder