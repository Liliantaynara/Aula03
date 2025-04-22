n1 = float (input( "digite nota 1: "))
n2 = float (input("Digite nota 2: "))
n3 = float (input("diigite nota3: "))

media = ( n1 + n2 + n3)/3

if media >= 7:
    print(f"aprovado {media}")

else:
    if media <=4:
        print(f"recuperacao{media}")
    else:
        print(f"vc foi reprovado {media}")
