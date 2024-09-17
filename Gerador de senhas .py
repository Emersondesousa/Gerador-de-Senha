#Crie um programa que gere senhas fortes e aleatórias,
#utilizando diferentes tipos de caracteres (letras maiúsculas, minúsculas, números e símbolos).
#O programa deve permitir ao usuário definir o tamanho da senha e os tipos de caracteres que deseja incluir.
import random
import string

usuario_tamanho = int(input("Informe o tamanho da senha: "))
letra_maiuscula = input("Desenha incluir letra Maiuscula ? (s/n):  ")
letra_minuscula = input("Deseja incluir Letra Minuscula ? (s/n):")
caracteres_pontuação = input("Deseja incluir Caracteres de Pontuação? (s/n): ")
numeros = input("Deseja incluir Números? (s/n): ")
caractere = ''
if letra_maiuscula == 's':
    caractere += string.ascii_uppercase
if letra_minuscula == 's':
    caractere += string.ascii_lowercase
if caracteres_pontuação == 's':
    caractere += string.punctuation
if numeros == 's':
    caractere += string.digits
if not caractere:
    print("Nenhum Caractere encontrado.")
else:    
   senha =  ''.join(random.choice(caractere) for i in range(usuario_tamanho))    #join combina os caracteres da senha.
   print(f"Senha : {senha}")    

