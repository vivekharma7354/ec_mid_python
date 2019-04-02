from array import *
a=[([0]*3) for i in range(3)]
b=[([0]*3) for i in range(3)]
c=[([0]*3) for i in range(3)]
for i in range(3):
	for j in range(3):
		a[i][j]=int(input())
for i in range(3):
	for j in range(3):
		b[i][j]=int(input())
for i in range(3):
	for j in range(3):
		for k in range(3):
			c[i][j]+=a[i][k]*b[k][j]
for i in range(3):
	for j in range(3):
		print(c[i][j],end=' ')
	print('')
