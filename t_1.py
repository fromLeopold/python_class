class Tomato:
    states = {1: 'цветочек', 2: 'зелененький', 3: 'красненький'}

    def __init__(self, arg):
        self._index = arg
        self._state = Tomato.states[self._index]

    def grow(self):
        self._index += 1
        self._state = Tomato.states[self._index]

    def is_ripe(self):
        keys = list(self.states.keys())
        last_state = max(keys)
        if self._index == last_state:
            return True


class TomatoBush:

    def __init__(self, numb):
        self.tomatoes = []
        for i in range(numb):
            tomato = Tomato(1)
            self.tomatoes.append(tomato)

    def grow_all(self):
        for i in self.tomatoes:
            if i.is_ripe() is not True:
                i.grow()

    def all_are_ripe(self):
        for i in self.tomatoes:
            if i.is_ripe() is True: continue
            else: return False
        return True

    def give_away_all(self):
        for i in range(len(self.tomatoes) - 1):
            tomato = self.tomatoes[i]
            if tomato.is_ripe() is True:
                del self.tomatoes[i]
        return len(self.tomatoes)


class Gardener:

    def __init__(self, name, tomato):
        self.name = name
        self._plant = tomato

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe(self) is True:
            self._plant.tomatoes = []
            return True
        else:
            return 'остались несозревшие плоды'

    @staticmethod
    def knowledge_base():
            return 'tomatotomatotomatotomatotomato'


print(Gardener.knowledge_base())
tomato_bush = TomatoBush(10)
Vlada = Gardener('Vlada', tomato_bush)
Vlada.work()
while Vlada.harvest() is not True:
    Vlada.work()
else:
    Vlada.harvest()
