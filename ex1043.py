input=list(map(float,input().split(" ")))
a=input[0]
b=input[1]
c=input[2]
valor=0

if(a<b+c)and(b<a+c) and(c<b+a):
    valor=a+b+c
    print(f"perimetro {valor:.1f}")
else:
    valor=((a+b)*c)/2
    print(f"Area {valor:.1f}")


