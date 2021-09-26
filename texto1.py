#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 17:02:37 2021

@author: cubos
"""
from typing import Counter


def cargarPalabras():
    archivo = open("words.txt","r")
    texto = archivo.read()
    datos = texto.split()
    archivo.close()
    return (datos)

def espacio():
    for i in range(2):
        print('      ')
        i+=1


#print(len(dic1)) imprime la longitud del diccionaro


alfabeto = "abcdefghijklmnopqrstuvwxyz"

cifrado = "smk wfkvpylzly ipuh hpsvlqt, tfz pk m imb, smk, slkumqqb, imv"\
          " fkl. hl wfkvpvuly ft m uzpqqpfk, uzpqqpfk, uzpqqpfk "\
          " mky pkwfzzcgupaql, lmwh wmzly tfz ab glztlwu mcufsmufkv, "\
          "lncmqqb pkwfzzcgupaql, ihpql uhl spkyv ft mqq uhl afyplv "\
          "tzllqb slquly fkl pkuf uhl fuhlz, pkypvupkdcpvhmaql. smk vmpy, "\
          "'uhl ckpolzvl pv ybpkd.' smk qffely mafcu mu uhl ypsspkd dmqmjplv."\
          " uhl dpmku vumzv, vglkyuhzptuv, ilzl dfkl qfkd mdf, amwe pk uhl"\
          " ypsslvu ft uhl yps tmz gmvu.mqsfvu mqq"\
          " vumzv ilzl ihpul yimztv, tmypkd uf uhl lky."
          
letras = {} #Se inicializa el diccionario


for c in alfabeto: #se crea e inicializa el diccionario "letras"
#para cada CARACTER en ALFABETO, c va a valer 0
    letras[c] = 0
#print(letras) esto imprime el primer diccionario
for c in alfabeto:
    letras[c]=cifrado.count(c)

archivo=open("salida.csv","w")
for c in letras.keys():
    archivo.write(c+","+str(letras[c])+"\n")
archivo.close()

dic1 = cargarPalabras()
cont = 0
def contador():
    print('las palabras que hay son: '+str(cont))
    
   
#probando con mcufsmufkv
espacio()
cont=0
for pal in dic1:
    if (len(pal)==10):
        if (pal[0]==pal[5]and pal[3]==pal[7]and pal[2]==pal[6]):
            cont +=1
            print(pal)

contador()
print("\nsera nuestro primer filtro de letras:\nM=a,e, U=t, F=i,o, V=g,n,s, C=c,u,n, S= v,m,r, K=n,o,e")          

espacio()
#para fkl
cont = 0
for pal in dic1:
    if (len(pal)==3):
      if(pal[0]=="i"or pal[0]=="o"):
          if(pal[1]=="n"or pal[1]=="o"or pal[1]=="e"):
            cont +=1
            print(pal)
contador()
print("actualizacion de de palabras:\nM=a,e, U=t, F=i,o, V=g,n,s, C=c,u,n, S= v,m,r, K=n,o, L=knse")
espacio()

#para uzpqqpfk
cont = 0
for pal in dic1:
    if (len(pal)==8):
      if(pal[0]=="t"):
          if(pal[-1]=="n"or pal[-1]=="o"):
              if(pal[2]==pal[5] and pal[3]==pal[4]):
                  cont +=1
                  print(pal)
contador()
print("actualizacion de de palabras:\nM=a,e, U=t, F=o, V=g,n,s, C=c,u,n, S= v,m,r, K=n L=knse, Z=r, P=i, Q=l")

'''

#para mcufsmufkv segunda ronda
      
for pal in dic1:
    
    if (len(pal)==10):
        if(pal[3] and pal[7]=="o"):
            if(pal[-2]=="n"):
                if (pal[0]=="a"or pal[0]=="e"):
                    if(pal[2]=="t"and pal[6]=="t"):
                        cont +=1
                        print(pal)
print(cont)

CUARTO FILTRO DE LETRAS
posM="a"
posU="t"
posF="o"
posV="s"
posC="u"
posS="m"
posK="n"
posL="ke"
posZ="r"
posP="i"
posQ="l"

#para spkyv

for pal in dic1:
    if (len(pal)==5):
        if (pal[0]=="m" and pal[1]=="i" and pal[2]=="n" and pal[-1]=="s"):
            cont+=1
            print(pal)
print(cont)

QUINTO FILTRO DE LETRAS
posM="a"
posU="t"
posF="o"
posV="s"
posC="u"
posS="m"
posK="n"
posL="ke"
posZ="r"
posP="i"
posQ="l"
posY="dek"


#para ypsspkd
for pal in dic1:
    if (len(pal)==7):
        if(pal[1]=="i"and pal[-3]=="i"):
            if(pal[2]=="m" and pal[3]=="m"):
                if(pal[-2]=="n"):
                    cont+=1
                    print(pal)
print(cont)

SEXTO FILTRO DE LETRAS
posM="a"
posU="t"
posF="o"
posV="s"
posC="u"
posS="m"
posK="n"
posL="ke"
posZ="r"
posP="i"
posQ="l"
posY="d"
posD="g"

#para gqmwl
for pal in dic1:
    if (len(pal)==5):
        if(pal[1]=="l" and pal[2]=="a"):
            if(pal[-1]=="k" or pal[-1]=="e"):
                if(pal[0]!="s"and pal[-2]!="n"and pal[-2]!="r"and pal[-2]!="m")\
                    and pal[-2]!="t"and pal[-2]!="d"and pal[-2]!="s":
                    cont+=1
                    print(pal)
print(cont)    

SEXTO FILTRO DE LETRAS
posM="a"
posU="t"
posF="o"
posV="s"
posC="u"
posS="m"
posK="n"
posL="ke"
posZ="r"
posP="i"
posQ="l"
posY="d"
posW="czk"
posG="bcfgp"
posD="g"

#para imv
for pal in dic1:
    if (len(pal)==3):
        if(pal[1]=="a" and pal[2]=="s"):
            cont+=1
            print(pal)
SEPTIMO FILTRO DE LETRAS
posM="a"
posU="t"
posF="o"
posV="s"
posC="u"
posS="m"
posK="n"
posL="ke"
posZ="r"
posP="i"
posQ="l"
posY="d"
posW="czk"
posG="bcfgp"
posI="ghvw"
posD="g"

#para fkl
for pal in dic1:
    if (len(pal)==3):
        if(pal[0]=="o" and pal[1]=="n"):
            cont+=1
            print(pal)
            
OCTAVO FILTRO DE LETRAS
posM="a"
posU="t"
posF="o"
posV="s"
posC="u"
posS="m"
posK="n"
posL="e"
posZ="r"
posP="i"
posQ="l"
posY="d"
posW="czk"
posG="bcfp"
posI="hvw"
posD="g"

#para hl
for pal in dic1:
    if (len(pal)==2):
        if(pal[1]=="e"and pal[0]!="m"and pal[0]!="r"):
            cont+=1
            print(pal)


NOVENO FILTRO DE LETRAS
posM="a"
posU="t"
posF="o"
posV="s"
posC="u"
posS="m"
posK="n"
posL="e"
posZ="r"
posP="i"
posQ="l"
posY="d"
posW="czk"
posG="bcfp"
posI="hvw"
posH="bhwy"
posD="g"


#para tmypkd
for pal in dic1:
    if(len(pal)==6):
        if(pal[1]=="a" and pal[2]=="d" and pal[-1]=="g"):
            cont +=1
            print(pal)

#DECIMO FILTRO DE LETRAS
posM="a"
posU="t"
posF="o"
posV="s"
posC="u"
posS="m"
posK="n"
posL="e"
posZ="r"
posP="i"
posQ="l"
posY="d"
posD="g"
posW="czk"
posG="bcfp"
posI="hvw"
posH="bhwy"
posT="fjw"

#para wmzly
for pal in dic1:
    if (len(pal)==5):
        if(pal[1]=="a"and pal[2]==posZ and pal[3]==posL\
             and pal[-1]==posY and pal[0]!=posC and pal[0]!=posF\
                and pal[0]!=posY):
                if(pal[0]=="c" or pal[0]=="z" or pal[0]=="k"):
                    cont+=1
                    print(pal)


#DECIMO FILTRO DE LETRAS
posM="a"
posU="t"
posF="o"
posV="s"
posC="u"
posS="m"
posK="n"
posL="e"
posZ="r"
posP="i"
posQ="l"
posY="d"
posD="g"
posW="c"
posG="bfp"
posI="hvw"
posH="bhwy"
posT="fjw"

#para glztlwu
#     perfect
for pal in dic1:
    if(len(pal)==7):
        if(pal[1]==posL and pal[4]==posL and pal[2]==posZ\
            and pal[-2]==posW):
             cont+=1
             print(pal)
print(cont)

#11 FILTRO DE LETRAS
posA=""
posB=""
posC="u"
posD="g"
posF="o"
posG="p"
posH="bhwy"
posI="hvw"
posJ=""
posK="n"
posL="e"
posM="a"
posN=""
posO=""
posP="i"
posQ="l"
posR=""
posS="m"
posT="f"
posU="t"
posV="s"
posW="c"
posX=""
posY="d"
posZ="r"

#para afyplv
for pal in dic1:
    if(len(pal)==6):
        if(pal[1]==posF and pal[2]==posY and pal[3]==posP and pal[4]==posL):
            print(pal)

#12 FILTRO DE LETRAS
posA="b"
posB="y"
posC="u"
posD="g"
posE=""
posF="o"
posG="p"
posH="hw"
posI="hvw"
posJ=""
posK="n"
posL="e"
posM="a"
posN=""
posO=""
posP="i"
posQ="l"
posR=""
posS="m"
posT="f"
posU="t"
posV="s"
posW="c"
posX=""
posY="d"
posZ="r"

#para ab
for pal in dic1:
    if(len(pal)==2):
        if(pal[0]==posA and pal[1]!=posL):
            print(pal)

#13 FILTRO DE LETRAS
posA="b"
posB="y"
posC="u"
posD="g"
posE="kh"
posF="o"
posG="p"
posH="hw"
posI="hvw"
posJ=""
posK="n"
posL="e"
posM="a"
posN=""
posO=""
posP="i"
posQ="l"
posR=""
posS="m"
posT="f"
posU="t"
posV="s"
posW="c"
posX=""
posY="d"
posZ="r"

#para amwe
for pal in dic1:
    if(len(pal)==4):
        if(pal[0]==posA and pal[1]==posM and pal[2]==posW):
            print(pal)

#14 FILTRO DE LETRAS
posA="b"
posB="y"
posC="u"
posD="g"
posE="kh"
posF="o"
posG="p"
posH="hw"
posI="hvw"
posJ="x"
posK="n"
posL="e"
posM="a"
posN=""
posO=""
posP="i"
posQ="l"
posR=""
posS="m"
posT="f"
posU="t"
posV="s"
posW="c"
posX=""
posY="d"
posZ="r"
#para dmqmjplv
#     galaxies
for pal in dic1:
    if(len(pal)==8):
        if(pal[0]==posD and pal[1]==posM and pal[3]==posM and pal[-2]==posL):
            print(pal)
           
#15 FILTRO DE LETRAS
posA="b"
posB="y"
posC="u"
posD="g"
posE="kh"
posF="o"
posG="p"
posH="hw"
posI="hvw"
posJ="x"
posK="n"
posL="e"
posM="a"
posN="q"
posO=""
posP="i"
posQ="l"
posR=""
posS="m"
posT="f"
posU="t"
posV="s"
posW="c"
posX=""
posY="d"
posZ="r"
#para lncmqqb
#     equally
for pal in dic1:
    if(len(pal)==7):
        if(pal[0]==posL and pal[-1]==posB and pal[-2]==posQ and pal[-3]==posQ):
            print(pal)
#16 FILTRO DE LETRAS            
posA="b"
posB="y"
posC="u"
posD="g"
posE="kh"
posF="o"
posG="p"
posH="hw"
posI="hw"
posJ="x"
posK="n"
posL="e"
posM="a"
posN="q"
posO="v"
posP="i"
posQ="l"
posR=""
posS="m"
posT="f"
posU="t"
posV="s"
posW="c"
posX=""
posY="d"
posZ="r"
#para ckpolzvl
#     universe
for pal in dic1:
    if(len(pal)==8):
        if(pal[0]==posC and pal[1]==posK and pal[4]==posL and pal[5]==posZ\
             and pal[-1]==posL):
             print(pal)
              '''
#16 FILTRO DE LETRAS
posA="b"
posB="y"
posC="u"
posD="g"
posE="k"
posF="o"
posG="p"
posH="h"
posI="w"
posJ="x"
posK="n"
posL="e"
posM="a"
posN="q"
posO="v"
posP="i"
posQ="l"
posR=""
posS="m"
posT="f"
posU="t"
posV="s"
posW="c"
posX=""
posY="d"
posZ="r"
'''
#para uhl
for pal in dic1:
    if(len(pal)==3):
        if(pal[0]==posU and pal[2]==posL):
                print(pal)
                '''
espacio()

def traduccion(cifrado):
    nuevoTexto={'a':'b','b':'y','c':'u','d':'g','e':'k','f':'o','g':'p','i':'w',\
        'j':'x','k':'n','l':'e','m':'a','n':'q','o':'v','p':'i','q':'l','s':'m',\
            't':'f','u':'t','v':'s','w':'c','y':'d','z':'r'}
    transTable=cifrado.maketrans(nuevoTexto)
    cifrado = cifrado.translate(transTable)
    print(cifrado)


traduccion(cifrado)




espacio()


