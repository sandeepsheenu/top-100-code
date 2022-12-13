from abc import ABC, abstractmethod
class sandeep(ABC):
    @abstractmethod
    def fun1(self):
         pass

class san(sandeep):
    def fun1(self):
        print("fun in child class")
                

ob=san()
ob.fun1()
