import sys

class SimuladorMT:  
    def __init__(self):
        self.alfabeto_entrada = set("01#")
        self.branco = "_"
        self.estado_inicial = "q0"
        self.estados_finais = {"q_aceita"}
        
        self.transicoes = {
            ("q0", "0"): ("q_procura_hash_0", "X", "R"),
            ("q0", "1"): ("q_procura_hash_1", "Y", "R"),
            ("q0", "#"): ("q_verifica_fim_esq", "#", "R"),
            
            ("q_procura_hash_0", "0"): ("q_procura_hash_0", "0", "R"),
            ("q_procura_hash_0", "1"): ("q_procura_hash_0", "1", "R"),
            ("q_procura_hash_0", "#"): ("q_procura_match_0", "#", "R"),
            
            ("q_procura_match_0", "X"): ("q_procura_match_0", "X", "R"),
            ("q_procura_match_0", "Y"): ("q_procura_match_0", "Y", "R"),
            ("q_procura_match_0", "0"): ("q_retorna", "X", "L"),
            
            ("q_procura_hash_1", "0"): ("q_procura_hash_1", "0", "R"),
            ("q_procura_hash_1", "1"): ("q_procura_hash_1", "1", "R"),
            ("q_procura_hash_1", "#"): ("q_procura_match_1", "#", "R"),
            
            ("q_procura_match_1", "X"): ("q_procura_match_1", "X", "R"),
            ("q_procura_match_1", "Y"): ("q_procura_match_1", "Y", "R"),
            ("q_procura_match_1", "1"): ("q_retorna", "Y", "L"),
            
            ("q_retorna", "0"): ("q_retorna", "0", "L"),
            ("q_retorna", "1"): ("q_retorna", "1", "L"),
            ("q_retorna", "X"): ("q_retorna", "X", "L"),
            ("q_retorna", "Y"): ("q_retorna", "Y", "L"),
            ("q_retorna", "#"): ("q_retorna_esq", "#", "L"),
            
            ("q_retorna_esq", "0"): ("q_retorna_esq", "0", "L"),
            ("q_retorna_esq", "1"): ("q_retorna_esq", "1", "L"),
            ("q_retorna_esq", "X"): ("q0", "X", "R"),
            ("q_retorna_esq", "Y"): ("q0", "Y", "R"),
            
            ("q_verifica_fim_esq", "X"): ("q_verifica_fim_esq", "X", "R"),
            ("q_verifica_fim_esq", "Y"): ("q_verifica_fim_esq", "Y", "R"),
            ("q_verifica_fim_esq", "_"): ("q_aceita", "_", "R"),
        }

    def reconhecer(self, cadeia):
        if any(c not in self.alfabeto_entrada for c in cadeia):
            return False, 0
            
        fita = list(cadeia) if cadeia else [self.branco]
        cabeca = 0
        estado_atual = self.estado_inicial
        passos = 0
        max_passos = 20000  
        
        while estado_atual not in self.estados_finais and passos < max_passos:
            if cabeca >= len(fita):
                fita.append(self.branco)
            if cabeca < 0:
                fita.insert(0, self.branco)
                cabeca = 0
                
            simbolo_atual = fita[cabeca]
            chave = (estado_atual, simbolo_atual)
            
            if chave in self.transicoes:
                novo_estado, simbolo_escrito, direcao = self.transicoes[chave]
                fita[cabeca] = simbolo_escrito
                cabeca += 1 if direcao == "R" else -1
                estado_atual = novo_estado
                passos += 1  
            else:
                return False, passos
                
        return (estado_atual in self.estados_finais), passos

if __name__ == "__main__":
    entrada = sys.argv[1] if len(sys.argv) > 1 else ""
    mt = SimuladorMT()
    resultado, qtd_passos = mt.reconhecer(entrada)
    print(f"Cadeia: '{entrada}' | Aceito: {resultado} | Passos: {qtd_passos}")