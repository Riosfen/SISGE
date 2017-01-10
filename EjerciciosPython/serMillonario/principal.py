'''
Created on 10 ene. 2017

@author: Victor
'''

numPreguntas = 0
numTotalPreguntas = 0

fichero  = open("preguntas.txt", "r")
for linea in fichero.readlines():
    auxLinea = linea.split(" ", 1)

    if (auxLinea[0] == "P:" ):
        numTotalPreguntas = numTotalPreguntas + 1

fichero  = open("preguntas.txt", "r")
for linea in fichero.readlines():

    auxLinea = linea.split(" ", 1)

    if (auxLinea[0] == "P:" ):
        numPreguntas = numPreguntas+1
        print ("Pregunta" , numPreguntas , "/" , numTotalPreguntas)
        print (auxLinea[1])
        i = 0
        
    else:
        
        if ("*" in linea):
            preguntaCorrecta = linea.split("*", 1)
            respuesta = preguntaCorrecta[1].split(".", 1)
            print ("la respuesta correcta es:" , respuesta[0])
        
        print 
        
        