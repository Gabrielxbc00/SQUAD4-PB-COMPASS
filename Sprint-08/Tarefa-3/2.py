animais = ["Elefante", "Leao", "Girafa", "Zebra", "Tigre", "Macaco", "Panda", "Cachorro", "Gato", "Pato",
           "Galinha", "Coelho", "Cavalo", "Pinguim", "Urso", "Cobra", "Aranha", "Tubarao", "Golfinho", "Baleia"]

animais_ordenados = sorted(animais)

for animal in animais_ordenados:
    print(animal)

with open('animais.csv', 'w') as file:
    for animal in animais_ordenados:
        file.write(f"{animal}\n")
