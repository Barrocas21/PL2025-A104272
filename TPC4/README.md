# TPC4

**Data**: 9 de Março de 2025  
**Autor**  
Nome: Miguel Nogueira Barrocas
Número: 104272 

## Introdução
Este documento descreve a implementação de um analisador léxico para uma linguagem de consulta semelhante a SPARQL. O programa identifica diferentes elementos da linguagem utilizando expressões regulares e classifica os tokens em categorias predefinidas.

## Objetivo
O objetivo do analisador léxico é processar uma string contendo uma consulta e dividir seu conteúdo em tokens, classificando-os em categorias como palavras reservadas, variáveis, URIs, literais, símbolos, espaços em branco e comentários.

## Implementação
A implementação do analisador léxico foi realizada em Python, utilizando a biblioteca `re` para manipular expressões regulares. A classificação dos tokens é feita com base em `TipoToken`, que define os diferentes tipos de tokens reconhecidos pelo analisador.

## Definição dos Tokens

* **PALAVRA_RESERVADA**: `SELECT`, `WHERE`, `LIMIT` (ignorando diferença entre maiúsculas e minúsculas).
* **VARIAVEL**: Identificadores que começam com `?`.
* **URI**: Prefixo seguido de `:` e um identificador.
* **LITERAL**: Sequências entre aspas duplas, podendo ter uma etiqueta de idioma opcional.
* **SIMBOLO**: Caracteres especiais como `{}`, `()`, `.` e `;`.
* **COMENTARIO**: Linhas iniciadas por `#`.
* **ESPACO**: Espaços e quebras de linha (ignorados pelo analisador).

## Método de Tokenização
A função `tokenizar(consulta)` percorre a string da consulta e, a cada iteração:
1. Testa cada padrão de expressão regular.
2. Se houver correspondência, adiciona o token à lista, exceto espaços.
3. Avança no texto de acordo com o comprimento do token identificado.
4. Se nenhum padrão for reconhecido, emite um erro de sintaxe.


##Exemplos de utilização
# DBPedia: obras de Chuck Berry
SELECT ?nome ?desc WHERE {
  ?s a dbo:MusicalArtist.
  ?s foaf:name "Chuck Berry"@en .
  ?w dbo:artist ?s.
  ?w foaf:name ?nome.
  ?w dbo:abstract ?desc
} LIMIT 1000

##Saída
(COMENTARIO, '# DBPedia: obras de Chuck Berry')
(PALAVRA_RESERVADA, 'SELECT')
(VARIAVEL, '?nome')
(VARIAVEL, '?desc')
(PALAVRA_RESERVADA, 'WHERE')
(SIMBOLO, '{')
(VARIAVEL, '?s')
(PALAVRA_RESERVADA, 'a')
(URI, 'dbo:MusicalArtist')
(SIMBOLO, '.')
(URI, 'foaf:name')
(LITERAL, '"Chuck Berry"@en')
(SIMBOLO, '.')
(URI, 'dbo:artist')
(VARIAVEL, '?s')
(SIMBOLO, '.')
(URI, 'foaf:name')
(VARIAVEL, '?nome')
(SIMBOLO, '.')
(URI, 'dbo:abstract')
(VARIAVEL, '?desc')
(SIMBOLO, '}')
(PALAVRA_RESERVADA, 'LIMIT')
(NUMERO, '1000')


