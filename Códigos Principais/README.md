# 🧠 Atividade de Participação — Estruturas de Dados

### Universidade Federal do Piauí (UFPI) – CCN – Departamento de Computação

📅 **Período:** 2025.2
📚 **Disciplina:** Estruturas de Dados
🧑‍🏫 **Professor:** Raimundo Santos Moura

---

## 📋 Descrição da Atividade

Esta atividade tem como objetivo **analisar o comportamento de funções hash** aplicadas a nomes de alunos, avaliando colisões e dispersão em diferentes configurações de tabelas hash.

O trabalho envolve:

* Implementação de uma classe `HashTable` em Python.
* Testes com diferentes **funções hash** e **tamanhos de tabela (M)**.
* Construção de **histogramas** mostrando colisões.
* Comparação entre resultados para valores **primos e não primos** de M.
* Elaboração de um **relatório técnico** e um **vídeo curto (até 3 minutos)** explicando o funcionamento da solução.

---

## ⚙️ Experimentos Solicitados

### 🧪 Questão 1

* Usar **M = 26**.
* Utilizar **a primeira letra** do nome como função hashing.
* Gerar um **histograma** mostrando quais letras geram mais ou menos colisões.

### 🧪 Questão 2

* Repetir o experimento com **a função hash padrão do Python (`hash()`)**.
* Comparar os resultados e identificar colisões.

### 🧪 Questão 3

* Repetir os experimentos com o arquivo `alunosED2025.txt`.
* Testar a função hash discutida em sala para os valores de **M = 17, 43 e 97**.
* Determinar qual valor de M espalha melhor os nomes.

### 🧪 Questão 4

* Testar novamente com **M = 16, 40 e 100** (números pares).
* Comparar com os resultados anteriores e analisar se **usar número primo** realmente melhora a distribuição.

---

## 📊 Resultados Esperados

* Histogramas mostrando a **distribuição de chaves** (letras ou nomes).
* Contagem de **colisões** para cada função hash.
* Gráficos ou tabelas comparando os diferentes valores de M.
* Discussão sobre a influência de **números primos** na eficiência da tabela hash.

---
