class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        texto = texto.lower().replace(" ", "")
    
        texto_invertido = ""
        for i in range(len(texto) - 1, -1, -1):
            texto_invertido += texto[i]
    
        return texto == texto_invertido
    
    def invertir_cadena(self, texto):
        texto_invertido = ""
    
        for i in range(len(texto) - 1, -1, -1):
            texto_invertido += texto[i]
    
        return texto_invertido
    
    def contar_vocales(self, texto):
        vocales = "aeiouAEIOU"
        contador = 0
    
        for char in texto:
            if char in vocales:
                contador += 1
    
        return contador
    
    def contar_consonantes(self, texto):
        vocales = "aeiouAEIOU"
        contador = 0

        for char in texto:
            if not char.isalpha():
                continue

            if char in vocales:
                continue

            if char.lower() == "y":  # no contar Y ni y
                continue

            contador += 1

        return contador
    
    def es_anagrama(self, texto1, texto2):
        texto1 = texto1.replace(" ", "").lower()
        texto2 = texto2.replace(" ", "").lower()
    
        if len(texto1) != len(texto2):
            return False
    
        for char in texto1:
            if char not in texto2:
                return False
            texto2 = texto2.replace(char, "", 1)
    
        return True
    
    def contar_palabras(self, texto):
        palabras = texto.split()
        return len(palabras)
    
    def palabras_mayus(self, texto):
        resultado = ""
        nueva_palabra = True

        for char in texto:
            if char == " ":
                resultado += char
                nueva_palabra = True
            else:
                if nueva_palabra:
                    resultado += char.upper()
                    nueva_palabra = False
                else:
                    resultado += char.lower()

        return resultado
    
    def eliminar_espacios_duplicados(self, texto):
        resultado = ""
        espacio_anterior = False
    
        for char in texto:
            if char == " ":
                if not espacio_anterior:
                    resultado += char
                espacio_anterior = True
            else:
                resultado += char
                espacio_anterior = False
    
        return resultado
    
    def es_numero_entero(self, texto):
        if texto.startswith("-"):
            return texto[1:].isdigit()
        return texto.isdigit()
    
    def cifrar_cesar(self, texto, desplazamiento):
        texto_cifrado = ""
    
        for char in texto:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                texto_cifrado += chr((ord(char) - base + desplazamiento) % 26 + base)
            else:
                texto_cifrado += char
    
        return texto_cifrado
    
    def descifrar_cesar(self, texto, desplazamiento):
        return self.cifrar_cesar(texto, -desplazamiento)
    
    def encontrar_subcadena(self, texto, subcadena):
        if subcadena == "":
            return []
    
        posiciones = []
    
        for i in range(len(texto) - len(subcadena) + 1):
            if texto[i:i+len(subcadena)] == subcadena:
             posiciones.append(i)
    
        return posiciones