class P100:
    def best_solution(self, data: str) -> list[int]:
        datos = data.strip().split(" ")
        self.dato_n = int(datos[0])
        self.dato_l = int(datos[1])
        self.val = datos[2:]
        self.val = [int(j) for j in self.val]

        resultado = self.recursive(self.dato_n, self.val)
        
        return resultado

    def quitar_dias(self, lista, m):
        for i in range(0,min(self.dato_l, len(lista)-m-1)):
            lista[m+i] = -1
        for i in range(1, m-self.dato_l if m-self.dato_l>=0 else m):
            lista[m-i] = -1
        return lista
                
    def recursive(self, n, dias):
        if n == 0:
            print(f"Lista de n={n}: {dias}, {0}")
            return [0, dias]
        
        else:
            max = 0
            lista = dias
            for i in range(0,len(dias)):
                rec = self.recursive(n-1, dias)
                nuevo = rec[0]+dias[i]
                if nuevo >= max:
                    max = nuevo
                    lista = self.quitar_dias(rec[1], i)
            print(f"Lista de n={n}: {lista}, {max}")
            return [max, lista]

def main():
    obj = P100()
    print(obj.best_solution("2 3 1 7 4"))
    print(obj.quitar_dias([0,1,2,3,4,5,6,7], 4))

if __name__ == "__main__":
    main()


