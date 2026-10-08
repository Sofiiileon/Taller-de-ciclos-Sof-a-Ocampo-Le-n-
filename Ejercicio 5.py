print('ingrese un año')
a1=input()
if a1%4==0 or a1%400==0:
    print(f'El año {a1} es bisiesto')
elif a1%100!=0:
    print(f'El año {a1} no es bisisesto')


