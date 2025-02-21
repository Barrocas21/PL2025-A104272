import sys

# Índices das colunas no CSV
INDICE_COMPOSITOR = 4
INDICE_PERIODO = 3
INDICE_OBRA = 0

def parse_csv(content):
    """Converte um CSV em uma lista de listas, separando corretamente os campos."""
    rows = []
    current_row = []
    field = []
    inside_quotes = False
    
    for char in content:
        if char == '"':
            inside_quotes = not inside_quotes  # Alterna entre dentro e fora das aspas
        elif char == '\n' and not inside_quotes:
            current_row.append(''.join(field).strip())
            rows.append(current_row)
            current_row = []
            field = []
        elif char == ';' and not inside_quotes:
            current_row.append(''.join(field).strip())
            field = []
        else:
            field.append(char)
    
    if field:
        current_row.append(''.join(field).strip())
    if current_row:
        rows.append(current_row)
    
    return rows[1:]  # Ignora o cabeçalho

def process_data(linhas):
    """Processa os dados do CSV e retorna as estruturas necessárias."""
    compositores = set()
    obras_por_periodo = {}
    obras_por_compositor = {}

    for linha in linhas:
        if len(linha) <= max(INDICE_COMPOSITOR, INDICE_PERIODO, INDICE_OBRA):
            continue  # Ignorar linhas inválidas

        compositor = linha[INDICE_COMPOSITOR].strip()
        periodo = linha[INDICE_PERIODO].strip()
        obra = linha[INDICE_OBRA].strip()

        # Guardar compositor
        if compositor:
            compositores.add(compositor)

        # Contabilizar obras por período
        if periodo:
            obras_por_periodo.setdefault(periodo, []).append(obra)

    return sorted(compositores), obras_por_periodo

def main():
    file_path = sys.argv[1] if len(sys.argv) > 1 else "obras.csv"

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Erro: Ficheiro '{file_path}' não encontrado.")
        sys.exit(1)

    linhas = parse_csv(content)
    compositores, obras_por_periodo = process_data(linhas)

    opcao = input(
        "Escolha uma opção:\n"
        "1. Lista ordenada alfabeticamente dos compositores musicais\n"
        "2. Distribuição das obras por período\n"
        "3. Dicionário com obras organizadas por período\n"
        "Opção (1-3): "
    )

    if opcao == "1":
        print("\nCompositores musicais (Ordem alfabética):")
        print("\n".join(compositores))

    elif opcao == "2":
        print("\nNúmero de obras por período:")
        for periodo, obras in sorted(obras_por_periodo.items()):
            print(f"{periodo}: {len(obras)} obras")

    elif opcao == "3":
        print("\nLista de obras por período (Ordenadas alfabeticamente):")
        for periodo, obras in sorted(obras_por_periodo.items()):
            print(f"{periodo}:")
            for obra in sorted(obras):
                print(f"  - {obra}")

    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()
