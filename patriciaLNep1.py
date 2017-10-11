#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP, 
  DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA. 
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO-PROGRAMA (EP) FORAM 
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
  OU PLÁGIO.  
  DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS DESSE
  PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A SUA DISTRIBUIÇÃO.
  ESTOU CIENTE QUE OS CASOS DE PLÁGIO E DESONESTIDADE ACADÊMICA
  SERÃO SEVERAMENTE PUNIDOS.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E, AINDA
  ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Nome:PATRICIA 
  Número USP: 
  Curso: ESTATISTICA               Turma: 
  Exercício-Programa 01  

  Referências: Com exceção das rotinas que podem ser fornecidas
  no enunciado ou em sala de aula, caso você tenha utilizado
  alguma referência, liste-as abaixo para que o seu programa não
  seja considerado plágio ou irregular.
  
  Exemplo:
  - O algoritmo de ordenação Quicksort foi baseado em
  http://www.ime.usp.br/~pf/algoritmos/aulas/quick.html

"""
'''
Dados um número inteiro positivo n e uma sequência de n datas, imprimir qual
é o dia da semana correspondente a cada uma das datas fornecidas.
mes = 1 corresponde a janeiro etc.
valor = 0 corresponde a domingo etc.
'''
def main():
    
    n = int(input("Digite um numero inteiro: "))
    i = 1 #contador
    
    while i <= n:
        dia = int(input("Digite o dia: "))
        mes = int(input("Digite o mes: "))
        ano = int(input("Digite o ano: "))
        
        a = ano - (((14 - mes)/12)//1)
        k = a + ((a/4)//1) - ((a/100)//1) + ((a/400)//1)
        m = mes + 12 * (((14 - mes)/12)//1) - 2   
        d = (dia + k + (((31 * m)/12)//1)) % 7   
    
        if d == 0:
            print ("Data %d: %d/%d/%d - domingo" % (i, dia, mes, ano))
        elif d == 1:
            print ("Data %d: %d/%d/%d - segunda-feira" % (i, dia, mes, ano))
        elif d == 2:
            print ("Data %d: %d/%d/%d - terça-feira" % (i, dia, mes, ano))
        elif d == 3:
            print ("Data %d: %d/%d/%d - quarta-feira" % (i, dia, mes, ano))
        elif d == 4:
            print ("Data %d: %d/%d/%d - quinta-feira" % (i, dia, mes, ano))
        elif d == 5:
            print ("Data %d: %d/%d/%d - sexta-feira" % (i, dia, mes, ano))
        elif d == 6:
            print ("Data %d: %d/%d/%d - sábado" % (i, dia, mes, ano))
            
        i += 1
        
main()
