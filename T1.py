#Programa 1. Retorna la palabra palindrome mas larga en un texto

cadena='cas' #Inserte texto aqui

#Funcion Palindrome.

def palindromes(text):
	#Cambiar el texto a minuscula si es necesario
    text = text.lower()
    #Inicializando lista con palabras palindromes
    pal = []

    for i in range(len(text)):
        for j in range(0, i):
            word = text[j:i + 1]

            if word == word[::-1]: #Verificando si es palindrome
                pal.append(word)   #Agregando a la lista

#Si pal no es nulo retorna la palabra palindrome mas larga
    
    if len(pal)!=0:
        return max(pal, key=len) #Retorna la palabra mas larga de la lista

#Si no, no existe ninguna palabra palindrome en el texto
    	
    else: 
        return "No hay ninguna palabra palindrome"

#Escribe resultado
    	
print "La palabra palindorme mas larga es: " + palindromes(cadena)
    
    	
    


