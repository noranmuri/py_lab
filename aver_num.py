#!/usr/bin/env python3

sum=0
n = int(input("Enter the number size : "))

for i in range(0,n,1):
	num=int(input("Input the number: "))
	sum+=num

result=sum/n
print("The average is : ",result)
