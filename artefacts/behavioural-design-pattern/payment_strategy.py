from abc import ABC, abstractmethod

class PaymentStrategy(ABC):

    @abstractmethod

    def pay(self, amount):

        pass

class CreditCardPayment(PaymentStrategy):

    def pay(self, amount):

        print(f"Processing credit card payment of ${amount}")



class PayPalPayment(PaymentStrategy):

    def pay(self, amount):

        print(f"Processing PayPal payment of ${amount}")



class BankTransferPayment(PaymentStrategy):

    def pay(self, amount):

        print(f"Processing bank transfer of ${amount}")



class PaymentProcessor:

    def __init__(self, strategy):

        self.strategy = strategy

    def process_payment(self, amount):

        self.strategy.pay(amount)



strategy_map = {

    "credit_card": CreditCardPayment(),

    "paypal": PayPalPayment(),

    "bank_transfer": BankTransferPayment()

}

payment_type = "paypal"

amount = 100



strategy = strategy_map.get(payment_type)

if strategy is None:

    raise ValueError("Invalid payment type")



processor = PaymentProcessor(strategy)

processor.process_payment(amount)
