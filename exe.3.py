A=float(input("Digite o valor do lado A: "))
B=float(input("Digite o valor do lado B: "))
C=float(input("Digite o valor do lado C: "))
if A<B+C and B<A+C and C<A+B:
    if A==B and B==C:
        print("É um triângulo equilátero.")
    elif A!=B and B!=C:
        print("É um triângulo escaleno.")
    elif A==B or A==C or B==C:
        print("É um triângulo isósceles.")
else:
    print("Não é um triângulo.")