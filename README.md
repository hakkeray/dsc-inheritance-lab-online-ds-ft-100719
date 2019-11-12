
# Inheritance - Lab

## Introduction

In this lab, you'll use what you've learned about inheritance to model a zoo using superclasses, subclasses, and maybe even an abstract superclass!

## Objectives

You will be able to:

* Use inheritance to write nonredundant code
* Describe the relationship between subclasses and superclasses
* Create a domain model using OOP

## Modeling a Zoo

Consider the following scenario:  You've been hired by a zookeeper to build a program that keeps track of all the animals in the zoo.  This is a great opportunity to make use of Inheritance and Object-Oriented Programming!

## Creating an Abstract Superclass

Start by creating an abstract superclass, `Animal`.  When our program is complete, all subclasses of `Animal` will have the following attributes:

* `name`, which is a string set at instantation time
* `size`, which can be `'small'`, `'medium'`, `'large'`, or `'enormous'`.
* `weight`, which is an integer set at instantiation time.
* `species`, a string that tells us the species of the animal
* `food_type`, which can be `'herbivore'`, `'carnivore'`, or `'omnivore'`
* `nocturnal`, a boolean value that is `True` if the animal sleeps during the day, otherwise `False`

They'll also have the following behaviors:

* `sleep`, which prints a string saying if the animal sleeps during day or night
* `eat`, which takes in the string `plants` or `meat`, and returns `'{animal name} the {animal species} thinks {food} is yummy!'` or `'I don't eat this!'` based on the animal's `food_type` attribute. 

In the cell below, create an abstract superclass that meets these specifications.

**_NOTE:_** For some attributes in an abstract superclass such as `size`, the initial value doesn't matter--just make sure that you remember to override it in each of the subclasses!


```python
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
                
```

Great! Now that you have our Abstract Superclass, you can begin building out the specific animal classes.

In the cell below, complete the `Elephant` class.  This class should:

* Subclass `Animal`
* Have a species of `'elephant'`
* Have a size of `'enormous'`
* Have a food type of `'herbivore'`
* Set nocturnal to `False`

**_Hint:_** Remember to make use of the `super()` object during initialization, and be sure to pass in the values it expects at instantiation time!


```python
class Elephant(Animal):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.species = 'elephant'
        self.size = 'enormous'
        self.food_type = 'herbivore'
        self.nocturnal = False
```

Great! Now, in the cell below, create a `Tiger` class.  This class should:

* Subclass `Animal`
* Have a species of `'tiger'`
* Have a size of `'large'`
* Have a food type of `'carnivore'`
* Set nocturnal to `True`


```python
class Tiger(Animal):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.species = 'tiger'
        self.size = 'large'
        self.food_type = 'carnivore'
        self.nocturnal = True
```

Great! 2 More classes to go. In the cell below, create a `Raccoon` class.  This class should:

* Subclass `Animal`
* Have a species of `raccoon`
* Have a size of `'small'`
* Have a food type of `'omnivore'`
* Set nocturnal to `True`


```python
class Raccoon(Animal):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.species = 'raccoon'
        self.size = 'small'
        self.food_type = 'omnivore'
        self.nocturnal = True
```

Finally, create a `Gorilla` class.  This class should:

* Subclass `Animal`
* Have a species of `gorilla`
* Have a size of `'Large'`
* Have a food type of `'herbivore'`
* Set nocturnal to `False`


```python
class Gorilla(Animal):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.species = 'gorilla'
        self.size = 'large'
        self.food_type = 'herbivore'
        self.nocturnal = False
```

## Using Our Objects

Now it's time to populate the zoo! To ease the creation of animal instances, create a function `add_animal_to_zoo`.

This function should take in the following parameters:

* `zoo`, an array representing the current state of the zoo
* `animal_type`, a string.  Can be `'Gorilla'`, `'Raccoon'`, `'Tiger'`, or `'Elephant'`.
* `name`, the name of the animal being created
* `weight`, the weight of the animal being created

The function should then:

* use `animal_type` to determine which object to create
* Create an instance of that animal, passing in the `name` and `weight`
* Append the newly created animal to `zoo`
* Return `zoo`


```python
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
```

Great! Now, add some animals to your zoo. 

Create the following animals and add them to your zoo.  The names and weights are up to you.

* 2 Elephants
* 2 Raccons
* 1 Gorilla
* 3 Tigers


```python
# Create your animals and add them to the 'zoo' in this cell!
new_animals = ['elephant', 'elephant', 'raccoon', 'raccoon', 'gorilla', 'tiger', 'tiger', 'tiger']

zoo = []

for i in new_animals:
    zoo = add_animal_to_zoo(zoo, i, "name", 100)
    
zoo
```




    [<__main__.Elephant at 0x11ff42550>,
     <__main__.Elephant at 0x11ff425f8>,
     <__main__.Raccoon at 0x11ff424e0>,
     <__main__.Raccoon at 0x11ff42a90>,
     <__main__.Gorilla at 0x11ff420b8>,
     <__main__.Tiger at 0x11ff426d8>,
     <__main__.Tiger at 0x11ff42fd0>,
     <__main__.Tiger at 0x11ff426a0>]



Great! Now that you have a populated zoo, you can do what the zookeeper hired you to do--write a program that feeds the correct animals the right food at the right times!

To do this, write a function called `feed_animals`.  This function should take in two arguments:

* `zoo`, the zoo array containing all the animals
* `time`, which can be `'Day'` or `'Night'`.  This should default to day if nothing is entered for `time`.

This function should:

* Feed only the non-nocturnal animals if `time='Day'`, or only the nocturnal animals if `time='Night'`
* Check the food type of each animal before feeding.  If the animal is a carnivore, feed it `meat`; otherwise, feed it `plants`. Feed the animals by using their `.eat()` method.


```python
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
        
```

Now, test out your program.  Call the function for a daytime feeding below.


```python
feed_animals(zoo)
```

    name the elephant thinks plants is yummy!
    name the elephant thinks plants is yummy!
    name the gorilla thinks plants is yummy!


If the elephants and gorrillas were fed then things should be good!

In the cell below, call `feed_animals` again, but this time set `time='Night'`


```python
feed_animals(zoo, time='night')
```

    name the raccoon thinks plants is yummy!
    name the raccoon thinks plants is yummy!
    name the tiger thinks meat is yummy!
    name the tiger thinks meat is yummy!
    name the tiger thinks meat is yummy!


That's it! You've used OOP and inheritance to build a working function to help the zookeeper feed his animals the right food at the correct times!

## Summary

In this lab, you modeled a zoo and learned how to use inheritance to write nonredundant code, describe the relationship between subclasses and superclasses, and create a domain model using OOP.
