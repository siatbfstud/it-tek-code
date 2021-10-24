import random

liste = [1, 2, 3, 4]
liste.append(5)
print(liste[0])
liste[3] = "fire"
print(liste)

liste2 = ["en", "to", "en", "fire", "en", "seks"]

liste3 = ["not funny", "didnt laugh", "*monkey noises*"]
joke = random.randrange(len(liste3))
print(liste3[joke])
print(random.choice(liste3))

