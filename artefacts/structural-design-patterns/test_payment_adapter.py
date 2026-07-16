from payment_adapter import LegacyPaymentSystem, PaymentAdapter


def test_legacy_payment_system():
    legacy = LegacyPaymentSystem()

    result = legacy.make_payment(100, "GBP")

    assert result == "SOAP payment made: 100 GBP"


def test_payment_adapter_delegates_payment():
    legacy = LegacyPaymentSystem()
    payment = PaymentAdapter(legacy)

    result = payment.pay(100, "GBP")

    assert result == "SOAP payment made: 100 GBP"


def test_payment_adapter_with_different_amount_and_currency():
    legacy = LegacyPaymentSystem()
    payment = PaymentAdapter(legacy)

    result = payment.pay(250.50, "USD")

    assert result == "SOAP payment made: 250.5 USD"
