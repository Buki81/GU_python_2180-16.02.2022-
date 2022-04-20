from abc import ABC, abstractmethod
class Clothes(ABC):
    consumption = 0

    @abstractmethod
    def calculation(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v
        Clothes.consumption += self.calculation

    @property
    def calculation(self):
        cut = self.v / 6.5 + 0.5
        return float(f'{cut:.02f}')

    def __str__(self):
        return f' Размер пальто: {self.v}, расход ткани: {self.calculation} пог.м, ' \
               f'общий расход ткани: {Clothes.consumption:.02f} пог.м'



class Suit(Clothes):
    def __init__(self, h):
        self.h = h
        Clothes.consumption += self.calculation

    @property
    def calculation(self):
        cut = self.h * 2 + 0.3
        return float(f'{cut:.02f}')

    def __str__(self):
        return f' Размер костюма: {self.h}, расход ткани: {self.calculation} пог.м, ' \
               f'общий расход ткани: {Clothes.consumption:.02f} пог.м'



coat = Coat(56)
print(coat)
suit = Suit(46)
print(suit)
