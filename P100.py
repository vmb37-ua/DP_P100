class P100:
    def best_solution(self, data: str) -> list[int]:
        datos = data.strip().split(" ")
        self.dato_n = int(datos[0])
        self.dato_l = int(datos[1])
        self.val = datos[2:]
        self.val = [int(j) for j in self.val]
        self.memoizacion = {}

        mejor = self.recursive(self.dato_n, self.val)
        resultado = sorted(i+1 for i in mejor[1])

        return resultado

    def quitar_dias(self, lista, m):
        lista = lista.copy()
        for i in range(max(0, m-self.dato_l+1), min(len(lista), m+self.dato_l)):
            lista[i] = -1
        return lista
                
    def recursive(self, n, dias):
        if n == 0:
            return [0, []]

        else:

            memo = self.memoizacion.get([n,dias], False)
            if memo:
                return memo  

            mejor = [0, []]
            for i in range(0,len(dias)):
                if dias[i] == -1:
                    continue
                rec = self.recursive(n-1, self.quitar_dias(dias, i))
                nuevo = rec[0]+dias[i]
                if nuevo > mejor[0]:
                    mejor = [nuevo, rec[1] + [i]]

            memo[[n, dias]] = mejor
            return mejor

def main():
    obj = P100()
    print(obj.best_solution("20 2 1 2 4 7 3 5 7 2 4 9 4 5 2 2 3 5 9 1 0 7 8"))

if __name__ == "__main__":
    main()


