# 1. Completar y probar:
def devolver_longitud_de_un_nombre(unNombre):
  return len(unNombre)

# 2. Completar y probar:
def devoler_primer_elemento_de_una_lista(unaLista):
  return unaLista[0]

# 3. Completar y probar:
def devolver_segundo_elemento_del_nombre(unNombre):
  return unNombre[1]

# 4. Completar y probar:
def devolver_ultimo_elemento_del_nombre(unNombre):
  return unNombre[-1]

# 5. Completar y probar:
def devolver_la_letra_en_posicion_del_nombre(unNombre, posicion):
  return unNombre[posicion]

# 6. Completar y probar:
def reemplazar_ultimo_elemento_de_la_lista(unaLista, unElemento):
  unaLista[-1] = unElemento
  return unaLista

# 7. Completar y probar:
def agregar_25_al_final_de_la_lista():
  lista = ["casa", 5, "A"]
  elemento = 25
  lista.append(elemento)
  return lista

# 8. Completar y probar:
def agregar_nombre_al_final_de_la_lista(unNombre):
  lista = ["casa", 5, "A"]
  lista.append(unNombre)
  return lista

# 9. Definir un función que recibe una lista de números y devuelve esa lista pero con el primer elemento
# multiplicado por 2
def multiplica_por_2_primer_numero_de_la_lista(lista_numeros):
  lista_numeros[0] = lista_numeros[0] * 2
  return lista_numeros

# 10. Definir una función que recibe una lista de números y devuelve esa lista pero con el último elemento
# multiplicado por 3
def multiplica_por_3_ultimo_numero_de_la_lista(lista_numeros):
  lista_numeros[-1] = lista_numeros[-1] * 3
  return lista_numeros

# 11. Definir un función que recibe una lista de números y devuelve esa lista pero con el primero y el
# último elemento multiplicados por 2 y 3 respectivamente (todo en una única función pero usando
# las funciones definidas en los dos puntos anteriores)
def multiplica_por_2_y_3_los_numeros_de_la_lista(lista_numeros):
  lista_numeros[0] = lista_numeros[0] * 2
  lista_numeros[-1] = lista_numeros[-1] * 3
  return lista_numeros

# 12. Definir un función que recibe una lista y un elemento, y devuelve la lista con ese elemento agregado
# al final
def agregar_elemento_a_la_lista(lista, elemento):
  lista.append(elemento)
  return lista
