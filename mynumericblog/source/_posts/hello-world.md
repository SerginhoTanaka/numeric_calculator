---
title: Dashboard de Cálculo Numérico
date: 2024-06-10
---


## Introdução

Este dashboard apresenta conceitos fundamentais de Cálculo Numérico, incluindo interpolação e regressão linear simples. Utilize os links abaixo para explorar mais sobre cada tópico.

---

## Interpolação

### O que é Interpolação?

A interpolação é uma técnica de estimativa de valores desconhecidos entre dois pontos conhecidos em um conjunto de dados. O objetivo é construir novos pontos dentro da faixa de um conjunto discreto de pontos conhecidos. Existem vários métodos de interpolação, incluindo:

- **Interpolação Linear:** Utiliza uma linha reta para estimar valores entre dois pontos conhecidos.
- **Interpolação Polinomial:** Utiliza um polinômio de grau n para passar exatamente pelos n+1 pontos conhecidos.

#### Exemplo de Interpolação Linear

Dado dois pontos (x1, y1) e (x2, y2), a interpolação linear estima o valor y para um ponto x utilizando a fórmula:

\[ y = y1 + \frac{(y2 - y1)}{(x2 - x1)} \cdot (x - x1) \]

---

## Regressão Linear Simples

### O que é Regressão Linear Simples?

A regressão linear simples é uma técnica estatística usada para modelar a relação entre uma variável dependente e uma variável independente. O objetivo é ajustar uma linha reta que minimiza a soma dos quadrados das diferenças entre os valores observados e os valores previstos.

#### Fórmula da Regressão Linear

A fórmula da regressão linear simples é:

\[ y = a + bx \]

onde:
- \( y \) é a variável dependente.
- \( x \) é a variável independente.
- \( a \) é o intercepto da regressão.
- \( b \) é o coeficiente de inclinação.

### Exemplo de Cálculo

Dado um conjunto de dados, os valores de \( a \) e \( b \) podem ser determinados usando os mínimos quadrados:

\[ b = \frac{\sum{(x_i - \bar{x})(y_i - \bar{y})}}{\sum{(x_i - \bar{x})^2}} \]
\[ a = \bar{y} - b\bar{x} \]

onde \( \bar{x} \) e \( \bar{y} \) são as médias de \( x \) e \( y \), respectivamente.

---

## Recursos Adicionais

Para saber mais sobre esses tópicos, visite os seguintes links:


- [Link do meu código](https://replit.com/@SerginhoTanaka/calculo-numerico)


---

## Conclusão

Este dashboard fornece uma visão geral básica de dois métodos importantes em cálculo numérico. Utilize os links fornecidos para aprofundar seu entendimento sobre interpolação e regressão linear simples.

---

