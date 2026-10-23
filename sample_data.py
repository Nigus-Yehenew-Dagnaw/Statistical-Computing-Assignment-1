import random

names = ["Ana", "Ben", "Chen", "Dina", "Eli", "Faye", "Gus", "Hana", "Ivan", "Jo"]

print("name,score")
for name in names:
    print(f"{name},{random.randint(50, 100)}")