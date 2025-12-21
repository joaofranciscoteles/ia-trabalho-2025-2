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
├── data/              
├── reports/
│   └── figs/          
├── src/
│   ├── part1_tree_manual/
│   │   ├── tree_diagram.md
│   │   └── tree_manual.py
│   ├── part2_ml/
│   │   ├── plot_comparision.py
│   │   ├── preprocess.py
│   │   ├── train_knn.py
│   │   ├── train_svm.py
│   │   ├── train_tree.py
│   │   └── utils.py
│   ├── part3_ga/
│   │   ├── problems/
│   │   │   └── tsp.py
│   │   ├── ga.py
│   │   └── run_ga.py
│   └── part4_swarm_immune/
│   │   ├── aco.py
│   │   ├── clonalg.py
│   │   └── run_meta.py
├── README.md
├── .gitignore
├── Trabalho_Algoritmos_de_Aprendizado_IA.pdf
└── requirements.txt

```
## ▶️ Execução

Certifique-se de estar na raiz do projeto (pasta `ia-trabalho-2025-2`) e com o ambiente virtual ativado. Cada parte do trabalho funciona de maneira independente.

### 1. Árvore de Decisão Manual
Executa o sistema especialista interativo para recomendação de filmes.
```bash
python src/part1_tree_manual/tree_manual.py
```

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
python src/part3_ga/run_ga.py
```

Resultado:  
`reports/figs/grafico_ga.png`

---

### Parte 4 — Enxame e Sistemas Imunes

Execução padrão:
```bash
python src/part4_swarm_immune/run_meta.py
```

Resultado:  
`reports/figs/comparison_part4.png`

---

## ⚙️ Decisões Técnicas

- **Dataset:** Cleveland Heart Disease Dataset, proveniente do UCI Machine Learning Repository.
- **Formulação do problema:** classificação binária, considerando ausência de doença cardíaca (classe 0) e presença de doença (classe 1).
- **Pré-processamento:** remoção de amostras com valores ausentes, conversão de tipos, binarização da variável alvo e codificação one-hot das variáveis categóricas.
- **Normalização:** aplicada apenas nos algoritmos sensíveis à escala (KNN e SVM), por meio do StandardScaler.
- **Validação:** divisão hold-out estratificada (70% treino / 30% teste) e validação cruzada estratificada (5-fold) para seleção de hiperparâmetros.
- **Seleção de hiperparâmetros:**
  - KNN: escolha do parâmetro K via validação cruzada (K = 25);
  - SVM: avaliação de kernels linear e RBF, com seleção de C e gamma;
  - Árvore de Decisão: controle de complexidade por meio da profundidade máxima (max\_depth = 9).
- **Métricas de avaliação:** acurácia, precisão, recall e F1-score, utilizando média macro para lidar com possível desbalanceamento entre classes.
- **Reprodutibilidade:** uso de sementes fixas (`random_state=42`) e parâmetros explícitos nos scripts de execução.

---

## 💻 Máquinas de Teste

Para testagem do projeto, foram utilizadas 2 máquinas que rodaram o cógido em sistema operacional Linux (Ubuntu).

| Máquina | Processador            | Memória RAM | Sistema Operacional |
|------------------|------------------------|-------------|---------------------|
| ACER NITRO 5 |Intel(R) Core(TM) i5-12450H    | 16 GB       | Windows 10     |
| Acer Aspire A515-54    | Intel(R) Core(TM) i5-10210U    | 8 GB        | Windows 11       |


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

[gmail-joao]: mailto:joaoteles0505@gmail.com








