#!/usr/bin/python
#!encoding: UTF-8
import sys
import math

PI35 = 3.1415926535897931159979634685441852 #se declara como variable global

#Función
def calcular_pi (n):
  ini = 0
  intervalos = 1.0 / float (n)
  sumatorio = 0.0
  for i in range(n):
    #x_i = calcular_xi (n, i+1)
    x_i = ((i+1) - 1.0/2.0) / n
    fx_i = 4.0 / (1.0 + x_i * x_i)
    ini += intervalos
    sumatorio += fx_i
  valor_pi = sumatorio / n
  return (valor_pi)
  
#Programa principal
if (__name__ == "__main__"):
  argumentos = sys.argv[1:] #[1:] que empiece a visualizar desde la posición 1 hasta el final
  if (len(argumentos) == 2):
    n = int (argumentos[0])
    aproximaciones = int (argumentos[1])
  else:
    print "Introduzca el nº de intervalos (n>0):"
    n = int (raw_input())
    print "Introduzca el nº de aproximaciones:"
    aproximaciones = int (raw_input())
  if (n>0):
    intervalo = n
    lista = []
    for i in range (aproximaciones):
      valor = calcular_pi (intervalo)
      lista.append (valor)
      intervalo += n
    print lista
    diferencia = []
    for i in range (aproximaciones):
      dif = abs (PI35 - lista[i])
      diferencia.append (dif)
    print "i \tPI35     \tlista i     \tPI35 - lista i"
    for i in range (aproximaciones):
      print "%d\t%1.10f\t%1.10f\t%1.10f" % (i+1,PI35,lista[i],diferencia[i])
  else:
    print "El valor de los intervalos debe ser mayor de 0"