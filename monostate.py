# coding: utf-8

__doc__ = '''
简单设计模式（monostate）意图：
1、确保有且只有一个对象被创建
2、为对象提供一个访问点，以程序可以全局访问该对象
3、控制共享资源的并行访问
'''


class Singleton(object):
    __doc__ = "只会生成一个实例"

    def __new__(cls, *args, **kwargs):
        # 使用hasattr方法检查cls是否存在instance实例，如果存在直接返回instance，如果不存在则生成一个
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


class SingletonA(object):
    __doc__ = "懒汉实例化，只有在使用对象时才实例化对象，节约资源"
    __instance = None

    def __init__(self):
        if not SingletonA.__instance:
            print "__init__ method called.."
        else:
            print "Instance already created:", self.get_instance()

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = SingletonA()
        return cls.__instance


class Borg:
    __doc__ = '''共享模式，类可以生成多个实例，但是这些实例数据相同，
    任何一个实例数据改变会引起其他实例的数据改变'''
    __shared_state = {"l": 3, "1": 2}
    # 为什么在这里添加y成员是正常的在init中添加y成员报错？
    # y = 2

    def __init__(self):
        self.x = 1
        self.y = 2
        # __dict__是类保存成员的，当定义x的时候，x被加到__dict__中，但是为什么y没有被加到__dict__中呢？
        # 当赋值后__dict__中的key就是类的成员
        self.__dict__ = self.__shared_state

        pass


#  python 3.5有效
class MyInt(type):
    __doc__ = "从元类派生的新类，即定义了一个数据类型，type(实例)结果为MyInt"

    def __call__(cls, *args, **kwargs):
        print "******Here`s My Int********"
        print "Now do  whatever you want wish these object..."
        return type.__call__(cls, *args, **kwds)


class int:
    __metaclass__ = MyInt

    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == "__main__":
    __doc__ = "self test"
    print __doc__

    print "---------------单例模式-----------------"
    s = Singleton()
    print "Object create ", s

    s1 = Singleton()
    print "Object create ", s1
    print "---------------------------------------"
    print "\n"

    print "----------------懒汉实例化---------------"
    s2 = SingletonA()
    print "Object create", SingletonA.get_instance()
    s3 = SingletonA()
    print "----------------------------------------"
    print "\n"

    print "--------------共享状态-------------------"
    a = Borg()
    a1 = Borg()
    print a.l
    print a1.l

    print "Borg object 'a':", a
    print "Borg object 'a1':", a1

    a1.x = 4
    print "Object state 'a':", a.__dict__
    print "Object state 'a1'", a1.__dict__
    # print "Object value x, y 'a':", a.x, a.y
    # print "Object Value x, y 'a1':", a1.x, a1.y
    print "-----------------------------------------"
    print "\n"

    print "---------------元类-----------------------"
    b = int(6, 7)
    print b
