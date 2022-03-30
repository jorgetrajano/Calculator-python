# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

print("\nObserve as operações matemáticas a seguir:")
#Solicitar operação matemática do usuário.
print("\n1- Adição;")
print("\n2- Subtração;")
print("\n3- Multiplicação;")
print("\n4- Divisão;")


op = int(input("\nDigite a função desejada: "))

#Definir valores válidos para as operações matemáticas econstrução da calculadora.
if(op == 1 or op == 2 or op == 3 or op == 4):

    #Primeira operação válida.
    if(op == 1):
       
    
        print(" --- Adição ---")
        
        a1 = float(input("Informe a primeira variável: "))
        a2 = float(input("Informe a segunda variável: "))
        soma = a1 + a2
        
        print( a1, " + ", a2, " = ", soma)
    
    #Segunda operação válida.    
    elif(op == 2):
        
        print(" --- Subtração ---")
        
        s1 = float(input("Informe a primeira variável: "))
        s2 = float(input("Informe a segunda variável: "))
        sub = s1 - s2
        
        print( s1, " - ", s2, " = ", sub)
    
    #Terceira operação válida.
    elif(op == 3):
        
        print(" --- Multiplicação ---")
        
        m1 = float(input("Informe a primeira variável: "))
        m2 = float(input("Informe a segunda variável: "))
        mult = m1 * m2
        
        print(m1, " * ", m2, " = ", mult)
    
    #Quarta operação válida.
    elif(op == 4):
        
        print(" --- Divisão ---")
        
        d1 = float(input("Informe a primeira variável: "))
        d2 = float(input("Informe a segunda variável: "))
        div = d1 / d2
        
        print( d1, " / ", d2, " = ", div)

#Caso a entrada não seja identificada, informar:        
else:
    print("\nOperação inválida!")