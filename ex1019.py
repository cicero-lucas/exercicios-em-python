from math import pow
from math import sqrt
valor=list(map(float,input().split(" ")))

a=valor[0]
b=valor[1]
c=valor[2]

delt=(pow(b,2))-(4*a*c)
if delt>0:
    #tentativa e exceção para não gera erro no codigo
    try:
        x1=((-b)+(sqrt(delt)))/(2*a)
        x2=((-b)-(sqrt(delt)))/(2*a)
        print(f"R1 = {x1:.5f}")
        print(f"R1 = {x2:.5f}")
    except:
        print("Impossivel calcular")
else:
    print("Impossivel calcular")
    

