# -*- coding: utf-8 -*-
from arvore import Arvore
import copy
import auxiliar as aux
import numpy as np

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
			return;
		if self.jogador:
			peca = 1
		else:
			peca = 2
		if self.fimDeJogo():
			return;
		t = self.valor.copy(order='C')
		for i in xrange(0,3):
			for j in xrange(0,3):
				if t[i,j]==0:
					t[i,j] = peca
					self.addFilho(VelhaNode(t,not self.jogador))
					# aux.matrixToPrint(t)
					t = copy.deepcopy(self.valor)

	def fimDeJogo(self):
		pecas = [0,0]
		t = self.valor

		pecas[0] = 1
		pecas[1] = 2

		for x in xrange(0,2):
			for i in xrange(0,3):
					if t[i,0]==pecas[x] and t[i,1]==pecas[x] and t[i,2]==pecas[x]:
						self.label = x+1
						return True

		for x in xrange(0,2):
			for i in xrange(0,3):
					if t[0,i]==pecas[x] and t[1,i]==pecas[x] and t[2,i]==pecas[x]:
						self.label = x+1
						return True

		for x in xrange(0,2):
			if t[0,0]==pecas[x] and t[1,1]==pecas[x] and t[2,2]==pecas[x]:
				self.label = x+1
				return True

		for x in xrange(0,2):
			if t[0,2]==pecas[x] and t[1,1]==pecas[x] and t[2,0]==pecas[x]:
				self.label = x+1
				return True

		b = True
		for i in xrange(0,3):
			for j in xrange(0,3):
					b = b and t[i,j]!=0
		if b==True:
			self.label = "x"
			return b

		return False