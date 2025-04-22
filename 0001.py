h1 = int ( input("digite horas: "))
m1 = int ( input("digite os minutos: "))
h2 = int ( input("digite novamente horas: "))
m2 = int( input("digite novamente horas: "))

totalh1 = 12
totalmin = 60

if h1 > 12:
    h2 -= 12

    m1 > 60
    m2 -= 60

    totalh1 = h1 + m2
    totalmin = m1 + m2

if totalmin >= 60 :
    totalh1 += totalmin // 60
    totalmin = totalh1 % 60

print(f"horario {totalh1}H e {totalmin}Min definida")