from ctypes import addressof
import bcrypt 

passwords = ["hi", "hii"]
salt = bcrypt.gensalt()

hashed_password1 = bcrypt.hashpw(passwords[0].encode("utf-8"), salt)
hashed_password2 = bcrypt.hashpw(passwords[1].encode("utf-8"), salt)

print("Hashed password 1:", hashed_password1 )
print("Hashed password 2:", hashed_password2 )
print("Both of the passwords are equal:", hashed_password2 == hashed_password1)
print("\n", "\n")

hash = hash("hi")
print(hash)
