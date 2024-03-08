#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import os
import time
import sys

def printHarryNum(harry,num):
	harry = harry.split("\n")
	num = num.split("\n")
	for l in range(len(harry)):
		print(harry[l], " "*5,num[l] if l < len(num) else "")
	

def usage():
	print(f"Usage:\n{sys.argv[0]} <num_questões>")
	sys.exit(0)

def main():
	numeros = None
	
	if len(sys.argv) < 2:
		usage()
	
	random.seed()
	
	try:
		MAXQ = int(sys.argv[1])
		if MAXQ > 31:
			print("Versão atual suporta até 31.")
			print("Aguarde versão futura.")
			sys.exit(1)
	except ValueError:
		print("Argumento precisa ser um número")
		sys.exit(1)
	
	with open("sorteioQuest.rsc","r") as f:
		numeros = f.read().split("\n\n");
	
	with open("harry.rsc","r") as f:
		harry = f.read();
	
	try:
		while True:	
			input("Sortear")
			os.system("clear")
			for i in range(30):
				os.system("clear")
				printHarryNum(harry,numeros[random.randint(0,MAXQ-1)])
				time.sleep(0.05)
	except KeyboardInterrupt:
		print("\n\nAté a próxima!!!")
		
			

if __name__ == '__main__':
	main()
