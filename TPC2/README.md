# TPC2

**Data:** 20/02/2025  
**Nome:** Miguel Nogueira Barrocas  
**Número:** a104272

---

## Resumo  

Este trabalho analisa um dataset de obras musicais, extraindo informações relevantes como compositores, períodos e obras. O código implementado processa um ficheiro CSV sem utilizar bibliotecas específicas para manipulação de CSV, garantindo uma solução personalizada.  

A implementação inclui três funcionalidades principais:  
1. Listar de forma ordenada os compositores musicais.  
2. Contagem das obras por período.  
3. Dicionário que associa períodos a listas de títulos das obras.  

O código recebe o ficheiro como entrada, realiza o parsing manual do CSV e processa os dados para obter as informações desejadas.

---

## Leitura e processamento do CSV  

O código utiliza a função `parse_csv` para converter um ficheiro CSV numa lista de listas. Devido à possibilidade de campos com aspas (`"..."`), a função lida com separação correta dos campos ignorando `;` dentro de aspas.  

## Funcionalidades Implementadas  

O programa apresenta um menu interativo permitindo ao utilizador escolher entre três opções:  

- **Opção 1:** Lista ordenada alfabeticamente dos compositores musicais.  
- **Opção 2:** Distribuição das obras por período.  
- **Opção 3:** Dicionário com obras organizadas por período.  

Consoante a escolha do utilizador, os dados são apresentados corretamente.  

---

## Resultados  

Os seguintes resultados foram obtidos ao executar o programa com um ficheiro de teste:  

### 4.1. Lista ordenada dos compositores  

```bash
$ python3 tpc2.py obras.csv
Escolha uma opção:
1. Lista ordenada alfabeticamente dos compositores musicais
2. Distribuição das obras por período
3. Dicionário com obras organizadas por período
Opção (1-3): 1

Compositores musicais (Ordem alfabética):
Alessandro Stradella
Antonio Maria Abbatini
Bach, Johann Christoph

```

## 5. Conclusão  

A análise do dataset foi realizada com sucesso, permitindo a extração correta das informações solicitadas. O parsing manual do CSV demonstrou-se eficiente, garantindo um tratamento adequado de aspas e delimitadores.  


