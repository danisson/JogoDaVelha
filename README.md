JogoDaVelha
===========
Uma tentativa de jogador de jogo da velha (tic-tac-toe) em Python.
Atualmente ele está bem lerdo. Para usar, basta importar criar um VelhaNode
recebendo uma matrix (do NumPy) 3x3 ternária e um booleano para saber se é a vez do primeiro
jogador.
Agora você tem um nó da árvore deste jogo, agora basta computar o resto da árvore em largura
ou seja `nó.largura(lambda v,i: v.computarFilhos())` e ele está pronto para jogar cada turno
retornando o próximo estado: `jogarUmTurno(nó, bool)`. O restorno será `None` se o jogo acabou.  

Além disso foi feito um código para imprimir na saída final uma espécie de gráfico da árvore,
por exemplo, uma árvóre binária com 3 nós é representadada assim:
```
 o
o o
```
