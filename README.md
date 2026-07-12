# 🧮 Validador de Números Primos (Divisão por Tentativa)

Este repositório contém um algoritmo desenvolvido em Python para identificar se um número natural é primo. O código foi construído com foco
na aplicação de lógica estruturada, controle de fluxo de dados e matemática computacional pura.

## ⚙️ A Lógica por Trás do Código

Em vez de importar bibliotecas matemáticas complexas, o algoritmo simula o raciocínio analítico usando o método de **Divisão por Tentativa**:
1. **Laço de Repetição (`for`):** O sistema itera do número 1 até o número digitado pelo usuário.
2. **Operador de Módulo (`%`):** Em cada volta, o código testa se a divisão é exata (resto zero).
3. **Variável Acumuladora (`quantidade_de_zeros`):** O sistema atua como um contador, registrando quantas divisões exatas ocorreram durante o laço.
4. **Formatação Dinâmica (`end=" "`):** Os divisores são impressos no terminal lado a lado, em tempo real, sem quebrar a linha, otimizando a leitura visual.
5. **A Prova Real:** Ao final da execução, um bloco condicional (`if/elif/else`) avalia o total do contador. Se houver exatamente 2 divisores,
6. a premissa fundamental dos números primos é confirmada.

