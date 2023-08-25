#Definir variables de tipo primitivo

entero = 5
float = 3.1416
bool = True
String = "Liz"

#Concatena la cadena las variables
result_concatenado = "Mi nombre es " + str(String) + ". Tengo " + str(entero) +" gatos. El valor de pi es " + str(float) +"?  Eso es " + str(bool)


# Límite de los enteros y los flotantes en Python
limite_entero = 2**31 - 1  # Límite para enteros con signo de 32 bits
limite_flotante = 1.8e308  # Mayor valor representable en punto flotante

# Fórmula para la suma de los primeros n números pares
n = entero
suma_pares = n * (n + 1)
 
 
print(result_concatenado)
print("El limite entero es: " + str(limite_entero))
print("El limite flotante es: " + str(limite_flotante))
print("La suma de los primeros n numeros pares es " + str(suma_pares))