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

  Nome: Patricia 
  Número USP: 
  Curso: Estatística                     Turma: 48
  Exercício-Programa 03

  Referências: Com exceção das rotinas que podem ser fornecidas
  no enunciado ou em sala de aula, caso você tenha utilizado
  alguma referência, liste-as abaixo para que o seu programa não
  seja considerado plágio ou irregular.
  
  Exemplo:
  - O algoritmo de ordenação Quicksort foi baseado em
  http://www.ime.usp.br/~pf/algoritmos/aulas/quick.html

"""
import math
import random

def main():
    task = input("Digite o código de uma tarefa('t' ou 'm' ou '-'): ")
    a = 0.0
    b = 1.0
    M = 1.0
    while task != '-':
        if task == 't':
            action = int(input("Digite o número de trapézios: "))
            print("\n")
            print("Tarefa : Valor aproximado de PI pelo método dos trapézios")
            print("Número de trapézios = ", action)
            delta_x = 1 / action
            print ("Deltax = ", delta_x)
            Pi = metodo_trapezios(a,b,action) 
            print("Pi = ", Pi)
            print("\n")
            
        
        elif task == 'm':
            action = int(input("Digite uma semente para o gerador de números pseudo-aleatórios: "))
            random.seed(action)
            repete = int(input("Digite o número de repetições para o cálculo da área: "))
            points = int(input("Digite o número de pontos a serem gerados: "))
            print("\n")
            print("Tarefa : Valor aproximado de PI pelo método de Monte Carlo")
            print("Semente = ", action)
            print("Número de repetições = ", repete)
            print("Número de pontos = ", points)
            quad, soma = [], 0
            for i in range (repete):
                Pi = metodo_monte_carlo(0.0,1.0, M, points)
                quad.append(Pi)
            for i in range (len(quad)):
                soma += quad[i]
            media = soma / repete     
            print("Pi = ", media)
            print("\n")
             
        task = input("Digite o código de uma tarefa('t' ou 'm' ou '-'): ")
    
def f(x):
    """ (float) -> float
    Recebe um número real x e se (1.0-x*x) for positivo, retorna uma aproximação
    para a raiz quadrada de (1.0-x*x); em caso contrário, retorna 0.
    Obs.: para determinar a raiz quadrada ´e utilizada a função sqrt do módulo math.
    """
    if x >= 0:
        fun = math.sqrt(1.0 - x*x)   #área de pi
        return fun
    else:
        return 0
    
def metodo_trapezios(a, b, k):
    """ (float, float, int) -> float
    Recebe dois números reais a e b, com a < b, e um inteiro positivo k.
    Esta função retorna um valor aproximado para a área sob a função f(x), no intervalo
    [a, b], calculada pelo método dos trapézios, utilizando k trapézios.
    """  
    delta_x = (b - a) / k
    soma = 0
    A = 0
    for i in range (0, k):
        soma = soma + f(a + i * delta_x) + f(a + (i + 1) * delta_x)
        A = soma * delta_x / 2
    Area = 4 * A
    return Area
   
def gera_coordenadas_ponto(a, b, M):
    """ (float, float, float) -> float, float
    Recebe dois números reais a e b, com a < b, e um número real positivo M.
    Esta função retorna as coordenadas reais x e y de um ponto gerado no retângulo
    [a, b] x [0, M].
    Obs.: para gerar um número real é utilizada a função uniform do módulo random.
    """
    #gera um número real aleatório no intervalo
    xi = random.uniform(a, b)    
    yi = random.uniform(0, M)
    return (xi, yi)
    
def metodo_monte_carlo(a, b, M, n):
    """ (float, float, float, int) -> float
    Recebe dois números reais a e b, com a < b; um número real positivo M
    tal que f(x) <= M, para todo x em [a, b]; e um inteiro positivo n.
    Esta função retorna um valor aproximado para a área sob a função f(x), no
    intervalo [a, b], utilizando o método de Monte Carlo, gerando as
    coordenadas reais de n pontos no retângulo [a, b] x [0, M].
    Para isso, utiliza a função gera_coordenadas_ponto.
    """
    i = 0
    dentro = 0
    
    while i <= n:
        x,y = gera_coordenadas_ponto(0.0, 1.0, 1.0)
        #chama f(x)
        if y <= f(x):
            dentro += 1       
        i += 1     
        #else: ponto caiu fora da área
    P = dentro/n
    A = P * (b - a) * M
    Area = 4 * A
    return Area
    
    
main()



