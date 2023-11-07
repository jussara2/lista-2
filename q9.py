amor=float(input("digite um numero: "))
vida=float(input('digite outro numero:'))
paixão=float(input("digite mais um numero: "))
if amor > vida > paixão:
    print(amor,vida,paixão)
elif amor > paixão >vida:
    print(amor,paixão,vida)
elif vida > amor >paixão:
    print(vida,amor,paixão)
elif vida > paixão >amor:
    print(vida,paixão,amor)
elif paixão > amor >vida:
    print(paixão,amor,vida)
else:
    print(paixão,vida,amor)
