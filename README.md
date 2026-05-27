# Sistema Unificado de Validação Formal — Hierarquia de Chomsky

Este projeto consiste no desenvolvimento e análise empírica de um sistema aplicado de validação formal contendo três reconhecedores independentes, cada um correspondendo a um nível estrito da Hierarquia de Chomsky:
1. **Linguagem Regular (LR):** Validador do formato tipográfico e estrutural de CPF brasileiro.
2. **Linguagem Livre de Contexto (LLC):** Verificador de balanceamento de parênteses e escopos em expressões algébricas.
3. **Linguagem Recursiva (R):** Validador de integridade e espelhamento binário de pacotes no formato $w\#w$.

A meta central do trabalho é evidenciar na prática a inclusão estrita $LR \subsetneq LLC \subsetneq R$, analisando as restrições de armazenamento, direções de varredura e a volumetria de passos assintóticos de cada modelo computacional sem o uso de condicionais de fluxo tradicionais (`if/elif/else`).

---

## 🎯 Estrutura do Projeto

A organização dos arquivos no repositório segue estritamente a arquitetura de módulos limpos e isolados exigida pela especificação:

```text
.
├── README.md                # Instruções completas de compilação, execução e testes
├── testes.py                # Script orquestrador da bateria completa de testes automatizados
├── src/                     # Código-fonte dos simuladores de autômatos
│   ├── __init__.py          # Inicializador do pacote python
│   ├── regular.py           # Simulador de Autômato Finito Determinístico (DFA)
│   ├── livre_contexto.py    # Simulador de Autômato a Pilha Determinístico (PDA)
│   └── recursiva.py         # Simulador de Máquina de Turing de Fita Única (MT)
└── teste/                   # Arquivos de dados textuais com as cadeias de teste
    ├── testes_regular.txt       # Casos de teste para a máscara de CPF
    ├── testes_livre_contexto.txt # Casos de teste para expressões algébricas
    └── testes_recursiva.txt     # Casos de teste para o espelhamento w#w
