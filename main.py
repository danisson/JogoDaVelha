#!/usr/bin/python
# -*- coding: utf-8 -*-

from arvore import Arvore
import auxiliar as aux
import velha as v
import numpy as np
from numpy import matrix

def ratio(t,jogador,prof=1):
	if t.filhos != None:
		aux = 0
		for i in t.filhos:
			aux += ratio(i, jogador,prof+1)
		return aux/len(t.filhos)

	if jogador:
		peca = 1
	else:
		peca = 2

	if t.label == peca:
		return -2*(1.0/prof)
	elif t.label == 'x':
		return -1*(1.0/prof)
	else:
		return 1*(1.0/prof)


def jogarUmTurno(t,jogador):
	if t.jogador != jogador or t.fimDeJogo():
		return None

	a = np.zeros(len(t.filhos))
	for i in xrange(0,len(t.filhos)):
		a[i]=ratio(t.filhos[i],jogador)

	return t.filhos[np.argmin(a)]

def main():
	t = v.TabNumpy()
	b = True

	# print t.fimDeJogo()!=0
	# print t.calcularProximos(True)
	# t[0] = 1;t[2]=2;t[3]=1;t[4]=1;t[6]=2;
	# b = False
	# print type(t)

	jogo = v.VelhaNode(t,b)

	print "Loading"
	jogo.largura(lambda v,i: v.computarFilhos())
	print "Done\n"

	while True:
		jogo = jogarUmTurno(jogo, b)
		if jogo is None:
			break

		print jogo.valor,"\n"
		b = not b

if __name__ == '__main__': main()