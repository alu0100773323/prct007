#!/usr/bin/python
#!encoding: UTF-8
import modulo

tupla = (10,20,30,40) #la t-upla no se puede modificar es constante

lista = []
for i in tupla:
  valor = modulo.calcular_pi (i)
  lista.append (valor)
print lista

pi35 = []
for i in tupla:
  pi35.append (modulo.PI35)
dif35 = []
for i in range (len (tupla)):#no quiere el valor de la t-upla sino la posición
  dif35.append (abs(pi35[i] - lista[i]))
print "i \tPI35     \tlista i     \tPI35 - lista i"
for i in range (len (tupla)):
  print "%d\t%1.10f\t%1.10f\t%1.10f" % (i+1,pi35[i],lista[i],dif35[i])
  
#nº máximo de valores de la t-upla: depende del hadware que tengamos el número podrá ser mayor o menos
#notación científica: se purede utilizar sin ningún problema
#.pyc: cuando hago un python.py y modulo.py el ejecutable lo combierte en una función .pyc
#forma de medir el tiempo: se hace con una función 'time' que calcula el tiempo inicial y el final y los resta

#Para saber más
print "Pasando la salida a una matriz...."
print "i \tPI35     \tlista i     \tPI35 - lista i", #
matriz = []
for i in range (len (tupla)):
  matriz.append ([i+1, pi35[i], lista[i], dif35[i]])
for i in range (len (tupla)):
  print
  print matriz[i][0],
  for j in range (1,4):
    print "\t%1.10f" % matriz[i][j], #