palindromo = input("Introduce una palabra: ").lower()

palindromo_volteado = palindromo[::-1]

if palindromo == palindromo_volteado:
    print("Es palindromo")
else:
    print("No es palindromo")