# src/testes.py
import os
import sys

# Força o Python a reconhecer a pasta 'src' para as importações
diretorio_src = os.path.dirname(os.path.abspath(__file__))
if diretorio_src not in sys.path:
    sys.path.append(diretorio_src)

try:
    from regular import SimuladorDFA
    from livre_contexto import SimuladorPDA
    from recursiva import SimuladorMT
except ImportError as e:
    print(f"\n❌ ERRO DE IMPORTAÇÃO: Não foi possível encontrar os arquivos na pasta 'src'.")
    print(f"Detalhe: {e}")
    sys.exit(1)

def carregar_massa_de_dados(caminho_arquivo):
    casos_de_teste = []
    caminho_absoluto = os.path.abspath(caminho_arquivo)
    
    if not os.path.exists(caminho_absoluto):
        print(f"⚠️ AVISO: O arquivo não foi encontrado em: {caminho_absoluto}")
        return casos_de_teste
        
    with open(caminho_absoluto, "r", encoding="utf-8") as f:
        linhas = f.readlines()
        for linha in sorted(linhas): # Garante consistência na leitura
            linha = linha.strip()
            if not linha or ";" not in linha:
                continue
            partes = linha.split(";", 1)
            cadeia = partes[0]
            esperado = partes[1].strip() == "1"
            casos_de_teste.append((cadeia, esperado))
            
    return casos_de_teste

def executar_suite():
    print("\n🔄 Iniciando os simuladores...")
    dfa = SimuladorDFA()
    pda = SimuladorPDA()
    mt = SimuladorMT()

    # Buscando a pasta exatamente no formato da sua foto: 'teste' na raiz
    pasta_raiz = os.path.dirname(diretorio_src)
    configuracao_suites = {
        "REGULAR (DFA)": (dfa, os.path.join(pasta_raiz, "teste", "testes_regular.txt")),
        "LIVRE DE CONTEXTO (PDA)": (pda, os.path.join(pasta_raiz, "teste", "testes_livre_contexto.txt")),
        "RECURSIVA (MT)": (mt, os.path.join(pasta_raiz, "teste", "testes_recursiva.txt"))
    }

    print("=" * 82)
    print(f"{'NÍVEL':<25} | {'CADEIA':<20} | {'ESPERADO':<8} | {'OBTIDO':<8} | {'PASSOS':<6}")
    print("=" * 82)

    total_testados = 0
    for nivel, (reconhecedor, caminho_arquivo) in configuracao_suites.items():
        testes = carregar_massa_de_dados(caminho_arquivo)
        if not testes:
            print(f"[{nivel}] Nenhuma cadeia carregada. Verifique o arquivo: {os.path.basename(caminho_arquivo)}")
            print("-" * 82)
            continue
            
        for cadeia, esperado in testes:
            total_testados += 1
            obtido, passos = reconhecedor.reconhecer(cadeia)
            exibicao_texto = f'"{cadeia}"' if cadeia == "" else cadeia
            print(f"{nivel:<25} | {exibicao_texto:<20} | {str(esperado):<8} | {str(obtido):<8} | {passos:<6}")
        print("-" * 82)
        
    print(f"\n✅ Fim da execução. Total de cadeias testadas: {total_testados}\n")

if __name__ == "__main__":
    executar_suite()