from payment_strategy import (
    PaymentProcessor,
    CreditCardPayment,
    PayPalPayment,
    BankTransferPayment,
)


def test_paypal_payment(capsys):
    processor = PaymentProcessor(PayPalPayment())

    processor.process_payment(100)

    captured = capsys.readouterr()
    assert captured.out.strip() == "Processing PayPal payment of $100"


def test_credit_card_payment(capsys):
    processor = PaymentProcessor(CreditCardPayment())

    processor.process_payment(75)

    captured = capsys.readouterr()
    assert captured.out.strip() == "Processing credit card payment of $75"


def test_bank_transfer_payment(capsys):
    processor = PaymentProcessor(BankTransferPayment())

    processor.process_payment(250)

    captured = capsys.readouterr()
    assert captured.out.strip() == "Processing bank transfer of $250"
