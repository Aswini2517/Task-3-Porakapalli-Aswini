
import random 
import string
length=int(input("Enter Password length:"))
chars=string.ascii_letters+string.digits
password=""
for i in range(length):
    password+=random.choice(chars)
print("Generated Password:",password)