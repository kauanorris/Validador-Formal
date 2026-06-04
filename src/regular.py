import sys

class SimuladorDFA:  
    def __init__(self):
        self.alfabeto = set("0123456789.-")
        self.estado_inicial = "q0"
        self.estados_finais = {"q14"}
        
        self.transicoes = {}
        self._construir_tabela()

    def _construir_tabela(self):
        digitos = "0123456789"
        esqueleto = [
            ("q0", digitos, "q1"),   
            ("q1", digitos, "q2"),   
            ("q2", digitos, "q3"),   
            ("q3", ".", "q4"),       
            ("q4", digitos, "q5"),   
            ("q5", digitos, "q6"),   
            ("q6", digitos, "q7"),   
            ("q7", ".", "q8"),       
            ("q8", digitos, "q9"),   
            ("q9", digitos, "q10"),  
            ("q10", digitos, "q11"), 
            ("q11", "-", "q12"),     
            ("q12", digitos, "q13"), 
            ("q13", digitos, "q14")  
        ]
        for est_origem, caracteres, est_destino in esqueleto:
            for char in caracteres:
                self.transicoes[(est_origem, char)] = est_destino

    def reconhecer(self, cadeia):
        estado_atual = self.estado_inicial
        passos = 0
        for simbolo in cadeia:
            if simbolo not in self.alfabeto:
                return False, passos
            chave = (estado_atual, simbolo)
            if chave in self.transicoes:
                estado_atual = self.transicoes[chave]
                passos += 1
            else:
                return False, passos
        aceito = estado_atual in self.estados_finais
        return aceito, passos

if __name__ == "__main__":
    entrada = sys.argv[1] if len(sys.argv) > 1 else ""
    dfa = SimuladorDFA()
    resultado, qtd_passos = dfa.reconhecer(entrada)
    print(f"Cadeia: '{entrada}' | Aceito: {resultado} | Passos: {qtd_passos}")