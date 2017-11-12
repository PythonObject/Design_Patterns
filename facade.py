# code: utf-8
"""
Facade model
"""


class EventManager(object):

    def __init__(self):
        print "Event manager:: Let me talk to the folks\n"

    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.bookHotel()

        self.florist = Florist()
        self.florist.setFlowerReqirements()

        self.caterer = Caterer()
        self.caterer.setCuisine()

        self.musician = Musician()
        self.musician.setMusicType()


class Hotelier(object):
    def __init__(self):
        print "Arranging the Hotel for Marrige? --"

    def __isAvaliable(self):
        print "Is the Hotel free for the event on given day?"
        return True

    def bookHotel(self):
        if self.__isAvaliable():
            print "Registered the Booking\n\n"


class Florist(object):
    def __init__(self):
        print "Flower Decorations for the Event? --"

    def setFlowerReqirements(self):
        print "Carnations, Roses and Lilies would be userd for Decorations\n\n"
    

class Caterer(object):
    def __init__(self):
        print "Food Arrangements for the Event --"

    def setCuisine(self):
        print "Chinese & Contiental Cuisine to be served\n\n "


class Musician(object):
    def __init__(self):
        print "musical Arrangements for the Marriage--"

    def setMusicType(self):
        print "Jazz and Classical will be played\n\n"


class You(object):
    def __init__(self):
        print "You:: whoa! Marriage Arrangements??!!"

    def askEventManager(self):
        print "You:: Let`s Contact the Event Manager\n\n"
        em = EventManager()
        em.arrange()

    def __del__(self):
        print "You:: Thanks to Event Manager, all preparations done! Phew!"


if __name__ == "__main__":
    you = You()
    you.askEventManager()


