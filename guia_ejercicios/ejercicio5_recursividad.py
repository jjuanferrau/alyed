def convertir_a_decimal(romano):
    valores_romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if not romano:
        return 0

    primer_caracter = romano[0]
    if len(romano) == 1 or valores_romanos[primer_caracter] >= valores_romanos[romano[1]]:
        return valores_romanos[primer_caracter] + convertir_a_decimal(romano[1:])
    else:
        return -valores_romanos[primer_caracter] + convertir_a_decimal(romano[1:])
