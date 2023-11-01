notas=[100, 50, 20, 10, 5, 2]
moedas=[1, 0.50, 0.25, 0.10, 0.05 , 0.01]
c=1
m=1
salario=float(input())
cem=cinq=vint=dez=cinco=dois=0
um=cinq_cent=dez_cent=cinco_cent=um_cent=vint_cinco=0

if(salario>=2):
        while salario!=1:
            if c==1:
                if salario<100:
                    c=2
                else:
                    salario-=100
                    cem+=1
                
            elif c ==2:
                if salario<50:
                    c=3
                else:
                    salario-=50
                    cinq+=1
                
            elif c ==3:
                
                if salario<20:
                    c=4
                else:
                    salario-=20
                    vint+=1
            elif c ==4:
               
                if salario<10:
                    c=5
                else:
                    salario-=10
                    dez+=1
            elif c ==5:
                if salario<5:
                    c=6
                else:
                    salario-=5
                    cinco+=1
            elif c==6:
                if salario<2:
                    pass
                else:
                    salario-=2
                    dois+=1
else:
    while salario!=0:
        if m==1:
            if salario<1:
                m=2
            else:
                salario-=1
                um+=1
                
        elif m ==2:
            if salario<0.50:
                m=3
            else:
                salario-=0.50
                cinq_cent+=1
        elif m ==3:
            if salario<0.25:
                m=4
            else:
                salario-=0.25
                vint_cinco+=1
            
        elif m==4:
            if salario<0.10:
                m=5
            else:
                salario-=0.10
                dez_cent+=1
        elif m ==5:
            if salario<0.05:
                c=6
            else:
                salario-=0.05
                cinco_cent+=1
        elif m == 6:
            if salario<0.01:
                break
            else:
                salario-=0.01
                um_cent+=1

print(cem,"cem")
print(cinq ,"50")
print(vint,"vint")
print(dez ,"dez")
print(cinco,"cinco")
print(dois ,"dois")

print(um,"um")
print(cinq_cent)
print(vint_cinco,"25")
print(dez_cent,"10")
print(cinco_cent,"5")
print(um_cent,"1")
            


