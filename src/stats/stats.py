class Stats:
    def promedio(self, numeros):
        if not numeros:
            return 0
        return sum(numeros) / len(numeros)
    
    def mediana(self, numeros):
        if not numeros:
            return 0
        sorted_nums = sorted(numeros)
        n = len(sorted_nums)
        if n % 2 == 1:
            return sorted_nums[n // 2]
        else:
            mid1 = sorted_nums[n // 2 - 1]
            mid2 = sorted_nums[n // 2]
            return (mid1 + mid2) / 2
    
    def moda(self, numeros):
        if not numeros:  # Lista vacía
            return None
        frequency = {}
        for num in numeros:
            frequency[num] = frequency.get(num, 0) + 1
        max_freq = max(frequency.values())
        for num in numeros:
            if frequency[num] == max_freq:
                return num

    
    def desviacion_estandar(self, numeros):
    
        if not numeros:
            return 0
        promedio = self.promedio(numeros)
        varianza = sum((x - promedio) ** 2 for x in numeros) / len(numeros)
        return varianza ** 0.5
    
    def varianza(self, numeros):
    
        if not numeros:
            return 0
        promedio = self.promedio(numeros)
        varianza = sum((x - promedio) ** 2 for x in numeros) / len(numeros)
        return varianza
    
    def rango(self, numeros):

        if not numeros:
            return 0
        return max(numeros) - min(numeros)