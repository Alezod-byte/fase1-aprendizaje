nombre = "alezod"
edad = 20
altura = 1.75

print(nombre)
print(edad)
print(altura)
###
print(type(nombre))
print(type(edad))
print(type(altura))
###
es_artista = True
print(es_artista)
print(type(es_artista))
###
frase = "hola mundo"
print(frase.upper())
print(frase.capitalize())
print(frase.replace("mundo", "alezod"))
print(len(frase))
###
nombre = "alezod"
edad = 20
print(f"Me llamo {nombre} y tengo {edad} años")
print(f"El doble de mi edad es {edad * 2}")
###
palabra = "Python"
print(palabra[0])   # primer carácter
print(palabra[-1])  # último carácter
print(palabra[0:3]) # del índice 0 al 2
print(palabra[::-1]) # al revés
###
palabra = "Python"
print(palabra[::2])   # un carácter sí, uno no
print(palabra[1::2])  # empezando desde el índice 1
###
numero_texto = "42"
numero_real = int(numero_texto)
print(type(numero_texto))
print(type(numero_real))
print(numero_real + 8)
###
nombre = input("¿Cómo te llamas? ")
print(f"Hola, {nombre}!")
###
edad = int(input("¿Cuántos años tienes? "))
print(type(edad))
print(edad + 5)
###
frase = "  Hola Mundo  "
print(frase.strip())
print(frase.lower())
print(frase.find("Mundo"))
print(frase.startswith("  Hola"))
print(frase.count("o"))
###
frase = "manzana,naranja,pera"
lista = frase.split(",")
print(lista)

palabras = ["hola", "mundo", "python"]
unida = " ".join(palabras)
print(unida)