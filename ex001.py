print("======"  "DESAFIO 72" "======")
n = ("zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze" , "doze", "treze", "quatore", "quinze", "dezesses", "dezessete", "dezoito", "dezenove", "vinte")
d = int(input("Digite um número entre 0 e 20: "))
while True:
    if d < 0 or d > 20:
        s = int(input("Tente novamente, digite um número entre 0 e 20: "))
        d = s
    else:
        break
ne = n[d]
print("O número que você digitou foi {}".format(ne))
