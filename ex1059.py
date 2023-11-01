#par ou impar
l_par=[]
l_impar=[]
nun=int(input())
for c in range(nun):
    n=int(input())
    if n%2==0:
        l_par.append(n)
    elif n%2!=0:
        l_impar.append(n)

l_par.sort() 
for p in l_par:
    print(p)
l_impar.sort()
l_impar.reverse()
for i in l_impar:
    print(i)