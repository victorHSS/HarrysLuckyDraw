#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import os
import time
import sys

#
# cria um gerador que retorna cada digito de num
# baseado num tamanho lenq, completando os digitos
# mais à esquerda com zeros
#
def genNumLen(num, lenq):
	nstr = f"{num:0{lenq}d}"
	for sn in nstr:
		yield int(sn)

#
# faz o trabalho de printar o harry e o número lado
# a lado, pegando linha por linha de cada um e printando
#
def printHarryNum(harry, numeros, num, lenq):
	harry = harry.split("\n")
	
	numlst = []
	for numi in genNumLen(num,lenq):
		numlst.append(numeros[numi].split("\n"))
	
	numlst2 = tuple(zip(*numlst))
	
	for l in range(len(harry)):
		print(harry[l], " "*5,"".join(numlst2[l]) if l < len(numlst[0]) else "")
	
#
# função auxiliar que mostra o uso do script
#
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
		LENQ = len(sys.argv[1])
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
				printHarryNum( harry, numeros, random.randint(1, MAXQ), LENQ )
				time.sleep(0.05)
	except KeyboardInterrupt:
		print("\n\nAté a próxima!!!")
		
			

if __name__ == '__main__':
	main()
