# Validador de Números Primos

Um programa simples, eficiente para pequenos números e altamente didático, desenvolvido em Python, para verificar se um número natural é primo.

## Sobre o Projeto

Este script não apenas diz se um número é primo ou não, mas **prova** o resultado na tela. Ele calcula e exibe todos os divisores do número informado, 
aplicando a regra fundamental da aritmética de forma visual. 

É uma excelente ferramenta para ambientes educacionais, facilitando o ensino de conceitos de divisibilidade e lógica de programação de forma integrada.

## Funcionalidades Principais

* Demonstração Visual:** Imprime no terminal todos os divisores exatos do número analisado.
* Validação Lógica:** Conta a quantidade de divisores para determinar a primalidade.
* Tratamento de Exceções Matemáticas: Identifica e explica corretamente por que o número `1` não é considerado primo por definição matemática,
* além de relatar a quantidade exata de divisores para números compostos.

## Limitações e Complexidade Computacional

Por ter um foco estritamente didático e de demonstração visual (imprimir todos os divisores), este algoritmo utiliza um laço de repetição com complexidade 
de tempo linear O(N). Isso significa que ele testa a divisão por todos os números inteiros de 1 até N.

* **Ideal para números menores:** Funciona de forma instantânea para números de até 8 algarismos (casa das dezenas de milhões).
* **Inviabilidade para números gigantes:** A partir de 9 a 10 algarismos (casa dos bilhões), o alto volume de repetições começa a exceder a capacidade
* de processamento rápido da CPU, causando lentidão severa. Para aplicações que exigem validação de números extremamente grandes (como em criptografia),
* seria necessário otimizar o algoritmo para testar apenas até a raiz quadrada do número O(sqrt{N})

## Como o código funciona

O script solicita ao usuário um número natural maior que zero. Em seguida, utiliza um laço de repetição (`for`) para testar a divisão do número escolhido 
por todos os inteiros de 1 até ele mesmo. Se o resto da divisão for zero, o divisor é contabilizado e impresso. Ao final, o programa classifica o número
baseado no total de divisores encontrados.

## Como Executar

O programa foi construído utilizando apenas os recursos nativos do Python, sem necessidade de bibliotecas externas.

1. Certifique-se de ter o **Python 3.x** instalado na sua máquina.
2. Faça o clone deste repositório ou baixe o arquivo `validador_de_numeros_primos.py`.
3. Abra o terminal na pasta onde o arquivo está localizado e execute:

```bash
python validador_de_numeros_primos.py
