
def dodawanie(x,y):
    sum = int(x) + int(y)
    return sum
def odejmowanie(x,y):
    sum = int(x) - int(y)
    return sum
def mnozenie(x,y):
    sum = int(x) * int(y)
    return sum
def dzielenie(x,y):
    sum = int(x) / int(y)
    return sum

n = input('wprowadz liczbe: ')
n1 = input('wprowadz druga liczbe:')
znak = input('Wprowadz znak(+,-,*,/)')


if znak == "+" :
    print (dodawanie(n,n1))
elif znak == "-" :
    print (odejmowanie(n,n1))
elif znak == "*" :
    print (mnozenie(n,n1))
elif znak == "/" :
    print (dzielenie(n,n1))
else:
    print("Wprowadzono nieprawidłowy znak!") 
