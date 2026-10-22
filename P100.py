class P100:
    def best_solution(self, data: str) -> list[int]:
        datos = data.strip()
        self.dato_n = datos[0]
        self.dato_l = datos[1]
        self.val = datos[2:]
        
        return resultado

    def recursive(self, n, l, dias):
        if n == 0:
            return 0
        
        else:
            max = 0
            for i in range(0,len(dias)):
                validos = dias[i:] # Quito todos los dias anteriores (no vuelvo)
                valor = self.recursive(n-1, l, validos[l:]) # Quito los dias dentro del rango no permitido
                if self.val[i] + valor > max :
                    max = valor + self.val[i]