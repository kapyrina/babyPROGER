""" пример вычисления1*2*3*4*5*6 = 720 """""


def factorialnum(n):

  if n== 1:

    return 1

  else:
    return(n * factorialnum(n-1))

number =7
print("Факториал числа", number, "равно",factorialnum(number))