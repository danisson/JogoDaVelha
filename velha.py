# -*- coding: utf-8 -*-
from arvore import Arvore
import copy
import auxiliar as aux
import numpy as np

class Tab(object):
	"""Interface que descreve um tabuleiro"""
	def __init__(self):
		raise NotImplementedError('Classe Abstrata')
	def __getitem__(self,key):
		raise NotImplementedError('Classe Abstrata')
	def __setitem__(self,key,value):
		raise NotImplementedError('Classe Abstrata')
	def __str__(self):
		raise NotImplementedError('Classe Abstrata')
	def calcularProximos(self):
		raise NotImplementedError('Classe Abstrata')
	def fimDeJogo(self):
		pecas = [1,2]

		for x in xrange(0,2):
			for i in xrange(0,3):
					if self[3*i+0]==pecas[x] and self[3*i+1]==pecas[x] and self[3*i+2]==pecas[x]:
						return x+1

		for x in xrange(0,2):
			for i in xrange(0,3):
					if self[3*0+i]==pecas[x] and self[3*1+i]==pecas[x] and self[3*2+i]==pecas[x]:
						return x+1

		for x in xrange(0,2):
			if self[3*0+0]==pecas[x] and self[3*1+1]==pecas[x] and self[3*2+2]==pecas[x]:
				return x+1

		for x in xrange(0,2):
			if self[3*0+2]==pecas[x] and self[3*1+1]==pecas[x] and self[3*2+0]==pecas[x]:
				return x+1

		b = True
		for i in xrange(0,3):
			for j in xrange(0,3):
					b = b and self[3*i+j]!=0
		if b==True:
			return 3

		return 0

class TabNumpy(Tab):
	"""Tabuleiro com arrays do Numpy"""
	def __init__(self):
		self.tab = np.array([0,0,0,0,0,0,0,0,0])
	def __getitem__(self,key):
		return self.tab[key]
	def __setitem__(self,key,value):
		self.tab[key] = value
	def __str__(self):
		r = ""
		for i in xrange(0,3):
			r+="[{},{},{}]".format(self.tab[3*i],self.tab[3*i+1],self.tab[3*i+2])
			if i<2:
				r+="\n"
		return r

	def calcularProximos(self,jogador):
		if jogador:
			peca = 1
		else:
			peca = 2
		if self.fimDeJogo():
			return;

		retorno = []
		t = copy.deepcopy(self)
		for i in xrange(0,3):
			for j in xrange(0,3):
				if t[3*i+j]==0:
					t[3*i+j] = peca
					retorno.append(t)
					t = copy.deepcopy(self)
		return retorno;

class VelhaNode(Arvore):
	"""Representa um nó de um jogo da velha"""
	def __init__(self, tabuleiro, jogador):
		super(VelhaNode, self).__init__()
		self.valor = tabuleiro
		self.jogador = jogador
		if jogador:
			self.label = 'u'
		else:
			self.label = 'd'

	def computarFilhos(self):
		""" Computa os jogos possiveis """
		if self.filhos != None:
			return
		proxs = self.valor.calcularProximos(self.jogador)
		if proxs is not None:
			for t in self.valor.calcularProximos(self.jogador):
				self.addFilho(VelhaNode(t,not self.jogador))

	def fimDeJogo(self):
		return self.valor.fimDeJogo()!=0