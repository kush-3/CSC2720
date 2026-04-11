

import hashlib


# Hash table that stores usernames as keys and hashed passwords as values.
password_table = {}


def hash_password(password):
    """Return the SHA-256 hash of the given password."""
    return hashlib.sha256(password.encode()).hexdigest()


def save_password(username, password):
    """Save a new user's password after hashing it."""
    if username in password_table:
        return f"Error: Username '{username}' is already taken."

    password_table[username] = hash_password(password)
    return f"Password saved for user: {username}"


def compare_password(username, password):
    """Check whether the given password matches the stored hashed password."""
    if username not in password_table:
        return f"Error: Username '{username}' not found."

    return password_table[username] == hash_password(password)


def change_password(username, current_password, new_password):
    """Change a user's password only if the current password is correct."""
    if username not in password_table:
        return f"Error: Username '{username}' not found."

    if not compare_password(username, current_password):
        return "Error: Current password is incorrect."

    password_table[username] = hash_password(new_password)
    return f"Password changed successfully for user: {username}"


if __name__ == "__main__":
    print(save_password("user1", "mypassword123"))
    print(save_password("user1", "newpassword456"))
    print(save_password("user2", "securepassword456"))

    print(compare_password("user1", "mypassword123"))
    print(compare_password("user1", "wrongpassword"))
    print(compare_password("user3", "any_password"))

    print(change_password("user1", "mypassword123", "updatedpassword789"))
    print(compare_password("user1", "updatedpassword789"))