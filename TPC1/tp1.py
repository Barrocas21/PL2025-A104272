
def somador_on_off(texto):
    soma = 0  # Armazena a soma dos números (começa no 0)
    soma_atual = True  # Indica se devemos somar os números ou não
    numero_atual = ""  # Armazena o número atual que está a ser lido

    i = 0
    while i < len(texto):
        char = texto[i]
        
        # Se o caractere for um dígito, acumula no número atual
        if char.isdigit():
            numero_atual += char #Se for um numero adiciona à variavel numero_atual
        else:
            #Caso o char não seja um número
            if numero_atual and soma_atual: #Se o numero_atual não for vazio e a soma estiver ligada
                soma += int(numero_atual) #Adiciona o numero_atual à soma
            numero_atual = ""  # Reseta o número atual

            #Para os caracteres como "=", "Off" e "On"
            if char == "=":  # Se encontrar "=", imprime a soma
                print("Soma atual:", soma)
            elif texto[i:i+3].lower() == "off":  # Se encontrar "Off", desliga a soma
                soma_atual = False
                i += 2  
            elif texto[i:i+2].lower() == "on":  # Se encontrar "On", liga a soma
                soma_atual = True
                i += 1  

        i += 1  # Avança para o próximo caractere

# Exemplo de uso

texto = input("Digite o texto: ") 
somador_on_off(texto)  
        

    
