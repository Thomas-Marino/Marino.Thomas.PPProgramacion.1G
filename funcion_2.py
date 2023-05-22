#2. Crear una función que se llame reemplazarCaracteres que reciba una cadena de caracteres como primer parámetro,
# un carácter como segundo y otro carácter  como tercero,  
# la misma deberá reemplazar cada ocurrencia del segundo parámetro por el tercero y devolver 
# la cantidad de veces que se reemplazo ese carácter  en la cadena

def reemplazarCaracteres (cadena_de_caracteres:str, caracter_unico_1:str, caracter_unico_2:str):
    sub_cadena = list(cadena_de_caracteres)
    contador = 0
    for i in range(len(sub_cadena)):
        if caracter_unico_1 == sub_cadena [i]:
            sub_cadena [i] = caracter_unico_2
            contador += 1
    print(f"Se reemplazaron un total de: {contador} caracteres.")
    cadena_de_caracteres = "".join(sub_cadena)
    return cadena_de_caracteres
