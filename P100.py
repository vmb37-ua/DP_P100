class P100:
    def best_solution(self, data: str) -> list[int]:
        datos = data.split()
        self.dato_n = int(datos[0])
        self.dato_l = int(datos[1])
        self.val = [int(j) for j in datos[2:]]
        self.memoizacion = {}

        resultado = self.iterative()

        return resultado

    # Tabla[n][dia]
    def iterative(self):
        n_dias = len(self.val)
        # Relleno la tabla con varias filas más de 0 para poder calcular desde el principio cualquier valor
        tabla = [[0] * (n_dias + self.dato_l) for _ in range(self.dato_n + 1)]

        for dia in range(n_dias - 1, -1, -1):
            for n in range(1, self.dato_n + 1):
                no_coger = tabla[n][dia + 1]
                coger = self.val[dia] + tabla[n - 1][dia + self.dato_l]
                tabla[n][dia] = max(no_coger, coger)

        # Reconstruyo los dias repitiendo las decisiones desde (dato_n, 0)
        resultado = []
        n = self.dato_n
        dia = 0
        while n > 0 and dia < n_dias:
            if self.val[dia] + tabla[n - 1][dia + self.dato_l] > tabla[n][dia + 1]: # Aquí revisa si el máximo era coger el dia o no
                resultado.append(dia + 1)
                n -= 1
                dia += self.dato_l
            else:
                dia += 1

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
