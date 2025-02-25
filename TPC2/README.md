# Relatório - Análise de Dataset de Obras Musicais

## Introdução

Este projeto consiste na análise de um dataset de obras musicais a partir de um ficheiro CSV, sem o uso do módulo `csv` do Python. O objetivo é processar os dados e fornecer três tipos de saída:

1. Lista ordenada alfabeticamente dos compositores musicais.
2. Distribuição das obras por período (quantidade de obras em cada período).
3. Dicionário que associa períodos a listas ordenadas de títulos das obras.

O programa recebe o nome do ficheiro CSV como argumento ou usa o padrão `obras.csv`.

---

## Implementação

O código é estruturado em três funções principais:

### `parse_csv(content)`

**Objetivo**:  
Processar o conteúdo do CSV e convertê-lo para uma estrutura de dados utilizável.

**Método**:  
- Lê o conteúdo do ficheiro linha por linha.
- Separa corretamente os campos, considerando a presença de aspas (`"`).
- Retorna os dados como uma lista de listas, ignorando o cabeçalho.

