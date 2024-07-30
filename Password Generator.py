#Password generator

import random
import string
l=int(input("Enter the password length:"))
low=string.ascii_lowercase
upp=string.ascii_uppercase
n=string.digits
s=string.punctuation
tot=low+upp+n+s
P=random.sample(total,l)
Password="".join(P)
print(Password)
