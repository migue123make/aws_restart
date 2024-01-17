"""
Your module description
"""
print ("Conteo hasta 10")
#utilizando el range (rango)

#range (inicio, valor_final - 1) con aumento de 1
print("Range con dos argumentos")
for  x  in range (0,11):
    print(x)
    
#aqui imprime del 1 al 10 o 

inicio = 0
final = 10

for  x  in range (inicio, final +1):
    print(x)
    
    # range(final) con aumento de 1 y da por hecho que inicia en 0
    
    
    
    
    #aqui da por hecho que inicia en 0
    print("range con un argumento")
     
     for x in range (final+1):
         print(x)
    
    
    
    #range con 3 argumentos
    #inicio, final, salto
    
    salto = 2
    for x in range(inicio, final +1, salto):
        print(x)
        
        
        #inicia en 0 luego brinca al 2, 4, 6, 8, 10