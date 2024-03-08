#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-

import random
import os
import time

def printHarryNum(harry,num):
	harry = harry.split("\n")
	num = num.split("\n")
	for l in range(len(harry)):
		print(harry[l], " "*5,num[l] if l < len(num) else "")
	

def main():
	numeros = None
	MAXQ = 31
	
	with open("sorteioQuest.rsc","r") as f:
		numeros = f.read().split("\n\n");
	
	with open("harry.rsc","r") as f:
		harry = f.read();
	
	while True:	
		input("Sortear")
		os.system("clear")
		for i in range(30):
			os.system("clear")
			printHarryNum(harry,numeros[random.randint(0,MAXQ-1)])
			time.sleep(0.05)
		
			

if __name__ == '__main__':
	main()
