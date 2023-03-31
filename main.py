# Para chegar no tamanho da tabela hash eu contei a quantidade de ids(6) e multiplequei por 2 que dá 12, após isso aproximei o resultado para o número primo mais próximo que é o 11, esse 11 será o tamanho da minha tabela hash(levando em conta que começa de 0 )
TAM = 11
indices = []

# como só tem 6 termos, coloquei num range de 6
for i in range(6):
    # Aqui pegarei somente as partes numéricas dos ids
    valor = int(input("Digite o valor: "))
    resto = valor % TAM
    indices.append(resto)

print(f"Os valores encontrados por meio da fução hash, mostraram os seguintes indices: {indices}")

