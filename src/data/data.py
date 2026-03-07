class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):
        lista_invertida = []
    
        for i in range(len(lista) - 1, -1, -1):
            lista_invertida.append(lista[i])
    
        return lista_invertida
    
    def buscar_elemento(self, lista, elemento):
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return -1
    
    def eliminar_duplicados(self, lista):
        lista_sin_duplicados = []
        
        for elemento in lista:
            existe = False
            for e in lista_sin_duplicados:
                if e == elemento and type(e) == type(elemento):
                    existe = True
                    break
            
            if not existe:
                lista_sin_duplicados.append(elemento)
        return lista_sin_duplicados
    
    def merge_ordenado(self, lista1, lista2):
        merged = []
        i = j = 0
        
        while i < len(lista1) and j < len(lista2):
            if lista1[i] < lista2[j]:
                merged.append(lista1[i])
                i += 1
            else:
                merged.append(lista2[j])
                j += 1
        
        while i < len(lista1):
            merged.append(lista1[i])
            i += 1
        
        while j < len(lista2):
            merged.append(lista2[j])
            j += 1
        
        return merged
    
    def rotar_lista(self, lista, k):
        if len(lista) == 0:
         return []
        
        k = k % len(lista)  
        return lista[-k:] + lista[:-k]
    
    def encuentra_numero_faltante(self, lista):
        n = len(lista) + 1  
        suma_esperada = n * (n + 1) // 2  
        suma_actual = sum(lista) 
        return suma_esperada - suma_actual  
    
    def es_subconjunto(self, conjunto1, conjunto2):
        return all(elem in conjunto2 for elem in conjunto1)
    
    def implementar_pila(self):
        pila = []

        def push(elemento):
            pila.append(elemento)

        def pop():
            if len(pila) == 0:
                return None
            return pila.pop()

        def peek():
            if len(pila) == 0:
                return None
            return pila[-1]

        def is_empty():
            return len(pila) == 0

        return {
            "push": push,
            "pop": pop,
            "peek": peek,
            "is_empty": is_empty
        }
    def implementar_cola(self):
        cola = []

        def enqueue(elemento):
            cola.append(elemento)

        def dequeue():
            if len(cola) == 0:
                return None
            return cola.pop(0)

        def peek():
            if len(cola) == 0:
                return None
            return cola[0]

        def is_empty():
            return len(cola) == 0

        return {
            "enqueue": enqueue,
            "dequeue": dequeue,
            "peek": peek,
            "is_empty": is_empty
        }
    
    def matriz_transpuesta(self, matriz):
        if len(matriz) == 0:
            return []
    
        filas = len(matriz)
        columnas = len(matriz[0])
        transpuesta = [[0] * filas for _ in range(columnas)]
    
        for i in range(filas):
            for j in range(columnas):
                transpuesta[j][i] = matriz[i][j]

        return transpuesta