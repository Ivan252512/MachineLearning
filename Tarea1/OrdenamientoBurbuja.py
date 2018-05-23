#Ordenamiento burbuja
def OrdenamientoBurbuja(x):
	veces=0
	while veces<len(x):
		i=0
		while i<(len(x)-1):
			if x[i]>x[i+1]:
				intercambio1=x[i]
				intercambio2=x[i+1]
				x[i]=intercambio2
				x[i+1]=intercambio1
			i+=1
		veces+=1
	return x


lista= [1,1,4,23,6,3,35,65,5,123,121,91,92,29,12]

print(OrdenamientoBurbuja(lista))
