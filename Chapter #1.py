import nltk
import numpy as np 
from nltk.book import *
from matplotlib import pyplot as plt 
nltk.download()

#1.3 BUSQUEDAD DE TEXTO
#text1.concordance( "monstrous" )                #Concordancia exacta de la palabra
#text1.similar("monstrous")                      #Similaridad de la palabra dentro de un contexto
#text2.common_contexts(["monstrous", "very"])    #Nos permite examinar solo los contextos que comparten dos o más palabras
#text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])   #Determinar la ubicación de una palabra en el texto: cuántas palabras desde el principio aparece. Esta información posicional se puede mostrar utilizando un diagrama de dispersión
#text3.generate()                                #Genera un texto aletorio en el estilo de texto con el que se llama el metodo

#1.4 CONTEO DE VOCABULARIO
texto = "Esto es una prueba de hola y mas hola"
len(texto)                                          
sorted(set(texto))  #Ordenar las cadenas y simbolos diferentes con set
len(set(texto))     #Obtenemos el tamaño del vocabulario

def lexical_diversity (text):
    return len(set(text))/len(text)

def percentage(count, total):
    return  100*count/total

lexical_diversity(texto)     #Calculamos una medida de la riqueza léxica del texto. El ejemplo siguiente nos muestra que el número de palabras distintas
percentaje(texto.count('a'),len(texto)) # Podemos contar con qué frecuencia aparece una palabra en un texto y calcular qué porcentaje del texto está ocupado por una palabra específica
	


