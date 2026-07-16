import bcrypt
from password_validator import PasswordValidator

class User:
    def __init__(self, username, password_hash):
        self.username = username
        self.password_hash = password_hash

class AuthenticationSystem:
    def __init__(self):
        self.users = []
        self.failed_attempts = {}
        self.max_attempts = 3
        # Enforce a strong password policy
        self.password_schema = PasswordValidator()
        self.password_schema.min(8).has().uppercase().has().lowercase().has().digits().has().symbols()

    def add_user(self, username, password):
        if not username or not password:
            return False, "Username and password cannot be empty."

        # Enforce password strength requirements
        if not self.password_schema.validate(password):
            return False, "Password is not strong enough."
        # Hash password before storing
        password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        self.users.append(User(username, password_hash))
        return True, "User registered successfully."

    def authenticate(self, username, password):
        if not username or not password:
            return False, "Username and password cannot be empty."

        # Rate limiting to reduce brute-force attacks
        if self.failed_attempts.get(username, 0) >= self.max_attempts:
            return False, "Maximum login attempts exceeded."

        for user in self.users:
            if user.username == username:
                # Secure password verification using bcrypt
                if bcrypt.checkpw(password.encode("utf-8"), user.password_hash):
                    self.failed_attempts[username] = 0
                    return True, "Login successful."
                self.failed_attempts[username] = self.failed_attempts.get(username, 0) + 1
                return False, "Incorrect password."
        return False, "Invalid username or password."


# Usage
auth_system = AuthenticationSystem()

print("Register weak admin:", auth_system.add_user("admin", "admin123"))
print("Register strong admin:", auth_system.add_user("admin", "Admin123!"))
print("Register user1:", auth_system.add_user("user1", "Password123!"))

print("Correct login:", auth_system.authenticate("admin", "Admin123!"))
print("Wrong password:", auth_system.authenticate("admin", "wrong"))

malicious_input = "admin' OR '1'='1"
print("Injection attempt:", auth_system.authenticate(malicious_input, "anything"))

print("Brute force attempt 1:", auth_system.authenticate("user1", "wrong1"))
print("Brute force attempt 2:", auth_system.authenticate("user1", "wrong2"))
print("Brute force attempt 3:", auth_system.authenticate("user1", "wrong3"))
print("Login after max attempts:", auth_system.authenticate("user1", "Password123!"))

