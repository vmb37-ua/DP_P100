import sys

class P100:
    def best_solution(self, data: str) -> list[int]:
        datos = data.split()
        self.dato_n = int(datos[0])
        self.dato_l = int(datos[1])
        self.val = [int(j) for j in datos[2:]]
        self.memoizacion = {}

        mejor = self.recursive(self.dato_n, 0)
        resultado = [i + 1 for i in mejor[1]]

        return resultado

    # Devuelvo [v, l_dias] donde v es el valor máximo de decidir si coger o no dia y l_dias es la lista de dias a devolver
    def recursive(self, n, dia):
        if n == 0 or dia >= len(self.val):
            return [0, []]

        memo = self.memoizacion.get((n, dia))
        if memo is not None:
            return memo

        # Cada nodo debate si coger o no el siguiente dia
        mejor = self.recursive(n, dia + 1)
        rec = self.recursive(n - 1, dia + self.dato_l)
        nuevo = rec[0] + self.val[dia]

        if nuevo > mejor[0]:
            mejor = [nuevo, [dia] + rec[1]]

        self.memoizacion[(n, dia)] = mejor
        return mejor


def main():
    obj = P100()
    print(obj.best_solution("3 2 1 2 4 7 3"))

if __name__ == "__main__":
    main()
