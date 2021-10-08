from abc import ABC, abstractmethod
from math import pi
class Shape(ABC):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    @abstractmethod
    def area():
        pass

class square(Shape):
    def area(self,w,h):
        self.area = w*h
        return(self.area)

class circle(Shape):
    def area(self,r):
        self.area = pi *r*r
        return(self.area)
class rectangle(Shape):
    def area(self,w,h):
        self.area = w*h
        return(self.area)