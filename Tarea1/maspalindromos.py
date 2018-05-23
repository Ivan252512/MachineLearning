#Funcion que regresa la palabra rotada tantas posiciones.
def rot(x,pos):
    x_n=str(x)
    #Consiste en copiar varias veces la palabra y regresar la posicion.
    for i in range(int(pos/len(str(x)))+1):
        x_n+=str(x)
    return int(x_n[pos:pos+len(str(x))])


def palindromo(x):
    x=str(x)
    for i in range(len(str(x))):
        if (x[i]!=x[len(x)-i-1]):
            return False
    return True

def erre(x):
    r=x
    x_n=str(x)
    for i in range(len(x_n)-1):
        r=r+(-i)**2*rot(x,int(x_n[i]))
    return r

def esturbopalindromos(x):
    r=erre(x)
    if palindromo(r):
        return True
    else:
        return False

def cuantostbpalindromos(inicial,final):
    contador=0
    for i in range(inicial,final):
        if esturbopalindromos(i):
            contador+=1
    return contador

print(cuantostbpalindromos(1,200000))
