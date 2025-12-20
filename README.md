# 🔬 Trabalho Prático: Algoritmos de Aprendizagem e Otimização (IA – 2025/2)

[![Instituição][cefet-badge]][cefet-url]
[![IDE][vscode-badge]][vscode-url]
[![Linguagem][python-badge]][python-url]

**Disciplina:** G05IART0.02 – Inteligência Artificial  
**Instituição:** CEFET-MG – Campus Divinópolis  
**Professor:** Tiago Alves de Oliveira  
**Autores:** Bruno Prado Dos Santos, João Francisco Teles da Silva

---

## 🎯 Objetivo do Projeto

Este trabalho tem como objetivo compreender, implementar e comparar diferentes paradigmas clássicos de Inteligência Artificial e Computação Natural, aplicados a problemas reais e combinatórios.

São abordadas técnicas que vão desde sistemas simbólicos manuais, passando por aprendizado de máquina supervisionado, até metaheurísticas populacionais, com foco em desempenho, custo computacional, capacidade de generalização e comportamento de convergência.

---

## 🧠 Visão geral do funcionamento

O projeto é modular e não possui um único arquivo `main.py` central, mas sim scripts específicos para cada paradigma de IA localizados na pasta `src/`. O fluxo geral de funcionamento segue a lógica abaixo:

1. **Definição e Carregamento do Problema:**
   - **Parte 1:** Solicita input direto do usuário via terminal para percorrer a árvore;
   - **Parte 2:** Lê o dataset bruto `cleveland.csv` (pasta `data/raw/`) e o processa, gerando arquivos de treino e teste em `data/processed/`;
   - **Partes 3 e 4:** Gera ou carrega a instância do problema de otimização (TSP com 20 cidades) definido matematicamente em `problems/tsp.py`.

2. **Execução dos Algoritmos:**
   - Ao rodar os scripts específicos (ex: `train_knn.py`, `run_ga.py`), o sistema executa o algoritmo correspondente: **Árvore de Decisão Manual**, Classificadores (**KNN, SVM, Árvore Scikit**), **Algoritmo Genético (GA)**, **Colônia de Formigas (ACO)** ou **Seleção Clonal (CLONALG)**.

3. **Coleta de Métricas:**
   - O sistema mede e coleta dados específicos para cada execução:
     - **ML:** Acurácia, Precisão, Recall e F1-Score;
     - **Otimização:** Melhor Fitness (Distância/Custo), Custo Computacional (tempo) e Histórico de Convergência (evolução por iteração).

4. **Geração de Resultados:**
   - Exibe um sumário no terminal com os resultados finais;
   - Salva **arquivos de métricas** (JSON) em `data/processed/`;
   - Gera e salva **gráficos comparativos** no diretório `reports/figs/` (ex: `graficoga.png`, `plot_comparision.png`, `comparison_part4.png`).

> Observação: por design, cada parte deve ser executada separadamente (ou via comandos agrupados no `Makefile`/`run.sh`). Se você quiser comparar parâmetros diferentes (ex: variar a população do GA), basta passar os argumentos via CLI (ex: `--iters 1000 --seed 42`) conforme implementado nos scripts de execução.

---

## 📥 Clone do Projeto

Para começar, clone este repositório para a sua máquina local usando o seguinte comando no seu terminal:

```bash
#usando HTTPS
git clone https://github.com/joaofranciscoteles/Algoritmos-de-Aprendizagem---IA.git

#usando SSH
git clone git@github.com:joaofranciscoteles/Algoritmos-de-Aprendizagem---IA.git
```

---

## 🚀 Requisitos

Para executar este projeto, você precisará do **Python 3.10** (ou superior) e das seguintes bibliotecas:

* **NumPy** (Cálculos matemáticos e matriciais)
* **Pandas** (Manipulação de dados e leitura de CSVs)
* **Matplotlib** (Geração de gráficos)
* **Scikit-learn** (Algoritmos de Machine Learning: KNN, SVM, Árvores)

---

## ⚙️ Instalação das Dependências

###  Instalação Manual (via Pip)

Você deve instalar a biblioteca manualmente usando o `pip` (gerenciador de pacotes do Python):

```bash
pip install -r requirements.txt
```

## 📂 Detalhes do Projeto

### Estrutura de Pastas

``` Markdown
Trabalho1/
├── data/
│   ├── labirinto.txt
│   ├── labirinto1.txt
|   └── labirinto3.txt
│
├── src/
│   ├── main.py
│   ├── astar.py
│   ├── bfs.py
│   ├── dfs.py
│   ├── gbfs.py
│   └── maze_utils.py
│
├── resultados/
│   ├── comparativo_heuristicas/
|   |    ├── custo_caminho.png
|   |    ├── memoria_maxima.png
|   |    ├── nos_expandidos.png
|   |    ├── tempo_execucao.png
│   ├── geral/
|   |    ├── custo_caminho.png
|   |    ├── memoria_maxima.png
|   |    ├── nos_expandidos.png
|   |    ├── tempo_execucao.png
|
├── .gitignore
├── trabalho1__BrunoPrado_JoãoFrancisco_.pdf
├── README.md 
└── requirements.txt


```
---

## 🧩 Estrutura do Trabalho

1. **Parte 1 — Sistemas Simbólicos**  
   Implementação manual de uma Árvore de Decisão binária (sistema especialista), sem uso de bibliotecas de ML.

2. **Parte 2 — Aprendizado Supervisionado**  
   Comparação entre KNN, SVM e Árvore de Decisão utilizando Scikit-Learn.

3. **Parte 3 — Computação Evolutiva**  
   Algoritmo Genético (GA) aplicado ao Problema do Caixeiro Viajante (TSP).

4. **Parte 4 — Enxame e Sistemas Imunes**  
   Estudo comparativo entre ACO e CLONALG aplicados ao TSP.

---

## ⚙️ Como Reproduzir

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .\.venv\Scripts\activate  # Windows

pip install -r requirements.txt
```

### Parte 1 — Árvore de Decisão Manual
```bash
python src/part1_tree_manual/tree_manual.py
```

Diagrama da árvore (Mermaid):  
`src/part1_tree_manual/tree_diagram.md`

---

### Parte 2 — Machine Learning (Classificação)

Pré-processamento:
```bash
python src/part2_ml/preprocess.py
```

Treinamento:
```bash
python src/part2_ml/train_knn.py
python src/part2_ml/train_svm.py
python src/part2_ml/train_tree.py
```

Gráficos comparativos:
```bash
python src/part2_ml/plot_comparison.py
```

Resultados:  
`reports/figs/plot_comparison.png`

---

### Parte 3 — Algoritmo Genético (TSP)

Execução padrão:
```bash
python src/part3_ga/run_ga.py --iters 2000
```

Execução reprodutível:
```bash
python src/part3_ga/run_ga.py --iters 2000 --seed 42
```

Resultado:  
`reports/figs/grafico_ga.png`

---

### Parte 4 — Enxame e Sistemas Imunes

```bash
python src/part4_swarm_immune/run_meta.py --iters 300
```

Execução estatística:
```bash
python src/part4_swarm_immune/run_meta.py --iters 1000 --seed 123
```

Resultado:  
`reports/figs/comparison_part4.png`

---

## 📊 Discussão dos Resultados (Resumo)

> ⚠️ **Seção parcial – discussão final será ajustada após consolidação dos resultados**

- **Machine Learning:** KNN apresentou melhor desempenho médio (≈86% de acurácia).  
- **GA:** Redução superior a 70% no custo da rota em relação à solução inicial aleatória.  
- **ACO vs CLONALG:** ACO converge rapidamente; CLONALG apresenta maior robustez em execuções longas.

---

## ⚙️ Decisões Técnicas

> ⚠️ **Alguns parâmetros ainda precisam ser confirmados**

- **Dataset:** Cleveland Heart Disease – UCI Repository (**link exato pendente**)  
- **Tarefa:** Classificação  
- **Pré-processamento:** limpeza, imputação, one-hot encoding, normalização  
- **Validação:** Hold-out + K-Fold (**valor de K pendente**)  
- **Métricas:** Acurácia, Precisão, Revocação, F1-score (macro)  
- **Sementes:** definidas em `src/common/seeds.py`

---

## 📦 Dependências Principais

- numpy  
- pandas  
- matplotlib  
- seaborn  
- scikit-learn  

---

## 👨‍💻 Autores

Trabalho desenvolvido em dupla pelos seguintes alunos:

<div align="center">
    
**Bruno Prado Dos Santos**
<br>
*Estudante de Engenharia de Computação @ CEFET-MG*
<br><br>
[![Gmail][gmail-badge]][gmail-bruno]


<br><br>

**João Francisco Teles da Silva**
<br>
*Estudante de Engenharia de Computação @ CEFET-MG*
<br><br>
[![Gmail][gmail-badge]][gmail-joao]


</div>

[cefet-badge]: https://img.shields.io/badge/CEFET--MG-Campus%20V-blue?logo=academia
[cefet-url]: https://www.cefetmg.br/
[vscode-badge]: https://img.shields.io/badge/VSCode-1.86-blue?logo=visualstudiocode
[vscode-url]: https://code.visualstudio.com/
[python-badge]: https://img.shields.io/badge/Python-3.10-yellow?logo=python
[python-url]: https://www.python.org/

[gmail-badge]: https://img.shields.io/badge/-Gmail-D14836?style=for-the-badge&logo=Gmail&logoColor=white

[gmail-bruno]: mailto:bruno.santos@aluno.cefetmg.br


[gmail-joao]: 

