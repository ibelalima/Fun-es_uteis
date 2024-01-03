#Fatorial de um numero
def fatorial(numero):
    fat = 1
    for i in range (1,numero+1):
        fat *=i
    return fat

#potencia de um numero x elevado a y
def potencia(base,expoente):
    mult = base
    for i in range(1,expoente):
        mult = mult *base
    return mult

#bolha de ordenação, funciona para nomes e numeros
def bolha (lista):
    trocou = True
    fim = (len(lista))
    while fim >0 and trocou:
        trocou = False
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
                trocou = True
        fim = fim -1
    return lista

#fala todos os numeros primos que estão presentes na lista
def primos(lista):
    lista_primos = []
    total = 0
    for i in lista:
        for x in range (1,i+1):
            if i % x == 0:
                total +=1
        if total == 2:
            lista_primos.append(i)
        total = 0
    return lista_primos

#remove um indice da lista e passa todo o resto.
def remover_indice_da_lista(lista,indice):
    lista_temporaria = []
    for i in range(len(lista)):
        if i != indice:
            lista_temporaria.append(lista[i])
    return lista_temporaria

#remove um numero especifico da lista 
def remover_numero_da_lista(lista,remover):
    lista2 = []
    for i in (lista):
        if i != remover:
            lista2.append(i)
    return lista2
#adiciona um termo na lista em um indice escolhido
def adicionar_termo_no_indice_da_lista(lista,termo,indice):
    lista2 =[]
    for i in range (len(lista)):
        if i != indice:
            lista2.append(lista[i])
        elif i == indice:
            lista2.append(termo)
            lista2.append(lista[i])
    return lista2

#verifica se o numero é primo
def verificar_primo(numero):
    recebe = 0
    for i in range(1,numero+1):
        if numero%i == 0:
            recebe +=1
    if recebe == 2:
        print("o numero é primo")
        return True
    else:
        print("o numero não é primo")
        return False

#inverte a frase mantendo as palavras iguais
def inverter_frase(frase):
    palavra=""
    inverso = ""

    for i in frase:
        if i != " ":
            palavra += i
        else:
            inverso = palavra + " " + inverso
            palavra =""
    inverso = palavra + " " + inverso
    return inverso

#inverte uma palavra
def inverter_palavra(palavra):
    cont = len(palavra) -1
    palavra_inverso = ''
    for i in range (len(palavra)):
        palavra_inverso+= palavra[cont]
        cont -= 1
    return palavra_inverso

#print palavra em diagonal
def palavra_diagonal(palavra):
    espaco = ''
    for letra in palavra:
        print(espaco,letra)
        espaco += " "

#print palavra em diagonal inversa
def palavra_diagonal_inversa(palavra):
    cont = len(palavra)
    espaco = ""
    for x in palavra:
        for i in range(cont):
            espaco += " "
        print(espaco,x)
        espaco = ""
        cont -= 1

#verifica e conta todos os numeros primos até o numero escolhido
def verificar_todos_os_numeros_primos(numero):
    contador = 0
    for i in range (1,numero+1):
        recebe = 0
        for x in range(1,i+1):
            if i%x == 0:
                recebe +=1
                if recebe > 2:
                    break
        if recebe == 2:
            print(i," ",end="")
            contador +=1
        
    print("existem",contador,"numeros primos até o numero",numero)

palavra_diagonal_inversa("computador")