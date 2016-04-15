class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds
    
    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)])
        print()


class Bassist(Musician):
    def __init__(self):
        super(Bassist, self).__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        super(Guitarist, self).__init__(["Boink", "Bow", "Boom"])
    
    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")

class Drummer(Musician):
    def __init__(self):
        super(Drummer, self).__init__(["Thump", "Dun", "Spang"])
    
    def countdown(self):
        for i in range(1,5):
            print(i)

class Vocalist(Musician):
    def __init__(self):
        super(Vocalist, self).__init__(["YEAHHH", "YOOOO", "WOOOO"])

class Band(object):
    def __init__(self):
        self.members = []
    def hire(self, member):
        self.members.append(member)
        for member in self.members:
            print(member.name)
    def fire(self, member):
        self.members.remove(member)
        for member in self.members:
            print(member.name)
    def bandplay(self, members):
        