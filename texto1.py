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
print("actualizacion de de letras:\nM=a,e, U=t, F=i,o, V=g,n,s, C=c,u,n, S= v,m,r, K=n,o, L=knse")
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
print("actualizacion de de letras:\nM=a,e, U=t, F=o, V=g,n,s, C=c,u,n, S= v,m,r, K=n L=k,n,s,e, Z=r, P=i, Q=l")
espacio()

#para mcufsmufkv segunda ronda
cont=0     
for pal in dic1:
    if (len(pal)==10):
        if(pal[3] and pal[7]=="o"):
            if(pal[-2]=="n"):
                if (pal[0]=="a"or pal[0]=="e"):
                    if(pal[2]=="t"and pal[6]=="t"):
                        cont +=1
                        print(pal)
contador()
print("actualizacion de de letras:\nM=a, U=t, F=o, V=s, C=u, S= m, K=n L=k,e, Z=r, P=i, Q=l")
espacio()

#Aqui las empezamos a usar como variables pos=posible
posM="a"
posU="t"
posF="o"
posV="s"
posC="u"
posS="m"
posK="n"
posZ="r"
posP="i"
posQ="l"

#para spkyv
cont=0
for pal in dic1:
    if (len(pal)==5):
        if (pal[0]==posS and pal[1]==posP and pal[2]==posK and pal[-1]==posV):
            cont+=1
            print(pal)
contador()
print("actualizacion de de letras:\nM=a, U=t, F=o, V=s, C=u, S= m, K=n L=k,e, Z=r, P=i, Q=l, Y=d,e,k")
espacio()

#para ypsspkd
cont=0
for pal in dic1:
    if (len(pal)==7):
        if(pal[1]==posP and pal[-3]==posP):
            if(pal[2]==posS and pal[3]==posS):
                if(pal[-2]==posK):
                    cont+=1
                    print(pal)

contador()
print("actualizacion de de letras:\nM=a, U=t," \
    "F=o, V=s, C=u, S= m, K=n L=k,e, Z=r, P=i, Q=l, Y=d, D=g")
espacio()

#Agregamos nuevas letras
posY="d"
posD="g"

#para gqmwl
for pal in dic1:
    if (len(pal)==5):
        if(pal[1]==posQ and pal[2]==posM):
            if(pal[-1]=="k" or pal[-1]=="e"):
                if(pal[0]!=posV and pal[-2]!=posK and pal[-2]!=posZ and pal[-2]!=posS)\
                    and pal[-2]!=posU and pal[-2]!=posY and pal[-2]!=posV:
                    cont+=1
                    print(pal)
contador()
print("actualizacion de de letras:\nM=a, U=t, " \
    "F=o, V=s, C=u, S= m, K=n L=k,e, Z=r, P=i, Q=l, Y=d, D=g, W=c,z,k, "\
        "G=b,c,f,g,p")
espacio()
print
#para imv
cont=0
for pal in dic1:
    if (len(pal)==3):
        if(pal[1]==posM and pal[2]==posV):
            cont+=1
            print(pal)
contador()
print("actualizacion de de letras:\nM=a, U=t, " \
    "F=o, V=s, C=u, S= m, K=n L=k,e, Z=r, P=i, Q=l, Y=d, D=g,  W=c,z,k, G=b,c,f,g,p,I=g,h,v,w")
espacio()            
            



#para fkl
cont=0
for pal in dic1:
    if (len(pal)==3):
        if(pal[0]=="o" and pal[1]=="n"):
            cont+=1
            print(pal)
contador()
print("actualizacion de de letras:\nM=a, U=t, " \
    "F=o, V=s, C=u, S= m, K=n L=k,e, Z=r, P=i, Q=l, Y=d, D=g, W=c,z,k, "\
    "G=b,c,f,g,p, I=h,v,w")
espacio()     

#nueva letra encontrada
posL="e"


#para hl
cont=0
for pal in dic1:
    if (len(pal)==2):
        if(pal[1]==posL and pal[0]!=posS and pal[0]!=posZ):
            cont+=1
            print(pal)
contador()
print("actualizacion de de letras:\nM=a, U=t, " \
    "F=o, V=s, C=u, S= m, K=n L=e, Z=r, P=i, Q=l, Y=d, D=g, W=c,z,k, "\
        "G=b,c,f,g,p, I=h,v,w, H=b,h,w,y")
espacio()  

#para tmypkd
cont=0
for pal in dic1:
    if(len(pal)==6):
        if(pal[1]==posM and pal[2]==posD and pal[-1]==posD):
            cont +=1
            print(pal)
contador()
print("actualizacion de de letras:\nM=a, U=t, "\
    "F=o, V=s, C=u, S= m, K=n L=e, Z=r, P=i, Q=l, Y=d, D=g, W=c,z,k, "\
        "I=h,v,w, H=b,h,w,y, T=f,j,w")
espacio()  

          



#para wmzly
cont=0
for pal in dic1:
    if (len(pal)==5):
        if(pal[1]==posM and pal[2]==posZ and pal[3]==posL\
             and pal[-1]==posY and pal[0]!=posC and pal[0]!=posF\
                and pal[0]!=posY):
                if(pal[0]=="c" or pal[0]=="z" or pal[0]=="k"):
                    cont+=1
                    print(pal)
contador()
print("actualizacion de de letras:\nM=a, U=t, "\
    "F=o, V=s, C=u, S= m, K=n L=e, Z=r, P=i, Q=l, Y=d, D=g, W=c, "\
        "G=b,f,p, I=h,v,w, H=b,h,w,y, T=fj,w")
espacio() 
#nueva letra 
posW="c"
  


#para glztlwu
cont=0
for pal in dic1:
    if(len(pal)==7):
        if(pal[1]==posL and pal[4]==posL and pal[2]==posZ\
            and pal[-2]==posW):
             cont+=1
             print(pal)
contador()
print("actualizacion de de letras:\nM=a, U=t, "\
    "F=o, V=s, C=u, S= m, K=n L=e, Z=r, P=i, Q=l, Y=d, D=g, W=c, "\
        "G=p, I=h,v,w, H=b,h,w,y, T=f, F=o")
espacio() 

posF="o"
posG="p"
posT="f"

#para afyplv
cont=0
for pal in dic1:
    if(len(pal)==6):
        if(pal[1]==posF and pal[2]==posY and pal[3]==posP and pal[4]==posL):
            print(pal)
contador()
print("actualizacion de de letras:\nM=a, U=t, "\
    "F=o, V=s, C=u, S= m, K=n L=e, Z=r, P=i, Q=l, Y=d, D=g, W=c, "\
        "G=p, I=h,v,w, H=h,w, T=f, F=o, A=b, B=y")
espacio() 

posA="b"
posB="y"

#para ab
cont=0
for pal in dic1:
    if(len(pal)==2):
        if(pal[0]==posA and pal[1]!=posL):
            print(pal)
contador()
print("actualizacion de de letras:\nM=a, U=t, "\
    "F=o, V=s, C=u, S= m, K=n L=e, Z=r, P=i, Q=l, Y=d, D=g, W=c, "\
        "G=p, I=h,v,w, H=h,w, T=f, F=o, A=b, B=y, E=k,h")
espacio() 



#para amwe
cont=0
for pal in dic1:
    if(len(pal)==4):
        if(pal[0]==posA and pal[1]==posM and pal[2]==posW):
            print(pal)
contador()
print("actualizacion de de letras:\nM=a, U=t, "\
    "F=o, V=s, C=u, S= m, K=n L=e, Z=r, P=i, Q=l, Y=d, D=g, W=c, "\
        "G=p, I=h,v,w, H=h,w, T=f, F=o, A=b, B=y, E=k,h, J=x, ")

espacio()

posJ="x" 


#para dmqmjplv
cont=0
for pal in dic1:
    if(len(pal)==8):
        if(pal[0]==posD and pal[1]==posM and pal[3]==posM and pal[-2]==posL):
            print(pal)
contador()
print("actualizacion de de letras:\nM=a, U=t, "\
    "F=o, V=s, C=u, S= m, K=n L=e, Z=r, P=i, Q=l, Y=d, D=g, W=c, "\
        "G=p, I=h,v,w, H=h,w, T=f, F=o, A=b, B=y, E=k,h, J=x, "\
            "N=q")

espacio()
posN="q"         

#para lncmqqb
cont=0
for pal in dic1:
    if(len(pal)==7):
        if(pal[0]==posL and pal[-1]==posB and pal[-2]==posQ and pal[-3]==posQ):
            print(pal)
contador()
print("actualizacion de de letras:\nM=a, U=t, "\
    "F=o, V=s, C=u, S= m, K=n L=e, Z=r, P=i, Q=l, Y=d, D=g, W=c, "\
        "G=p, I=h,v,w, H=h,w, T=f, F=o, A=b, B=y, E=k,h, J=x, "\
            "N=q, O= v")

espacio()            

posO="v"            

#para ckpolzvl
cont=0
for pal in dic1:
    if(len(pal)==8):
        if(pal[0]==posC and pal[1]==posK and pal[4]==posL and pal[5]==posZ\
             and pal[-1]==posL):
             print(pal)
contador()
print("actualizacion de de letras:\nM=a, U=t, "\
    "F=o, V=s, C=u, S= m, K=n L=e, Z=r, P=i, Q=l, Y=d, D=g, W=c, "\
        "G=p, I=w, H=h, T=f, F=o, A=b, B=y, E=k, J=x, "\
            "N=q, O= v")

espacio()                
posE="k" 
posH="h"
posI="w"          


#para uhl
cont=0
for pal in dic1:
    if(len(pal)==3):
        if(pal[0]==posU and pal[2]==posL):
                print(pal)
contador()
espacio() 
espacio()
def traduccion(cifrado):
    nuevoTexto={'a':'b','b':'y','c':'u','d':'g','e':'k','f':'o','g':'p','i':'w',\
        'j':'x','k':'n','l':'e','m':'a','n':'q','o':'v','p':'i','q':'l','s':'m',\
            't':'f','u':'t','v':'s','w':'c','y':'d','z':'r'}
    print(nuevoTexto,"\nEste es el diccionario que usaremos para descifrarlo ")
    espacio()
    espacio()
    
    transTable=cifrado.maketrans(nuevoTexto)
    cifrado = cifrado.translate(transTable)
    print("El texto traducido es:\n",cifrado)

traduccion(cifrado)

espacio()


