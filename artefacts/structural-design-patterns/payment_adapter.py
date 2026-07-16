class LegacyPaymentSystem:
    def make_payment(self, amount, currency):
        return f"SOAP payment made: {amount} {currency}"

class PaymentAdapter:
    def __init__(self, legacy_system):
        self.legacy_system = legacy_system

    def pay(self, amount, currency):
        return self.legacy_system.make_payment(amount, currency)

legacy = LegacyPaymentSystem()
payment = PaymentAdapter(legacy)
print(payment.pay(100, 'GBP'))
