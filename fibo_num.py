#!/usr/bin/env python3

f1=f2=1
num=int(input("fibonaci number? "))

if(num<=2):
	for a in range(0,num,1):
		print(1,end="")
		if(a==(num-1)): 
			print("")
		else: 
			print("," ,end="")
	print("F",num,"=",1)
else:
	print(1,1,sep=',',end=",")	
	for i in range(2,num,1):
		n=f1+f2
		f1=f2
		f2=n
		print(n,end="")
		if(i==(num-1)): 
			print("")
		else: 
			print("," ,end="")	
	print("F",num,"=",n)
