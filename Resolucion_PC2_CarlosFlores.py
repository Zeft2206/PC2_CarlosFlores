#%%Ejercicio 1
numero = 1500
divisor = 35
max = 2700

print("Los numeros divisibles entre 7 y multiplos de 5 son:")
while numero <= max:    
    if numero % divisor == 0:
     print(f'{numero}')
    numero = numero + 1

#%% Ejercicio 2
asterisco = int(1) 
max = 5
while asterisco <= max: 
   if asterisco <= max:
       print("*"*asterisco)
       asterisco = asterisco + 1
asterisco = max - 1
while asterisco >= 1:
    if asterisco >= 1:
       print("*"*asterisco)
       asterisco = asterisco - 1

#%% Ejercicio 3
Numeros_Insertados = []
Accion = input("¿Desea ingresar un número?")
while Accion == "SI":
   i = int(input("Ingrese el número"))
   Numeros_Insertados.append(i)
   Accion = input("¿Desea ingresar un número?")
   if Accion == "NO":
      break
print(Numeros_Insertados)

#%% Ejercicio 4

Alumno = {
    'Nombre': '',
    'Notas': []

}
Cantidad_notas = 3
Alumnos = []
Notas_obtenidas = []
n = int(input("Ingrese la cantidad de alumnos:"))
while i < n:
    ID = input("Ingresar nombre del alumno:")
    

    

    
 




Alumnos.append({'Nombre': ID })

#%% Ejercicio 5
def num(entero,digito):
 
 my_numero = str(entero)
 my_digito = str(digito)
 my_numero.count(my_digito)

print(num(0,1500))





#%% Ejercicio 6
def fibo(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a+b
    print()
fibo(20)


# %% Ejercicio 7
def es_primo(num, n=2):
    if n >= num:
        print("Es primo")
        return True
    elif num % n != 0:
        return es_primo(num, n + 1)
    else:
        print("No es primo", n, "es divisor")
        return False
     
    
print(es_primo(11))
   

# %% Ejercicio 8
def factorial(n):
   if n==0 or n==1:
            resultado=1
   elif n>1:
            resultado=n*factorial(n-1)
   return resultado

print(factorial(3))


#%% Ejercicio 9
vocales = ("a","e","i","o","u")
texto = input("Ingresa tu texto:")
nuevo_texto = ""
for i in texto:
    if i not in vocales:
        nuevo_texto = nuevo_texto + i

print(nuevo_texto)
print(len(nuevo_texto))

# %%
