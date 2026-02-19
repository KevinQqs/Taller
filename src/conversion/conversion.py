class Conversion:
    def celsius_a_fahrenheit(self, celsius):
       
        return round((celsius * 9/5)+32, 2)
    
    def fahrenheit_a_celsius(self, fahrenheit):
   
        return round((fahrenheit - 32) * 5/9, 2)
    
    def metros_a_pies(self, metros):
       
        return round((metros *3.28084), 7)
    
    def pies_a_metros(self, pies):
      
        return round((pies *0.3048), 4)
    
    def decimal_a_binario(self, decimal):
        if decimal == 0:
            return "0"

        binario = ""
        while decimal > 0:
            binario = str(decimal % 2) + binario
            decimal //= 2

        return binario
    
    def binario_a_decimal(self, binario):
        decimal = 0

        for bit in binario:
            decimal = decimal * 2 + int(bit)
        return decimal
    
    def decimal_a_romano(self, numero):
        if not (1 <= numero <= 3999):
            raise ValueError("El número debe estar entre 1 y 3999")

        valores = [
            (1000, "M"),
            (900,  "CM"),
            (500,  "D"),
            (400,  "CD"),
            (100,  "C"),
            (90,   "XC"),
            (50,   "L"),
            (40,   "XL"),
            (10,   "X"),
            (9,    "IX"),
            (5,    "V"),
            (4,    "IV"),
            (1,    "I")
        ]

        romano = ""
        for valor, simbolo in valores:
            while numero >= valor:
                romano += simbolo
                numero -= valor

        return romano
    
    def romano_a_decimal(self, romano):
        valores = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
        }

        total = 0
        previo = 0

        for letra in reversed(romano):
            valor = valores[letra]
            if valor < previo:
                total -= valor
            else:
                total += valor
            previo = valor

        return total
    
    def texto_a_morse(self, texto):
        morse_dic = {
            "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
            "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
            "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
            "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
            "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
            "Z": "--..",
            "0": "-----", "1": ".----", "2": "..---", "3": "...--",
            "4": "....-", "5": ".....", "6": "-....", "7": "--...",
            "8": "---..", "9": "----."
        }

        texto = texto.upper()
        return " ".join(morse_dic[char] for char in texto if char in morse_dic)
    
    def morse_a_texto(self, morse):
        morse_dic = {
        ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
        "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
        "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
        ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
        "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
        "--..": "Z",
        "-----": "0", ".----": "1", "..---": "2", "...--": "3",
        "....-": "4", ".....": "5", "-....": "6", "--...": "7",
        "---..": "8", "----.": "9"
    }

        palabras = morse.split()
        return "".join(morse_dic[codigo] for codigo in palabras)