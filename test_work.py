''' веселые животные '''


class Animal:
    ''' класс животные делают разные действия '''
    breed = ['dog', 'cat']

    def __init__(self):
        ''' '''
        pass


class dog(Animal):
    ''' класс собака - делает действия'''

    def __init__(self, breed):
        self.breed = breed

    def shout(self):
        print('Гав! Я %s!' % self.breed)

    def master(self, isMaster):
        if (isMaster == True):
            print('Я виляю хвостиком!')
        if (isMaster == False):
            print('Гав! Гав! Чужак!')


my_dog = dog('Овчарка')
my_dog.shout()
my_dog.master(True)


class cat(Animal):
    '''класс кошка - делает действия'''

    def __init__(self, breed):
        self.breed = breed

    def shout(self):
        print('Мяу! Я %s!' % self.breed)

    def master(self, isMaster):
        if (isMaster == True):
            print('Я хочу есть!')
        if (isMaster == False):
            print('Мяу! Мяу! Мяу!')


my_cat = cat('кошка')
my_cat.shout()
my_cat.master(True)
