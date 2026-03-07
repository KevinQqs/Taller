class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triangulo de pascal etc.
    """
    
    def fibonacci(self, n):
        if n < 0:
            return None

        if n == 0:
            return 0
        if n == 1:
            return 1

        a = 0
        b = 1

        for _ in range(2, n + 1):
            a, b = b, a + b

        return b
    
    def secuencia_fibonacci(self, n):
        if n < 0:
            return None

        secuencia = []
        a, b = 0, 1

        for _ in range(n):
            secuencia.append(a)
            a, b = b, a + b

        return secuencia
    
    def es_primo(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def generar_primos(self, n):
        if n < 2:
            return []
        
        primos = []
        for num in range(2, n + 1):
            if self.es_primo(num):
                primos.append(num)
        
        return primos
    
    def es_numero_perfecto(self, n):
        if n < 2:
            return False
        
        suma_divisores = 1  
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                suma_divisores += i
        
        return suma_divisores == n
    
    def triangulo_pascal(self, filas):
        if filas <= 0:
            return []
        
        triangulo = []
        for i in range(filas):
            fila = [1] * (i + 1)
            for j in range(1, i):
                fila[j] = triangulo[i - 1][j - 1] + triangulo[i - 1][j]
            triangulo.append(fila)
        
        return triangulo
    
    def factorial(self, n):
        if n < 0:
            return None
        if n == 0 or n == 1:
            return 1
        
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        
        return resultado
    
    def mcd(self, a, b):
        while b:
            a, b = b, a % b
        return abs(a)
    
    def mcm(self, a, b):
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // self.mcd(a, b)
    
    def suma_digitos(self, n):
        return sum(int(digito) for digito in str(abs(n)))
    
    def es_numero_armstrong(self, n):
        if n < 0:
            return False
        
        str_n = str(n)
        num_digitos = len(str_n)
        suma = sum(int(digito) ** num_digitos for digito in str_n)
        
        return suma == n
    
    def es_cuadrado_magico(self, matriz):
        n = len(matriz)
        if n == 0 or any(len(fila) != n for fila in matriz):
            return False
        
        suma_objetivo = sum(matriz[0])
        
     
        for fila in matriz:
            if sum(fila) != suma_objetivo:
                return False
        
       
        for col in range(n):
            if sum(matriz[row][col] for row in range(n)) != suma_objetivo:
                return False
        
        
        if sum(matriz[i][i] for i in range(n)) != suma_objetivo:
            return False
        if sum(matriz[i][n - 1 - i] for i in range(n)) != suma_objetivo:
            return False
        
        return True