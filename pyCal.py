def add(a,b):
	return a+b

def sub(a,b):
	return a-b

def mult(a,b):
	return a*b

def divide(a,b):
	return a//b

a =  int(input())
b=int(input())
cond = int(input())

if (cond==1):
	prinnt(add(a,b))
elif(cond==2):
	print(sub(a,b))
elif(cond==3):
	print(mult(a,b))
elif(cond==4):
	print(divide(a,b))
