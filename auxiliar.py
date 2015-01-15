# -*- coding: utf-8 -*-

def nList(n,d):
	out = []
	for i in xrange(0,n):
		out.append(d)
	return out

def nmList(n,m,d):
	out = []
	for i in xrange(0,n):
		out.append([])
		for j in xrange(0,m):
			out[i].append(d)
	return out

def matrixToString(p):
	s = ""
	for i in p:
		for j in i:
			s+=str(j)
		s+="\n"
	return s

def matrixToPrint(p):
	for i in p:
		print i
	print

def printTree(T,s,f=None):
	(r,rl) = T.preencherXY(0, s, 0)
	out = [nList(rl+1," ")]
	verts = [T]
	nexts = []
	i = 0
	while len(verts)!=0:

		v = verts.pop(0)
		if(v.filhos!=None):
			nexts.extend(v.filhos)

		if f==None or f(v)==None:
			out[i][v.x] = 'o'
		else:
			out[i][v.x] = f(v)

		if len(verts)==0 and len(nexts)!=0:
			out.append(nList(rl+1," "))
			i+= 1
			verts = nexts
			nexts = []

	return out

def printTrees(T,s,f=None):
	print matrixToString(printTree(T,s,f))