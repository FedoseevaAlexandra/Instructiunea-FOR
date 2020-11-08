'''
Să se calculeze sumele: 	s1=1+2+3+…+n
			s2=1*2+2*3+3*4+…+(n-1)*n
			s3=1+1*2+1*2*3+…+1*2*3*…*n
			s4=12+22+32+…+n2
			s5=1/2+2/3+3/4+…+n/(n+1)
			s6=1+2+22+23+24+…+2n
			Notă: Pentru fiecare sumă n – se va citi de la tastatură.
'''
n=int(input('dati nr: '))
s1=0
s2=0
s3=0
s4=0
s5=0
s6=3
for nr1 in range(1,n+1):
    s1+=nr1
print('suma=',s1)
n=int(input('dati al doilea nr: '))
for nr2 in range(1,n+1):
    s2+=(nr2-1)*nr2
print('suma2=', s2)
n=int(input('dati al treilea nr: '))
for nr3 in range(1,n+1):
    x=nr3
    while (nr3-1)>0:
        x*=nr3-1
        nr3-=1
    s3+=x
print('suma3=',s3)
n=int(input('dati al patrulea nr: '))
for nr4 in range(1,n+1):
    s4+=nr4*10+2
print('suma4=',s4)
n=int(input('dati al cincilea nr: '))
for nr5 in range(1,n+1):
    s5+=nr5/(nr5+1)
print('suma5=',s5)
n=int(input('dati al saselea nr: '))
for nr6 in range(2,n+1):
    s6+=20+nr6
print('suma6=',s6)

    
