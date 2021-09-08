# Junção por Intercalação - Algoritmo Modificado
# Autor - Jean Pierre Cordeiro Aboumrad
import time


def current_milli_time():
    return round(time.time() * 1000)


# Vetores de Teste
r = [x for x in range(1, 100000)]
s = [1, 1, 2, 3, 5, 5, 5, 12, 15, 18, 18, 26, 26, 123, 123]
p3 = []

tamanho_s = len(s) - 1
start_time = current_milli_time()

comeco_r = 1
comeco_s = 0
for i in range(len(r)):
    repeticao = 0
    aux = r[i]
    for j in range(comeco_r, len(r)):
        if r[j] == r[i]:
            repeticao += 1
            aux = r[j]

        elif r[j] > r[i]:
            # print('Break')
            break

    i = j
    comeco_r = i + 1

    while s[comeco_s] <= aux and comeco_s < tamanho_s:
        comeco_s += 1

    if s[comeco_s - 1] == aux:
        print(f's[comeco_s] = {s[comeco_s]}\naux = {aux}')
        print('OK!')
        p3.append(aux)

print(p3)

end_time = current_milli_time()
delta = end_time - start_time
print(f'Tempo de Execução Total 1: {delta}')