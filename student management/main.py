from abc import ABC,abstractmethod
class payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class UPI(payment):
    def pay(self,amount):
        print(f"paid {amount} using UPI")

class card(payment):
    def pay(self,amount):
        print(f"paid {amount} using card")

p1=UPI()
p1=card()
p1.pay(1000)
p1.pay(2000)