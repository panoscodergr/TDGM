import math

class Algebra:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Δεν μπορείς να διαιρέσεις με το μηδέν!")
        return a / b

    @staticmethod
    def square_root(a):
        if a < 0:
            raise ValueError("Δεν μπορείς να πάρεις την τετραγωνική ρίζα αρνητικού αριθμού!")
        return math.sqrt(a)
