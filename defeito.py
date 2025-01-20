palavras_corretas = []
for i in range(int(input())):
    defeito = input()
    palavra_correta = ""
    
    i = 0
    while i < len(defeito):
        char = defeito[i]

        if char in ["1", "3", "9"]:
            codigo = char + defeito[i + 1]
            i += 2
            if char == "1":
                codigo += defeito[i]
                i += 1

            palavra_correta += chr(int(codigo))
        else:
            palavra_correta += char
            i += 1
    
    palavras_corretas.append(palavra_correta)

for palavra in palavras_corretas:
    print(palavra)