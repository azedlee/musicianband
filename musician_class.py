class Musician(object):
    def __init__(self, sounds, name):
        self.sounds = sounds
        self.name = name
    
    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)])
        print()


class Bassist(Musician):
    def __init__(self, name):
        super(Bassist, self).__init__(name, ["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self, name):
        super(Guitarist, self).__init__(name, ["Boink", "Bow", "Boom"])
    
    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")

class Drummer(Musician):
    def __init__(self, name):
        super(Drummer, self).__init__(name, ["Thump", "Dun", "Spang"])
    
    def countdown(self):
        for i in range(1,5):
            print(i)

class Vocalist(Musician):
    def __init__(self, name):
        super(Vocalist, self).__init__(name, ["YEAHHH", "YOOOO", "WOOOO"])

class Band(object):
    def __init__(self):
        self.myBand = []
    def hire(self, member):
        self.myBand.append(member)
        for member in self.myBand:
            print(member.name)
    def fire(self, member):
        self.myBand.remove(member)
        for member in self.myBand:
            print(member.name)
    def play(self, member):
        if isinstance(self.myBand, Drummer):
            member.countdown
        for member in self.myBand:
            member.solo

amazing = Band()
mark = Drummer("mark")
dan = Vocalist("dan")
mike = Bassist("mike")
kevin = Guitarist("kevin")
jack = Drummer("jack")
amazing.hire(mark)
amazing.hire(dan)
amazing.hire(mike)
amazing.hire(kevin)
amazing.hire(jack)
amazing.fire(mark)
amazing.play