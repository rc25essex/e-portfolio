import pytest

from code_refactoring import calculate_total_price

def test_book_discount():
    items = [{"type": "book", "price": 20}]
    assert calculate_total_price(items) == 18.0


def test_electronics_discount():
    items = [{"type": "electronics", "price": 100}]
    assert calculate_total_price(items) == 80.0


def test_no_discount():
    items = [{"type": "clothing", "price": 50}]
    assert calculate_total_price(items) == 50.0


def test_multiple_items():
    items = [
        {"type": "book", "price": 20},
        {"type": "electronics", "price": 100},
        {"type": "clothing", "price": 50},
    ]

    assert calculate_total_price(items) == 148.0
