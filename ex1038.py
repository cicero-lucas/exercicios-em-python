input=list(map(int,input().split(" ")))

valor=0
cod=input[0]
quant=input[1]

if cod==1:
    valor=(quant*4.00)
elif cod==2:
    valor=(quant*4.50)
elif cod==3:
    valor=(quant*5.00)
elif cod==4:
    valor=(quant*2.00)
elif cod==5:
    valor=(quant*1.50)

print(f'Total: R$ {valor:.2f}')