# Trabalho Prático: Algoritmos de Aprendizagem e Otimização

**Disciplina:** Inteligência Artificial - 2025/2  
**Instituição:** CEFET-MG  
**Autores:** [Seu Nome], [Nome do Dupla]

---

## 📋 Sobre o Projeto

Este projeto implementa e analisa comparativamente diferentes paradigmas de Inteligência Artificial, abrangendo desde sistemas simbólicos manuais até metaheurísticas avançadas de inteligência de enxame e sistemas imunológicos artificiais. O objetivo é demonstrar a aplicação prática, a análise estatística e o custo computacional de cada abordagem.

O trabalho está dividido em quatro partes fundamentais:
1.  **Sistemas Simbólicos:** Árvore de Decisão Manual (Sistema Especialista).
2.  **Machine Learning Supervisionado:** Comparativo entre KNN, SVM e Árvores de Decisão (Scikit-Learn).
3.  **Computação Evolutiva:** Algoritmo Genético (GA) aplicado ao TSP (20 cidades).
4.  **Inteligência de Enxame e Imunes:** Comparativo entre ACO e CLONALG no TSP.

---

## 🛠️ Instalação e Configuração

O projeto foi desenvolvido em Python 3.10+. Para garantir a reprodutibilidade e isolamento das dependências, siga os passos abaixo:

### 1. Configurar Ambiente Virtual

Linux/Mac:
python -m venv venv
source venv/bin/activate

Windows:
python -m venv venv
.\venv\Scripts\activate

### 2. Instalar Dependências
pip install -r requirements.txt

---

## 🚀 Execução e Análises

Cada parte do projeto foi estruturada para ser executada de forma independente. Abaixo estão os comandos para reproduzir os experimentos.

### Parte 1: Árvore de Decisão Manual
Um sistema de recomendação de filmes baseado em regras "hardcoded", demonstrando a lógica de ramificação binária sem aprendizado de máquina.

Comando:
python src/part1_tree_manual/tree_manual.py

Artefatos:
- Diagrama da árvore disponível em: src/part1_tree_manual/tree_diagram.md

---

### Parte 2: Machine Learning (Classificação)
Pipeline completo de classificação utilizando o dataset "Cleveland Heart Disease". Inclui pré-processamento, validação cruzada (K-Fold) e análise de métricas.

1. Pré-processamento (Limpeza, One-Hot Encoding, Normalização):
python src/part2_ml/preprocess.py

2. Treinamento e Avaliação (Gera métricas JSON e gráficos de performance):
python src/part2_ml/train_knn.py
python src/part2_ml/train_svm.py
python src/part2_ml/train_tree.py

3. Gerar Relatório Visual Comparativo:
python src/part2_ml/plot_comparision.py

Resultados gerados em: reports/figs/plot_comparision.png

---

### Parte 3: Algoritmo Genético (TSP)
Solução para o Problema do Caixeiro Viajante (TSP) com 20 cidades ($2.4 \times 10^{18}$ permutações). O algoritmo utiliza representação por permutação, Crossover OX1 e Mutação Swap.

Execução padrão (2000 gerações):
python src/part3_ga/run_ga.py

Execução com semente fixa para reprodutibilidade:
python src/part3_ga/run_ga.py --seed 42

Resultados gerados em: reports/figs/graficoga.png

---

### Parte 4: Enxame e Sistemas Imunes (Comparativo)
Estudo comparativo de convergência entre Ant Colony Optimization (ACO) e Clonal Selection Algorithm (CLONALG) no mesmo cenário TSP da Parte 3.

Execução padrão (300 iterações):
python src/part4_swarm_immune/run_meta.py --iters 300

Execução robusta para análise estatística:
python src/part4_swarm_immune/run_meta.py --iters 1000 --seed 123

Resultados gerados em: reports/figs/comparison_part4.png

---

## 📊 Principais Resultados e Discussão

### Machine Learning
O modelo KNN obteve a melhor consistência nas métricas de teste (Acurácia ~86%), superando o SVM e a Árvore de Decisão. A análise sugere que a fronteira de decisão dos dados cardíacos possui alta não-linearidade local, favorecendo métodos baseados em vizinhança.

### Computação Evolutiva (GA)
Para um espaço de busca de 20 cidades, o GA foi capaz de convergir para soluções de alta qualidade em menos de 1 segundo, reduzindo a distância total de rota inicial (aleatória) em mais de 70%. O uso de matriz de distâncias pré-calculada foi essencial para o desempenho.

### Enxame (ACO) vs Imunes (CLONALG)
- **ACO:** Demonstrou convergência inicial extremamente rápida devido à heurística gulosa combinada com feromônios, ideal para encontrar boas soluções em pouco tempo.
- **CLONALG:** Apresentou uma evolução mais gradual, mas sustentada. Sua mecânica de hipermutação permitiu escapar de ótimos locais onde o ACO tendia a estagnar em execuções longas.

---

## 📦 Dependências

As principais bibliotecas utilizadas são:
- numpy: Cálculos vetoriais e matriciais.
- pandas: Manipulação de dados estruturados (CSV).
- matplotlib & seaborn: Visualização de dados e plotagem de gráficos.
- scikit-learn: Implementação dos modelos de ML (KNN, SVM, Tree).
- argparse: Interface de linha de comando para reprodutibilidade.

Para instalar todas:
pip install numpy pandas matplotlib seaborn scikit-learn

---

## ✒️ Autores

- [Seu Nome]
- [Nome do Parceiro]
