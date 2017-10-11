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

  Nome:PATRICIA L DO NASCIMENTO
  Número USP: 6836726
  Curso: ESTATISTICA               Turma: 48
  Exercício-Programa 02  

  Referências: Com exceção das rotinas que podem ser fornecidas
  no enunciado ou em sala de aula, caso você tenha utilizado
  alguma referência, liste-as abaixo para que o seu programa não
  seja considerado plágio ou irregular.
  
  Exemplo:
  - O algoritmo de ordenação Quicksort foi baseado em
  http://www.ime.usp.br/~pf/algoritmos/aulas/quick.html

"""
'''
Este programa testa se os dígitos verificadores de uma sequência de
números de CPF ou de cartões de crédito estão corretos.
'''

def main():
    
    print("Qual documento deseja escolher?")
    print("Utilize 1 para CPF e 2 para cartão de crédito, ou 0 para terminar.")
    
    doc = int(input("Digite a sua opção(1 ou 2 ou 0): "))
    
    #CPF
    if doc == 1:
        print("\nObs: Um número de CPF deve ser fornecido como um único número inteiro de onze dígitos (ou seja, sem os pontos e sem o hífen).")
        cpf = int(input("Digite um número de CPF: "))
        print("\n")
        
        #Cálculo do primeiro dígito verificador
        cpf_num = cpf // 100        #Elimina dois números do cpf
        cont = 9                    #Contador   
        soma = 0                    #Acumulador      
        while cont > 0:                        
            cpf_x = cpf_num % 10        #Pega último digito
            mult = cpf_x * cont         #Multiplica pelo contador
            soma = soma + mult          #Acumula as multiplicações
            cont -= 1                   #Atualiza contador
            cpf_num = cpf_num // 10     #Atualiza cpf
        calc_dig_pri = soma % 11
        if calc_dig_pri == 10:
            calc_dig_pri = 0
        
        #Cálculo do segundo dígito verificador
        cpf_num = cpf // 100        #Elimina dois números do cpf
        if calc_dig_pri == 0:       #Adiciona dígito
            cpf_num = cpf_num * 10
        else:               
            add_dig = calc_dig_pri / 10 
            cpf_num = cpf_num + add_dig 
            cpf_num = cpf_num * 10
        cont = 9                    #Contador
        soma = 0                    #Acumulador     
        while cont >= 0:                
            cpf_y = cpf_num % 10        #Pega último digito
            mult = cpf_y * cont         #Multiplica pelo contador
            soma = soma + mult          #Acumula as multiplicações
            cont -= 1                   #Atualiza contador
            cpf_num = cpf_num // 10     #Atualiza cpf
        calc_dig_seg = soma % 11   
        if calc_dig_seg == 10:
            calc_dig_seg = 0
            
        #Dígitos verificadores digitados
        verify = cpf
        dig_seg = verify % 10       #Segundo dígito verificador
        verify = verify // 10       #Atualiza
        dig_pri = verify % 10       #Primeiro dígito verificador
        
        print("O primeiro dígito verificador deve ser %d" % calc_dig_pri)
        print("O segundo dígito verificador deve ser %d" % calc_dig_seg)
        
        
        #Para imprimir nos moldes do CPF
        cpf_print = cpf                  
        dezena = cpf_print % 100
        cpf_print = cpf_print // 100
        centena = cpf_print % 1000
        cpf_print = cpf_print // 1000
        uni_milhar = cpf_print % 1000
        cpf_print = cpf_print // 1000
        dez_milhar = cpf_print % 1000
        cpf_print = cpf_print // 1000
        
        if calc_dig_pri == dig_pri and calc_dig_seg == dig_seg:
            print ("\nOs dois dígitos verificadores do CPF %03d.%03d.%03d-%02d estão corretos." % (dez_milhar, uni_milhar, centena, dezena))
            
        elif calc_dig_pri != dig_pri and calc_dig_seg != dig_seg:
            print ("\nOs dois dígitos verificadores do CPF %03d.%03d.%03d-%02d estão incorretos." % (dez_milhar, uni_milhar, centena, dezena))
            
        elif calc_dig_pri != dig_pri and calc_dig_seg == dig_seg:
            print ("\nO primeiro dígito verificador do CPF %03d.%03d.%03d-%02d está incorreto." % (dez_milhar, uni_milhar, centena, dezena))
            
        elif calc_dig_pri == dig_pri and calc_dig_seg != dig_seg:
            print ("\nO segundo dígito verificador do CPF %03d.%03d.%03d-%02d está incorreto." % (dez_milhar, uni_milhar, centena, dezena))
                
    #Cartão de crédito   
    if doc == 2:
        print("\nUm número de cartão de crédito deve ser fornecido como um único número inteiro de dezesseis dígitos (ou seja, sem espaços).")
        cartao = int(input("Digite um número de cartão de crédito: "))
        
        #Cálculo do dígito verificador
        card_num = cartao // 10     #Elimina um número do cartão
        cont = 0                    #Contador   
        fora = 2
        soma = 0
        while cont <= 15:                        
            card_x = card_num % 10      #Pega último digito
            mult = card_x * fora        #Multiplicação
            if mult > 9:                #Condição
                mult = mult - 9
                soma = soma + mult      #Acumula as multiplicações
            else:
                soma = soma + mult
            if fora == 2:               #Alternância 2 ou 1
                fora -= 1
            else: 
                fora += 1
            cont += 1                   #Atualiza contador
            card_num = card_num // 10   #Atualiza cartão
        calc_dig = 0
        
        calc_dig = 10 - (soma % 10)
        
        
        #Dígito verificador digitado
        verify = cartao
        dig = verify % 10
        
        print("O dígito verificador deve ser %d" % calc_dig)
        
        #Para imprimir nos moldes do cartão de crédito
        card_print = cartao
        dezena = card_print % 10000
        card_print = card_print // 10000
        centena = card_print % 10000
        card_print = card_print // 10000
        uni_milhar = card_print % 10000
        card_print = card_print // 10000
        dez_milhar = card_print % 10000
        card_print = card_print // 10000
        
        if calc_dig == dig:
            print("\nO dígito verificador do cartão de crédito %04d %04d %04d %04d está correto." % (dez_milhar, uni_milhar, centena, dezena))
            
        else:
            print("\nO dígito verificador do cartão de crédito %04d %04d %04d %04d está incorreto." % (dez_milhar, uni_milhar, centena, dezena))
        
    #Terminar o programa  
    if doc == 0:
        print("Fim!")
     
    
main()
    




