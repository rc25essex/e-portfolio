import pytest
from password_validation import AuthenticationSystem


def test_register_valid_user():
    auth = AuthenticationSystem()

    success, message = auth.add_user("admin", "Admin123!")

    assert success is True
    assert message == "User registered successfully."


def test_register_weak_password():
    auth = AuthenticationSystem()

    success, message = auth.add_user("admin", "admin123")

    assert success is False
    assert message == "Password is not strong enough."


def test_register_empty_username():
    auth = AuthenticationSystem()

    success, message = auth.add_user("", "Admin123!")

    assert success is False
    assert message == "Username and password cannot be empty."


def test_successful_login():
    auth = AuthenticationSystem()
    auth.add_user("admin", "Admin123!")

    success, message = auth.authenticate("admin", "Admin123!")

    assert success is True
    assert message == "Login successful."


def test_wrong_password():
    auth = AuthenticationSystem()
    auth.add_user("admin", "Admin123!")

    success, message = auth.authenticate("admin", "WrongPassword1!")

    assert success is False
    assert message == "Incorrect password."


def test_invalid_username():
    auth = AuthenticationSystem()

    success, message = auth.authenticate("unknown", "Password123!")

    assert success is False
    assert message == "Invalid username or password."


def test_empty_login():
    auth = AuthenticationSystem()

    success, message = auth.authenticate("", "")

    assert success is False
    assert message == "Username and password cannot be empty."


def test_account_lock_after_three_attempts():
    auth = AuthenticationSystem()
    auth.add_user("user1", "Password123!")

    auth.authenticate("user1", "wrong1")
    auth.authenticate("user1", "wrong2")
    auth.authenticate("user1", "wrong3")

    success, message = auth.authenticate("user1", "Password123!")

    assert success is False
    assert message == "Maximum login attempts exceeded."


def test_failed_attempts_reset_after_successful_login():
    auth = AuthenticationSystem()
    auth.add_user("admin", "Admin123!")

    auth.authenticate("admin", "wrong")
    auth.authenticate("admin", "Admin123!")

    assert auth.failed_attempts["admin"] == 0


def test_sql_injection_attempt():
    auth = AuthenticationSystem()
    auth.add_user("admin", "Admin123!")

    success, message = auth.authenticate(
        "admin' OR '1'='1",
        "anything"
    )

    assert success is False
    assert message == "Invalid username or password."
