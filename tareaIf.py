#PRIMERA PARTE
# 1. Completar y probar:
def decir_si_es_mas_grande_que_5():
  numero = 12
  return numero > 5

# 2. Completar y probar:
def decir_si_la_longitud_es_mayor_a_5():
  unNombre = "Camel Black"
  return len(unNombre) > 5

# 3. Completar y probar:
def decir_si_es_mas_grande_que(unNumero):
  if unNumero > 10:
    resultado = (str(unNumero) + " > 10")
  else: 
    resultado = (str(unNumero) + " < 10")
  return resultado

def decir_si_es_mas_grande_que(unNumero):
  if unNumero > 10:
    return True
  else:
    return False

# 4. Completar y probar:
def decir_si_es_igual_a(unNumero):
  numero = 10
  return unNumero == numero

# 5. Completar y probar:
def decir_si_la_longitud_es_igual_a(unNombre, unNumero):
  return len(unNombre) == unNumero

#SEGUNDA PARTE
#Completar y probar las siguientes funciones:
#1.-
def devolver_valor_mas_grande(valor1, valor2):
  if valor1 > valor2:
    resultado = valor1
  else:
    resultado = valor2
  return resultado

#2.-
def es_par(numero):
  resto = numero % 2
  return resto == 0
def devolver_el_doble_si_es_par(unNumero):
  if es_par(unNumero):
    resultado = unNumero * 2
  else:
    resultado = unNumero
  return resultado

#3
def devolver_segun_condicionales_locas(unNumero):
  if (unNumero == 2):
    resultado = unNumero + 1
  elif (unNumero <= 10):
    resultado = unNumero * 2
  elif (unNumero >= 20) and (unNumero <= 34):
    resultado = unNumero + 5
  else:
    resultado = 0
  return resultado

#TERCERA PARTE
#1. Definir una función que recibe un número y devuelve el doble si es más grande que 10 y menor a 20
def devolver_el_doble_si_es_mayor_10_y_menor_20(numero): #DUDAAAA!!!
  if (numero > 10) and (numero <20):
    resultado = numero * 2
  else:
    resultado = numero
  return resultado

# 2. Definir una función que recibe un número y devuelve “Rayos y Centellas” si es más grande que 20
# o menor a 5
def rayos_y_centellas(numero):
  if (numero > 20) or (numero <5):
    return "Rayos y Centellas" 
  else:
    return ""

# 3. Definir una función que recibe un número y devuelve “Está en el rango deseado” si el valor está
# entre 5 y 10 y “Fuera de Rango” en caso contrario
def rango_deseado_o_fuera_de_rango(numero):
  if (numero >= 5) and (numero <=10):
    mensaje = "Está en el rango deseado"
  else:
    mensaje = "Fuera de Rango"
  return mensaje

# 4. Definir una función que recibe un número y devuelve “Menor a 5” si el valor es menor a 5, “Entre
# 10 y 20” si el valor está entre 10 y 20, y en cualquier otro caso que devuelva “Número muy grande”
def tamanho_del_valor(numero):
  if numero < 5:
    mensaje = "Menor a 5"
  elif (numero>=10) and (numero<=20):
    mensaje = "Entre 10 y 20"
  else: 
    mensaje = "Número muy grande"
  return mensaje