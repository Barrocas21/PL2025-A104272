# TPC1 - Somador On/Off

**Data:** [12-02-2025]  
**Autor:** [Miguel Barrocas] [A104272] 
  

## Descrição  

Este projeto consiste na implementação de um **somador inteligente** em Python que processa sequências numéricas dentro de um texto, permitindo ativar ou desativar a soma através dos comandos `"On"` e `"Off"`. Sempre que o caractere `"="` for encontrado, o programa exibe a soma acumulada até o momento.  

## Funcionalidades  

- Soma sequências numéricas contidas no texto.  
- Ativa e desativa a soma com os comandos `"On"` e `"Off"`.  
- Lê dados diretamente do utilizador via `input()`.  
- Apresenta resultados parciais sempre que `"="` aparece na entrada.  


## Estrutura do Código  

### 1. Função `somador_on_off(texto)`

A função principal que implementa a lógica do somador:

- Percorre o texto caractere a caractere usando um **loop `while`**.  
- Mantém estado através das seguintes variáveis:  
  - `soma`: Acumulador da soma atual.  
  - `soma_atual`: Indica se a soma está ativa ou desativada.  
  - `numero_atual`: Armazena o número que está a ser construído.  
- Implementa lógica para:  
  - Detecção dos comandos `"On"` e `"Off"`.  
  - Construção de números através de sequência de dígitos.  
  - Processamento de `"="` para exibir o resultado parcial.  

### 2. Função principal  

- Lê a entrada do utilizador via `input()`.  
- Chama a função `somador_on_off()` para processar os dados.  

## Regras de Processamento  

### Estado Inicial:  
- A soma começa **ativa** por padrão.  
- O acumulador inicia em **zero**.  

### Comandos de Controle:  
- `"Off"`: Desativa a soma temporariamente.  
- `"On"`: Reativa a soma.  
- `"="`: Exibe a soma atual.  

## Conclusão  

O **Somador On/Off** demonstra uma implementação eficiente e funcional para processamento de sequências numéricas controladas por comandos. O programa consegue lidar corretamente com diferentes padrões de entrada, garantindo um **controle preciso sobre o estado da soma** e permitindo exibições parciais dos resultados.  

A estrutura modular do código facilita a **manutenção** e possíveis **expansões futuras**, como o suporte a entrada via ficheiros ou a adição de novas operações matemáticas. Além disso, o tratamento adequado dos comandos `"On"`, `"Off"` e `"="` assegura que o comportamento do somador seja **intuitivo e previsível** para o utilizador.  

Dessa forma, o projeto serve como uma base sólida para aplicações que necessitem de **interpretação e manipulação dinâmica de sequências numéricas**.  


