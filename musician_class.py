class Musician(object):
    def __init__(self, name, sounds):
        self.name = name
        self.sounds = sounds
    
    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)])
            print('')


class Bassist(Musician):
    def __init__(self, name, sounds):
        super(Bassist, self, sounds).__init__(name, ["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self, name):
        super(Guitarist, self, sounds).__init__(name, ["Boink", "Bow", "Boom"])
    
    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")

class Drummer(Musician):
    def __init__(self, name, sounds):
        super(Drummer, self, sounds).__init__(name, ["Thump", "Dun", "Spang"], True)
    
    def countdown(self):
        for i in range(1,5):
            print(i)

class Vocalist(Musician):
    def __init__(self, name, sounds):
        super(Vocalist, self, sounds).__init__(name, ["YEAHHH", "YOOOO", "WOOOO"])

class Band(object):
    def __init__(self):
        self.myBand = []
    def hire(self, member):
        self.myBand.append(member)
        print("Hired:", member.name)

    def fire(self, member):
        self.myBand.remove(member)
        print("Fired:", member.name)

    def play(self):
        print("Current Band Members:", end = " ")
        for members in self.myBand:
            print(members.name, end = " ")
        print("")
        for position in self.myBand:
            if isinstance(position, Drummer):
                position.solo
            else:
                pass
        for conduct in self.myBand:
            conduct.solo

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
amazing.play()