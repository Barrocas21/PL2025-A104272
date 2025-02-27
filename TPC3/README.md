# TPC3


* **Data**: 26/02/2025
* **Nome**: Miguel Nogueira Barrocas
* **Número**: a104272


## Resumo

O código implementa um conversor de Markdown para HTML com as seguintes funcionalidades:

* **Cabeçalhos**: Converte `#`, `##` e `###` para `<h1>`, `<h2>` e `<h3>` respectivamente
* **Formatação de texto**:
  * **Negrito**: Converte texto entre `**` para `<b>`
  * **Itálico**: Converte texto entre `*` para `<i>`
* **Links**: Converte `[texto](url)` para `<a href="url">texto</a>`
* **Imagens**: Converte `![alt](url)` para `<img src="url" alt="alt"/>`
* **Listas numeradas**: Converte linhas que começam com números (ex: `1. Item`) para listas HTML `<ol><li>Item</li></ol>`



### Pontos Fortes

1. **Uso eficiente de expressões regulares** para identificar e substituir padrões
2. **Código conciso** que realiza várias transformações em poucas linhas
3. **Abordagem sequencial** que facilita a manutenção e expansão
4. **Função auxiliar** bem implementada para lidar com listas numeradas


## Exemplos de Uso

### Entrada Markdown:

```markdown
# Título Principal

## Subtítulo

Este é um texto com **negrito** e *itálico*.

1. Primeiro item
2. Segundo item
3. Terceiro item

[Link para Google](https://www.google.com)

![Imagem de exemplo](https://example.com/image.jpg)
```

### Saída HTML Esperada:

```html
<h1>Título Principal</h1>

<h2>Subtítulo</h2>

Este é um texto com <b>negrito</b> e <i>itálico</i>.

<ol><li>Primeiro item</li><li>Segundo item</li><li>Terceiro item</li></ol>

<a href="https://www.google.com">Link para Google</a>

<img src="https://example.com/image.jpg" alt="Imagem de exemplo"/>
```

## Conclusão

O código apresenta uma implementação básica mas funcional de um conversor de Markdown para HTML. Para uso em produção, seria recomendável expandir as funcionalidades e melhorar a robustez do código. Alternativas como as bibliotecas `markdown`, `commonmark` ou `mistune` oferecem implementações mais completas e testadas para uso em ambientes de produção.
