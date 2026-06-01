edad = 20

if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 13:
    print("Eres adolescente")
else:
    print("Eres niño")
####
print(10 == 10)   # igual
print(10 != 5)    # distinto
print(10 > 5)     # mayor
print(10 < 5)     # menor
print(10 >= 10)   # mayor o igual
print(10 <= 9)    # menor o igual
####
edad = 17
tiene_licencia = False

if edad >= 18 and tiene_licencia:
    print("Puedes manejar")

if edad < 18 or tiene_licencia:
    print("Alguna condición se cumple")

if not tiene_licencia:
    print("No tienes licencia")
#########
contador = 0

while contador < 5:
    print(f"Contador: {contador}")
    contador += 1

print("Terminó")
###
contador = 0

while contador < 10:
    if contador == 5:
        break
    print(contador)
    contador += 1
########
contador = 0

while contador < 10:
    contador += 1
    if contador % 2 == 0:
        continue
    print(contador)
##########
for i in range(5):
    print(i)
############3
for i in range(1, 6):
    print(i)
##############
for i in range(0, 10, 2):
    print(i)
######
frutas = ["manzana", "naranja", "pera"]

for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")