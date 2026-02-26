class Geometria:
    """
    Class with geometric exercises.
    Include basic and funny operations in 2D and 3D.
    """
    
    def area_rectangulo(self, base, altura):
        if base < 0 or altura < 0:
            return 0        
        return base*altura
    
    def perimetro_rectangulo(self, base, altura):
        if base < 0 or altura < 0:      
            return 0
        return 2*(base + altura)
    
    def area_circulo(self, radio):
        if radio < 0:
            return 0
        return 3.1416 * radio**2
    
    def perimetro_circulo(self, radio):
        if radio < 0:
            return 0
        return 2 * 3.1416 * radio
    
    def area_triangulo(self, base, altura):
        if base < 0 or altura < 0:
            return 0
        return (base * altura) / 2
    
    def perimetro_triangulo(self, lado1, lado2, lado3):
        if lado1 < 0 or lado2 < 0 or lado3 < 0:
            return 0
        return lado1 + lado2 + lado3
    
    def es_triangulo_valido(self, lado1, lado2, lado3):
        if lado1 < 0 or lado2 < 0 or lado3 < 0:
            return False
        return (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1)
    
    def area_trapecio(self, base_mayor, base_menor, altura):
        if base_mayor < 0 or base_menor < 0 or altura < 0:
            return 0
        return ((base_mayor + base_menor) / 2) * altura
    
    def area_rombo(self, diagonal_mayor, diagonal_menor):
        if diagonal_mayor < 0 or diagonal_menor < 0:
            return 0
        return (diagonal_mayor * diagonal_menor) / 2
    
    def area_pentagono_regular(self, lado, apotema):
        if lado < 0 or apotema < 0:
            return 0
        return (5 * lado * apotema) / 2
    
    def perimetro_pentagono_regular(self, lado):
        if lado < 0:
            return 0
        return 5 * lado
    
    def area_hexagono_regular(self, lado, apotema):
        if lado < 0 or apotema < 0:
            return 0
        return (6 * lado * apotema) / 2
    
    def perimetro_hexagono_regular(self, lado):
        if lado < 0:
            return 0
        return 6 * lado
    
    def volumen_cubo(self, lado):
        if lado < 0:
            return 0
        return lado**3
    
    def area_superficie_cubo(self, lado):
        if lado < 0:
            return 0
        return 6 * lado**2
    
    def volumen_esfera(self, radio):
        if radio < 0:
            return 0
        return (4/3) * 3.1416 * radio**3
    
    def area_superficie_esfera(self, radio):
        if radio < 0:
            return 0
        return 4 * 3.1416 * radio**2
    
    def volumen_cilindro(self, radio, altura):
        if radio < 0 or altura < 0:
            return 0
        return 3.1416 * radio**2 * altura
    
    def area_superficie_cilindro(self, radio, altura):
        if radio < 0 or altura < 0:
            return 0
        return 2 * 3.1416 * radio * (radio + altura)
    
    def distancia_entre_puntos(self, x1, y1, x2, y2):
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    
    def punto_medio(self, x1, y1, x2, y2):
        if x1 < 0 or y1 < 0 or x2 < 0 or y2 < 0:
            return (0, 0)
        return ((x1 + x2) / 2, (y1 + y2) / 2)
    
    def pendiente_recta(self, x1, y1, x2, y2):
        return (y2 - y1) / (x2 - x1)
    
    def ecuacion_recta(self, x1, y1, x2, y2):
        if y1 == y2:
            return (0, 1, -y1)

        A = y2 - y1
        B = x1 - x2
        C = x2*y1 - x1*y2
        return (A, B, C)
    
    def area_poligono_regular(self, num_lados, lado, apotema):
        return (num_lados * lado * apotema) / 2
    
    def perimetro_poligono_regular(self, num_lados, lado):
        if num_lados < 3 or lado < 0:
            return 0
        return num_lados * lado
