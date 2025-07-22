
from abc import abstractmethod, ABC


class PaymentService(ABC):

    @abstractmethod
    def make_payment(self):
        pass

    @abstractmethod
    def get_payment_details(self):
        pass


class PaymentService1(PaymentService):

    def __init__(self):
        super().__init__()

    def make_payment(self):
        return super().make_payment()
    
    def get_payment_details(self):
        return super().get_payment_details()