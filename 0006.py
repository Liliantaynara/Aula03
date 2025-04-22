time1 = input("qual nome do time1: ")
gol1 = int (input("quantos gol fez: "))
time2 = input ("qual nome do time2: ")
gol2 = int (input("quantos gol time2 fez: "))

if gol1 > gol2:
     print(f"time vencedor {time1} {gol1}")
else:
    if gol1 < gol2:
        print (f"venceu {time2} {gol2}")
    else:
        print ("empate")