from abc import ABC, abstractmethod


class Tools(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def run(self,*args,**kwargs):
        """
        执行逻辑
        :param args:
        :param kwargs:
        :return:
        """
        pass

class CalculatorTools(Tools):
    def __init__(self):
        super().__init__("Calculator")

    def run(self,a,b):
        return a+b

if __name__=="__main__":
    calc = CalculatorTools()
    print(calc.run(1,2))
    print(calc.name)
