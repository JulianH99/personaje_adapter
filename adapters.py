from abc import ABC, abstractmethod
from jugador import Personaje

class AbstractAdapter(ABC):

    @abstractmethod
    def shoot(self):
        pass
    
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def paint(self, window):
        pass


class CharacterAdapter(AbstractAdapter, Personaje):

    def __init__(self):
        Personaje.__init__(self)

    def shoot(self, x, y):
        self.disparar(x, y)

    def paint(self, window):
        self.dibujar(window)

    def move(self):
        self.mover()




    

