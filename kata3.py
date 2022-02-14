print("Que velocidad tiene el asteroide?")
asteroide = input()
print("Que tamaño tiene el asteroide?")
tamano = input()
if int(asteroide) > 25:
    print("Advertencia asteroide muy cerca!!")
if int(asteroide) >= 20:
    print("Busquen el asteroide en el cielo!!")
else:
    print("Cielo despejado")
if int(asteroide) > 25 and int(tamano) >25:
    print("its time to run!!!!!!!!")