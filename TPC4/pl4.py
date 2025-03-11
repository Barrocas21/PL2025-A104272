import re
from enum import Enum

class TipoToken(Enum):
    PALAVRA_RESERVADA = "PALAVRA_RESERVADA"
    VARIAVEL = "VARIAVEL"
    URI = "URI"
    LITERAL = "LITERAL"
    SIMBOLO = "SIMBOLO"
    COMENTARIO = "COMENTARIO"
    ESPACO = "ESPACO"

REGRAS_TOKENS = [
    (TipoToken.PALAVRA_RESERVADA, r'\b(SELECT|WHERE|LIMIT)\b', re.IGNORECASE),
    (TipoToken.VARIAVEL, r'\?[a-zA-Z_][a-zA-Z0-9_]*'),
    (TipoToken.URI, r'\b[a-zA-Z0-9]+:[a-zA-Z0-9]+\b'),
    (TipoToken.LITERAL, r'"[^"]*"(@[a-zA-Z]+)?'),
    (TipoToken.SIMBOLO, r'[{}().;]'),
    (TipoToken.COMENTARIO, r'#[^\n]*'),
    (TipoToken.ESPACO, r'\s+', re.MULTILINE),
]

def tokenizar(consulta):
    tokens = []
    indice = 0
    while indice < len(consulta):
        for tipo_token, padrao, *flags in REGRAS_TOKENS:
            opcoes = flags[0] if flags else 0
            correspondencia = re.match(padrao, consulta[indice:], opcoes)
            if correspondencia:
                if tipo_token != TipoToken.ESPACO:  # Ignorar espaços em branco
                    tokens.append((tipo_token, correspondencia.group(0)))
                indice += len(correspondencia.group(0))
                break
        else:
            raise SyntaxError(f"Token inválido próximo de: {consulta[indice:20]}")
    return tokens

# Exemplo de utilização
consulta = """
# DBPedia: obras de Chuck Berry
SELECT ?nome ?desc WHERE {
  ?s a dbo:MusicalArtist.
  ?s foaf:name "Chuck Berry"@en .
  ?w dbo:artist ?s.
  ?w foaf:name ?nome.
  ?w dbo:abstract ?desc
} LIMIT 1000
"""

tokens = tokenizar(consulta)
for token in tokens:
    print(token)
