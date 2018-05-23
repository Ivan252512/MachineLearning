def myFibo(n):
    numeroprevio=0
    numeroactual=1
    sumatotal=0
    contador=0
    while numeroactual<=(n+contador):
        if numeroactual%2!=0:
            sumatotal+=numeroactual
            contador+=1
            print(sumatotal)
        temporal=numeroactual
        numeroactual=numeroactual+numeroprevio
        numeroprevio=temporal
    return sumatotal
print(myFibo(100000))
