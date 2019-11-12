class Musician(object):

    def __init__(self, name): # We'll set name at instantiation time to demonstrate passing in arguments to super().__init__()
        self.name = name
        self.band = "The Beatles"

    def tune_instrument(self):
        print("Tuning Instrument!")

    def practice(self):
        print("Practicing!")

    def perform(self):
        print("Hello New York!")

class Singer(Musician):

    def __init__(self, name):
        super().__init__(name)  # Notice how we pass in name argument from init to the super().__init() method, because it expects it
        self.role = "Singer"

    def tune_instrument(self):
        print("No tuning needed--I'm a singer!")

class Guitarist(Musician):

    def __init__(self, name):
        super().__init__(name)
        self.role = "Guitarist"

    def practice(self):
        print("Strumming the old 6 string!")

class Bass_Guitarist(Guitarist):

    def __init__(self, name):
        super().__init__(name)
        self.role = "Bass Guitarist"

    def practice(self):
        print("I play the Seinfeld Theme Song when I get bored")

    def perform(self):
        super().perform()
        print("Thanks for coming out!")

class Drummer(Musician):

    def __init__(self, name):
        super().__init__(name)
        self.role = "Drummer"

    def tune_instrument(self):
        print('Where did I put those drum sticks?')

    def practice(self):
        print('Why does my chair still say "Pete Best"?')
        
