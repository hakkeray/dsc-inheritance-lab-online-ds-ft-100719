class Animal(object):
    def __init__(self, name, weight):
        self.name = name
        self.size = None
        self.weight = weight
        self.species = None
        self.food_type = None
        self.nocturnal = False

    def sleep(self):
        if self.nocturnal:
            print("{} sleeps during the day.".format(self.name))
        else:
            print("{} sleeps at night.".format(self.name))

    def eat(self, food):
        if self.food_type == 'omnivore':
            print("{} the {} thinks {} is yummy!".format(self.name, self.species, food))
        elif (food == 'meat' and self.food_type == 'carnivore'):
            print("{} the {} thinks {} is yummy!".format(self.name, self.species, food))
        elif (food == 'plants' and self.food_type == 'herbivore'):
            print("{} the {} thinks {} is yummy!".format(self.name, self.species, food))
        else:
            print("I don't eat this!")


class Elephant(Animal):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.species = 'elephant'
        self.size = 'enormous'
        self.food_type = 'herbivore'
        self.nocturnal = False

class Tiger(Animal):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.species = 'tiger'
        self.size = 'large'
        self.food_type = 'carnivore'
        self.nocturnal = True

class Raccoon(Animal):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.species = 'raccoon'
        self.size = 'small'
        self.food_type = 'omnivore'
        self.nocturnal = True

class Gorilla(Animal):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.species = 'gorilla'
        self.size = 'large'
        self.food_type = 'herbivore'
        self.nocturnal = False


def add_animal_to_zoo(zoo, animal_type, name, weight):
    animal = None

    if animal_type == 'tiger':
        animal = Tiger(name, weight)
    elif animal_type == 'elephant':
        animal = Elephant(name, weight)
    elif animal_type == 'gorilla':
        animal = Gorilla(name, weight)
    elif animal_type == 'raccoon':
        animal = Raccoon(name, weight)
    else:
        print("The zoo doesn't recognize that type of animal.")

    zoo.append(animal)

    return zoo


def feed_animals(zoo, time='day'):
    for animal in zoo:
        if time == 'day':
            if animal.nocturnal == False:
                if animal.food_type == 'carnivore':
                    animal.eat('meat')
                else:
                    animal.eat('plants')
        else:
            if animal.nocturnal == True:
                if animal.food_type == 'carnivore':
                    animal.eat('meat')
                else:
                    animal.eat('plants')


# Create your animals and add them to the 'zoo' in this cell!
#new_animals = ['elephant', 'elephant', 'raccoon', 'raccoon', 'gorilla', 'tiger', 'tiger', 'tiger']

#zoo = []

#for i in new_animals:
#    zoo = add_animal_to_zoo(zoo, i, "name", 100)

#zoo


#feed_animals(zoo)

# feed_animals(zoo, time='night')
