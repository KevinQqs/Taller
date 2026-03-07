class Matrix:
    """
    Clase con métodos para operaciones sobre matrices.
    Incluye operaciones aritméticas, propiedades y transformaciones matriciales.
    """

    def suma_matrices(self, A, B):
    
        if len(A) != len(B) or len(A[0]) != len(B[0]):
            raise ValueError("Las matrices deben tener las mismas dimensiones")

        resultado = []

        for i in range(len(A)):
            fila = []
            for j in range(len(A[0])):
                fila.append(A[i][j] + B[i][j])
            resultado.append(fila)

        return resultado

    def resta_matrices(self, A, B):
        if len(A) != len(B) or len(A[0]) != len(B[0]):
            raise ValueError("Las matrices deben tener las mismas dimensiones")

        resultado = []

        for i in range(len(A)):
            fila = []
            for j in range(len(A[0])):
                fila.append(A[i][j] - B[i][j])
            resultado.append(fila)

        return resultado

    def multiplicar_matrices(self, A, B):
        if len(A[0]) != len(B):
            raise ValueError("El número de columnas de A debe ser igual al número de filas de B")

        resultado = []

        for i in range(len(A)):
            fila = []
            for j in range(len(B[0])):
                suma = 0
                for k in range(len(A[0])):
                    suma += A[i][k] * B[k][j]
                fila.append(suma)
            resultado.append(fila)

        return resultado

    def multiplicar_escalar(self, matriz, escalar):
        resultado = []

        for i in range(len(matriz)):
            fila = []
            for j in range(len(matriz[0])):
                fila.append(matriz[i][j] * escalar)
            resultado.append(fila)

        return resultado

    def transpuesta(self, matriz):
        if len(matriz) == 0:
            return []

        resultado = []

        for j in range(len(matriz[0])):
            fila = []
            for i in range(len(matriz)):
                fila.append(matriz[i][j])
            resultado.append(fila)

        return resultado   

    def es_cuadrada(self, matriz):
        if len(matriz) == 0:
            return False
        return len(matriz) == len(matriz[0])

    def es_simetrica(self, matriz):
        if not self.es_cuadrada(matriz):
            return False

        for i in range(len(matriz)):
            for j in range(i, len(matriz[0])):
                if matriz[i][j] != matriz[j][i]:
                    return False

        return True

    def traza(self, matriz):
        if not self.es_cuadrada(matriz):
            raise ValueError("La matriz debe ser cuadrada")

        suma = 0
        for i in range(len(matriz)):
            suma += matriz[i][i]

        return suma

    def determinante_2x2(self, matriz):
        if len(matriz) != 2 or len(matriz[0]) != 2:
            raise ValueError("La matriz debe ser 2x2")

        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

    def determinante_3x3(self, matriz):
        if len(matriz) != 3 or any(len(fila) != 3 for fila in matriz):
            raise ValueError("La matriz debe ser 3x3")

        return (
        matriz[0][0]*matriz[1][1]*matriz[2][2]
        + matriz[0][1]*matriz[1][2]*matriz[2][0]
        + matriz[0][2]*matriz[1][0]*matriz[2][1]
        - matriz[0][2]*matriz[1][1]*matriz[2][0]
        - matriz[0][0]*matriz[1][2]*matriz[2][1]
        - matriz[0][1]*matriz[1][0]*matriz[2][2]
        )

    def identidad(self, n):
        resultado = []

        for i in range(n):
            fila = []
            for j in range(n):
                if i == j:
                    fila.append(1)
                else:
                    fila.append(0)
            resultado.append(fila)

        return resultado

    def diagonal(self, matriz):
        if not self.es_cuadrada(matriz):
            raise ValueError("La matriz debe ser cuadrada")

        resultado = []

        for i in range(len(matriz)):
            resultado.append(matriz[i][i])

        return resultado

    def es_diagonal(self, matriz):
        if not self.es_cuadrada(matriz):
            return False

        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if i != j and matriz[i][j] != 0:
                    return False

        return True

    def rotar_90(self, matriz):
        resultado = []

        for j in range(len(matriz[0])):
            fila = []
            for i in range(len(matriz) - 1, -1, -1):
                fila.append(matriz[i][j])
            resultado.append(fila)

        return resultado

    def buscar_en_matriz(self, matriz, valor):
        posiciones = []

        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if matriz[i][j] == valor:
                    posiciones.append((i, j))

        return posiciones