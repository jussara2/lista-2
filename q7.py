n1=float(input("digite um numero:"))
n2=float(input("digite outro numero:"))
n3=float(input("digite mais um numero:"))
if n1 > n2 and n1 > n3:
    print(f"{n1}foi o maior numero")
elif n2 > n1 and n2 > n3 :
    print(f"{n2}foi o maior numero")
else:
    print(f"{n3}foi o maior numero")

if n1 < n2 and n1 < n3:
    print(f"{n1}foi o menor numero")
elif n2 < n1 and n2 < n3 :
    print(f"{n2}foi o menor numero")
else:
    print(f"{n3}foi o menor numero")
 
