# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 21:41:12 2018

@author: camilo
"""

import math

c0=1
c1=0
c2=-0.5
c3=0
c4=0.0416666

n0=0
n1=0.00001
n2=0.0001
n3=0.0001
n4=0.001
n5=0.01
n6=0.1
n7=1
n8=10

ap1=c0
ap2=c0+c1*n0
ap3=c0+c1*n0+c2*(n0**2)
ap4=c0+c1*n0+c2*(n0**2)+c3*(n0**2)
ap5=c0+c1*n0+c2*(n0**2)+c3*(n0**2)+c4*(n0**2)

apr1=c0
apr2=c0+c1*n1
apr3=c0+c1*n1+c2*(n1**2)
apr4=c0+c1*n1+c2*(n1**2)+c3*(n1**2)
apr5=c0+c1*n1+c2*(n1**2)+c3*(n1**2)+c4*(n1**2)

apro1=c0
apro2=c0+c1*n2
apro3=c0+c1*n2+c2*(n2**2)
apro4=c0+c1*n2+c2*(n2**2)+c3*(n2**2)
apro5=c0+c1*n2+c2*(n2**2)+c3*(n2**2)+c4*(n2**2)

aprox1=c0
aprox2=c0+c1*n3
aprox3=c0+c1*n3+c2*(n3**2)
aprox4=c0+c1*n3+c2*(n3**2)+c3*(n3**2)
aprox5=c0+c1*n3+c2*(n3**2)+c3*(n3**2)+c4*(n3**2)

aproxi1=c0
aproxi2=c0+c1*n4
aproxi3=c0+c1*n4+c2*(n4**2)
aproxi4=c0+c1*n4+c2*(n4**2)+c3*(n4**2)
aproxi5=c0+c1*n4+c2*(n4**2)+c3*(n4**2)+c4*(n4**2)

aproxim1=c0
aproxim2=c0+c1*n5
aproxim3=c0+c1*n5+c2*(n5**2)
aproxim4=c0+c1*n5+c2*(n5**2)+c3*(n5**2)
aproxim5=c0+c1*n5+c2*(n5**2)+c3*(n5**2)+c4*(n5**2)

aproxima1=c0
aproxima2=c0+c1*n6
aproxima3=c0+c1*n6+c2*(n6**2)
aproxima4=c0+c1*n6+c2*(n6**2)+c3*(n6**2)
aproxima5=c0+c1*n6+c2*(n6**2)+c3*(n6**2)+c4*(n6**2)

aprox01=c0
aprox02=c0+c1*n7
aprox03=c0+c1*n7+c2*(n7**2)
aprox04=c0+c1*n7+c2*(n7**2)+c3*(n7**2)
aprox05=c0+c1*n7+c2*(n7**2)+c3*(n7**2)+c4*(n7**2)

aproxi01=c0
aproxi02=c0+c1*n8
aproxi03=c0+c1*n8+c2*(n8**2)
aproxi04=c0+c1*n8+c2*(n8**2)+c3*(n8**2)
aproxi05=c0+c1*n8+c2*(n8**2)+c3*(n8**2)+c4*(n8**2)


print('x\tExacto\t\t\tAprox.1\t\tAprox.2\t\tAprox.3\t\tAprox.4\t\tAprox.5')
print('0','\t',math.cos(n0),'\t\t\t',ap1,'\t\t',ap2,'\t\t',ap3,'\t\t',ap4,'\t\t',ap5)
print('0.00001',math.cos(n1),'\t\t',apro1,'\t\t',apro2,'\t\t',apro3,'\t',apro4,'\t',apro5)
print('0.0001','\t',math.cos(n2),'\t\t',aprox1,'\t\t',aprox2,'\t\t',aprox3,'\t',aprox4,'\t',aprox5)
print('0.001','\t',math.cos(n3),'\t\t',aproxi1,'\t\t',aproxi2,'\t\t',aproxi3,'\t',aproxi4,'\t',aproxi5)
print('0.01','\t',math.cos(n4),'\t',aproxim1,'\t\t',aproxim2,'\t\t',aproxim3,'\t',aproxim4,'\t',aproxim5)
print('0,1','\t',math.cos(n5),'\t',aproxima1,'\t\t',aproxima2,'\t\t',aproxima3,'\t\t',aproxima4,'\t\t',aproxima5)
print('1','\t',math.cos(n6),'\t',aprox01,'\t\t',aprox02,'\t\t',aprox03,'\t\t',aprox04,'\t\t',aprox05)
print('10','\t',math.cos(n7),'\t',aproxi01,'\t\t',aproxi02,'\t\t',aproxi03,'\t\t',aproxi04,'\t\t',aproxi05)





