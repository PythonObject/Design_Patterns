# code: utf-8
"""
factory model study
"""

from abc import ABCMeta, abstractmethod


# simple factory
class Animal(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def do_say(self):
        pass


class Dog(Animal):
    def do_say(self):
        print "Bhow Bhow!!"


class Cat(Animal):
    def do_say(self):
        print "Meow Meow!!"


# forest factory defined
class ForesFactory(object):
    """Factory"""
    def make_sound(self, object_type):
        return eval(object_type)().do_say()
        # return Animal.register(object_type)


# factory
class Section(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def describe(self):
        pass


class PersonalSection(Section):
    def describe(self):
        print "Personal Section"


class AlbumSection(Section):
    def describe(self):
        print "Album Section"


class PatenSection(Section):
    def describe(self):
        print "Paten Section"


class PublicationSection(Section):
    def describe(self):
        print "Publication Section"


class Profile(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.sections = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass

    def getSections(self):
        return self.sections

    def addSections(self, section):
        self.sections.append(section)


class linkedin(Profile):
    def createProfile(self):
        self.addSections(PersonalSection)
        self.addSections(PatenSection)
        self.addSections(PublicationSection)


class facebook(Profile):
    def createProfile(self):
        self.addSections(PersonalSection)
        self.addSections(AlbumSection)


def SignIn(profile):
    return eval(profile.lower())()


# abstract factory
class PizzaFactory(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def createVegPizza(self):
        pass

    # @abstractmethod
    def createNonVegPizza(self):
        pass


class IndianPizzaFactory(PizzaFactory):
    def createVegPizza(self):
        return DeluxVeggiePizza()

    def createNonVegPizza(self):
        return ChickenPizza()


class USPizzaFactory(PizzaFactory):
    def createVegPizza(self):
        return MexicanVegPizza()

    def createNonVegPizza(self):
        return HamPizza()


class VegPizza(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def prepare(self, VegPizza):
        pass


class DeluxVeggiePizza(VegPizza):
    def prepare(self, VegPizza):
        print "prepare: ", type(self).__name__


class MexicanVegPizza(VegPizza):
    def prepare(self, VegPizza):
        print "prepare: ", type(self).__name__


class NonVegPizza(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def serve(self, NonVegPizza):
        pass


class ChickenPizza(NonVegPizza):
    def serve(self, NonVegPizza):
        print type(self).__name__, "is served with Chicken on", type(NonVegPizza).__name__


class HamPizza(NonVegPizza):
    def serve(self, NonVegPizza):
        print type(self).__name__, "is serve with Ham on", type(NonVegPizza).__name__


class PizzaStore(object):
    def __init__(self):
        pass

    def makePizza(self):
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            self.factory = factory
            self.NonVegPizza = self.factory.createNonVegPizza()
            self.VegPizza = self.factory.createVegPizza()
            self.VegPizza.prepare(self.VegPizza)
            self.NonVegPizza.serve(self.NonVegPizza)


# client code
if __name__ == "__main__":
    # simple factory
    ff = ForesFactory()
    ff.make_sound("Cat")
    ff.make_sound("Dog")

    # factory
    aa = SignIn('LinkedIn')
    print aa.getSections()
    bb = SignIn('FaceBook')
    print bb.getSections()

    # abstract factory
    pizza_store = PizzaStore()
    pizza_store.makePizza()