# 3. Crear una función que se llame ordenarCaracteres que reciba una cadena de 
# caracteres como parámetro  y su responsabilidad es ordenarlos caracteres 
# de manera ascendente dentro de la cadena. Ejemplo si le pasamos "algoritmo" la deja como "agilmoort"

def ordenarCaracteres (cadena:str, orden:str):
    i = 0
    j = 0
    sub_cadena = list(cadena)
    if orden == "des":
        while i < len(sub_cadena):
            while j < len(sub_cadena) - 1:
                if sub_cadena [j] < sub_cadena [j+1]:
                        elemento_auxiliar = sub_cadena [j+1]
                        sub_cadena [j+1] = sub_cadena [j]
                        sub_cadena [j] = elemento_auxiliar
                        j = 0
                j += 1
            i += 1
    if orden == "asc":
        while i < len(sub_cadena):
            while j < len(sub_cadena) - 1:
                if sub_cadena [j] > sub_cadena [j+1]:
                        elemento_auxiliar = sub_cadena [j+1]
                        sub_cadena [j+1] = sub_cadena [j]
                        sub_cadena [j] = elemento_auxiliar
                        j = 0
                j += 1
            i += 1
    cadena = "".join(sub_cadena)
    return cadena

