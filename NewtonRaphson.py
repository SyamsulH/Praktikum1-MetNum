import numpy as np
import matplotlib.pyplot as plt
from math import e #Untuk memanggil bilangan eksponen natural (e)

# Mendefinisikan fungsi
def f(x):
  return e**x-5*x**2

# Mendefinisikan turunan fungsi
def Df(x):
    return e**x-10*x

# Metode Newthon-Rapshon
def newtonRaphson(x0,eps):
    step = 0
    print('\n\n*** ---METODE NEWTON RAPSHON--- ***')
    xn = x0
    for n in range(0,100): #maksimal iterasi adalah 100
        fxn=f(xn)
        if abs(fxn) < eps:
            print('\n Akar Persamaan tersebut : %0.8f' % xn)
            return xn
        Dfxn=Df(xn)
        if Dfxn == 0:
            print('Solusi tidak ditemukan')
            return None
        xn=xn-(fxn/Dfxn)
        step = step + 1
        print('Iterasi-%d, x = %0.8f dan f(x) = %0.8f' % (step, xn, f(xn)))
    print('Iterasi maksimum, solusi tidak ditemukan')

# Sesi Input Nilai Awal yang dikonversi ke pecahan
x0  = float(input('x0: '))
eps = float(input('epsilon : '))
newtonRaphson(x0,eps)