"""TERMINOS COMUNES:
Para ejecutar como variable un "def" primero se finaliza su estrcutura, luego se debe crear un  variable y que sea igual al nombre asignado de tu def.
En un def se puede usar "return" para ejecutar su salida como si se utilizace un print()

for i, jugador in enumerate() : genera un recuento de la variable que esté dentro el parentesis de la funcion enumerate(). Para ello la variable 'jugador' debe almacenar contenido con [].

max() :verifica que numero es mayor: ejemplo 'largest_number = max(number1, number2, number3)'

"""

# Listas: se determinan con []
# Diccionarios: Se define con {}
    # actualizar con .update: nombre diccionario.update({"clave": dato a actualizar})
    # pop() :elimina el último elemento
    # popitem() :elimina el último par clave: valor
    # clear() :vacia todo el diccionario
    
    # keys() :claves (primer elemento del diccionario)
    # values() :valor (segundo elemento del diccionario)
    # len() :cuenta y entrega la cantidad
    # str() :retorna una representación del diccionario en cadena
    # item() :una vista de todos los pares clave valor
    # copy() :realiza una copia del diccionario

# .upper() :Transforma todos los caracteres en MAYÚSCULAS.
# .isupper() :verifica con un True si todos los caracteres alfabeticos son Mayúsculas.
# .islower() :verifica con un True si todos los caracteres alfabeticos son minúsculas.
# .lower() :Transforma todos los caracteres en MINÚSCULAS.
# .isdigit() :Verifica si todos los valores agregados son numéricos.
# .append() :agrega un elemento al final de una lista
# :.0f :se agrega dentro un print, despues de tu variable para definir cuantos decimales tendrá en un flotante (sin decimales al ser 0).
# ** :se eleva un numero
# . isdisjoint() :Verificar elementos en común
# .startswith() :para iniciar con un valor especifico.
# .count(x) :cuenta cuantos "x" hay

"""EJEMPLOS PARA DICCIONARIOS:

#Iterar sobre las claves for indice in diccionario (crea una columna de los datos):
#print()

for key in diccionario_autos_copia:
    print(key)

#Iterar sobre los valores .values() (crea una columna de los datos)
for value in diccionario_autos_copia.values():
    print(value)

#Iterar sobre clave valor for indice1, indice in diccionario.items() (Imprime en columna las claves y key del diccionario):
for value, key in diccionario_autos_copia.items():
    print(value, key)

"""

#try:
#Cuando el archivo no existe o la ruta esta mal escrita:
    # except FileNotFoundError:
# Error al acceder al diccionario y el tipo de dato no existe
    # except KeyError:
#Cuando el tipo de dato no es compatible
    # except TypeError:
 #Cuando se proporciona un valor inapropiado al pedido
    # except valueError:
#División por 0
    # except ZeroDivisionError: print("No se puede dividir por 0")
#Finally: Se ejecuta si o si

"""
#Crear un archivo de texto .txt
def crear_archivo_texto(nombre_archivo, contenido):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(contenido)
    print(f"archivo TXT: {nombre_archivo} creado exitosamente")

#Funcion para crear archivo CSV
def crear_archivo_csv(nombre_archivo, datos):
    with open(nombre_archivo, 'w') as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerows(datos)
    print(f"archivo CSV: {nombre_archivo} creado exitosamente")

#Crear un JSON
def crear_archivo_json(nombre_archivo, datos):
    with open(nombre_archivo, 'w') as archivo:
        json.dump(datos, archivo, indent=4)
    print(f"archivo json: {nombre_archivo} creado exitosamente")

#leer archivo txt
def leer_archivo_txt(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        return archivo.read()

#Leer archivo csv
def leer_archivo_csv(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        return list(csv.reader(archivo))

#Leer archivo json
def leer_archivo_json(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        return json.load(archivo)

#Mostrar y leer el archivo csv
for fila in leer_archivo_csv('ejemplo.csv'):
    print(fila)

#Mostrar y leer el archivo json
print(json.dumps(leer_archivo_json('ejemplo.json'), indent=4))


"""
#
#
#
""""EJ. COMUNES:

#Imprimir par  e impar del 1 al 100.
for num in range(1,100):
    if num % 2 == 0: 
        print(f"el número {num} es par")
    else: print(f"el número {num} es impar")

#Calculadora cpn def, o Función anidada
def operacion_anidada(a,b):
    def suma(numero1, numero2):
        return numero1 + numero2
    def multiplicar(numero1, numero2):
        return numero1*numero2
    total_suma = suma(a,b)
    total_multiplicacion = multiplicar(a,b)
    return total_suma, total_multiplicacion
print(....)
    
"""
print("watafak")