import sys

class SimuladorPDA:  
    def __init__(self):
        self.alfabeto = set("()abcdefghijklmnopqrstuvwxyz0123456789+-*/ ")
        self.estado_inicial = "q1"
        self.marcador_fundo = "Z"
        
        self.transicoes = {
            ("q1", "(", "Z"): ("q1", ("X", "Z")),
            ("q1", "(", "X"): ("q1", ("X", "X")),
            ("q1", ")", "X"): ("q1", ()),  # Tupla vazia simula o POP
        }
        
        caracteres_neutros = "abcdefghijklmnopqrstuvwxyz0123456789+-*/ "
        for char in caracteres_neutros:
            self.transicoes[("q1", char, "Z")] = ("q1", ("Z",))
            self.transicoes[("q1", char, "X")] = ("q1", ("X",))

    def reconhecer(self, cadeia):
        pilha = [self.marcador_fundo]
        estado_atual = self.estado_inicial
        passos = 0
        
        for simbolo in cadeia:
            if simbolo not in self.alfabeto:
                return False, passos
                
            if not pilha:
                return False, passos
                
            topo = pilha[-1]
            chave = (estado_atual, simbolo, topo)
            
            if chave in self.transicoes:
                pilha.pop()
                novo_estado, acao_pilha = self.transicoes[chave]
                
                for elem in reversed(acao_pilha):
                    pilha.append(elem)
                
                estado_atual = novo_estado
                passos += 1  
            else:
                return False, passos
                
        aceito = (len(pilha) == 1 and pilha[0] == self.marcador_fundo)
        return aceito, passos

if __name__ == "__main__":
    entrada = sys.argv[1] if len(sys.argv) > 1 else ""
    pda = SimuladorPDA()
    resultado, qtd_passos = pda.reconhecer(entrada)
    print(f"Cadeia: '{entrada}' | Aceito: {resultado} | Passos: {qtd_passos}")