#questao 1

lista_numero = [1,2,3,4,5,6,7,8,9,10]
qntd_par = 0
qntd_impar = 0

for numero in lista_numero:
    if numero % 2 == 0:
        qntd_par = qntd_par + numero
    else:
        qntd_impar = qntd_impar + numero

print("a soma dos pares de 1 a 10 é: ",qntd_par)
print("a soma dos impares de 1 a 10 é: ",qntd_impar)

#questao 2

palavra = input("digite uma palavra: ").lower()

qntd_vogais = 0
qntd_consoantes = 0
qntd_espaco = 0

for i in palavra:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        qntd_vogais = qntd_vogais + 1
    elif i == " ":
        qntd_espaco += 1
    else:
        qntd_consoantes = qntd_consoantes + 1

print("sua palavra/frase foi: ", palavra)
print("quantidade de vogais: ", qntd_vogais)
print("quantidade de consoantes: ", qntd_consoantes)
print("quantidade de espacos: ", qntd_espaco)

