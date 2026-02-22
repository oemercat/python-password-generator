import random
import string

length = int(input("Wie lang soll das Passwort sein? "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(characters) for i in range(length))

print("Dein Passwort ist:")
print(password)
