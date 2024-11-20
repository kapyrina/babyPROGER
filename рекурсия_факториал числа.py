""" пример вычисления для числа 6. 1*2*3*4*5*6 = 720 """""
""" в коде рекрусия числа 7. """""

def factorialnum(n):

  if n== 1:

    return 1

  else:
    return(n * factorialnum(n-1))

number =7
print("Факториал числа", number, ":",factorialnum(number))
