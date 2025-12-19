# Processo Seletivo – Intensivo Maker | AI

Bem-vindo(a) à **etapa prática do processo seletivo para o Intensivo Maker**.

Esta atividade tem como objetivo avaliar competências técnicas relacionadas a **Machine Learning**, **Visão Computacional** e **Otimização de modelos para sistemas embarcados (Edge AI)**, a partir da aplicação prática dos conhecimentos adquiridos nos cursos EAD da etapa anterior.

> 🎯 **Importante:**  
> O foco deste desafio é avaliar sua capacidade de **projetar, treinar e otimizar um modelo de IA**.
---

## 📌 Navegação Rápida

- 🏁 [Passo 0 – Antes de Tudo](#-passo-0-antes-de-tudo)
- ⚙ [Passo 1 – Preparando o Ambiente](#-passo-1-preparando-o-ambiente)
- 💻 [Passo 2 – O Desafio Técnico](#-passo-2-o-desafio-técnico)
  - 🎯 [Conjunto de Dados](#-conjunto-de-dados)
  - 📂 [Estrutura do Projeto](#-estrutura-do-projeto)
  - 📚 [Material de Apoio](#-material-de-apoio)
  - ⚖️ [Critérios de Avaliação](#️-critérios-de-avaliação)
- 📤 [Passo 3 – Instruções de Entrega](#-passo-3-instruções-de-entrega)
  - 📝 [Relatório do Candidato](#-relatório-do-candidato)


---

## 🏁 Passo 0: Antes de Tudo

Caso você **nunca tenha utilizado Git ou GitHub**, não se preocupe.  
Siga atentamente as etapas abaixo.

### 1️⃣ Criação de Conta no GitHub

1. Acesse: https://github.com  
2. Clique em **Sign up**  
3. Crie sua conta gratuita seguindo as instruções da plataforma  

📌 *O GitHub será utilizado para envio, versionamento e correção automática do seu projeto.*



### 2️⃣ Instalação do Git

- **Windows**: https://git-scm.com/downloads  
- **Linux / macOS**:
```bash
git --version
```

---

## ⚙ Passo 1: Preparando o Ambiente

### 1️⃣ Fork do Repositório
Crie um fork deste repositório no seu perfil do GitHub.

### 2️⃣ Clone do Repositório

```bash
git clone https://github.com/SEU_USUARIO/nome-do-repositorio.git
cd nome-do-repositorio
```



### 3️⃣ Preparação do Ambiente de Execução

Você pode executar o projeto de **duas formas**.



## ✅ Opção A – Ambiente Python Local (Recomendado)

Requisitos:
- Python 3.10 ou 3.11
- pip

Instale as dependências:

```bash
pip install -r requirements.txt
```



## 🐳 Opção B – Dev Container (Opcional)

Este repositório inclui um **Dev Container** para facilitar a criação de um ambiente Python padronizado.

📌 Use esta opção apenas se você já estiver familiarizado com VS Code e Docker.

> 💡 O uso do Dev Container é **opcional** e **não faz parte da avaliação**.

---

## 💻 Passo 2: O Desafio Técnico

O desafio consiste em desenvolver um **modelo de Visão Computacional** para **classificação de dígitos manuscritos (MNIST)** e otimizá-lo para **Edge AI**.

Fluxo esperado:

**treinamento → salvamento → conversão → otimização**



### 🎯 Conjunto de Dados

Dataset **MNIST**, disponível diretamente via TensorFlow/Keras.



### ✅ Requisitos Obrigatórios

#### 🧠 Etapa 1 – Treinamento (`train_model.py`)

- Carregar o MNIST
- Criar e treinar uma CNN simples
- Exibir a acurácia final
- Salvar o modelo (`.h5` ou `.keras`)



#### ⚡ Etapa 2 – Otimização (`optimize_model.py`)

- Carregar o modelo treinado
- Converter para **TensorFlow Lite (.tflite)**
- Aplicar técnica de otimização (ex: quantização dinâmica)



#### 📂 Estrutura do Projeto

```plaintext
seu-repositorio/
├── .github/workflows/ci.yml
├── .devcontainer/ (opcional)
├── train_model.py
├── optimize_model.py
├── requirements.txt
├── model.h5
├── model.tflite
└── README.md
```



#### ⚠️ Restrições e Considerações de Engenharia

- Execução apenas em CPU
- CNN simples (até 3 camadas convolucionais)
- Poucas épocas (ex: até 5)
- Código deve rodar sem intervenção manual



## 📤 Passo 3: Instruções de Entrega

```bash
git add .
git commit -m "Entrega do desafio técnico - Seu Nome"
git push origin main
```



## 📝 Relatório do Candidato

O arquivo (`README.md`) deve ser utilizado como **relatório final do desafio**.
Ele será analisado junto com o código enviado neste repositório.

Preencha todas as seções de forma clara e objetiva.

> 💡 Dica: este relatório não precisa ser extenso. O mais importante é
> demonstrar que você compreende as decisões técnicas tomadas ao longo
> do desafio.


### 👤 Identificação

**Nome Completo:**  

### 1️⃣ Resumo da Arquitetura do Modelo

Descreva, em palavras, a arquitetura da **Rede Neural Convolucional (CNN)**
que você implementou no arquivo `train_model.py`.


### 2️⃣ Bibliotecas Utilizadas

Liste as principais bibliotecas utilizadas no projeto, preferencialmente
com suas versões.


### 3️⃣ Técnica de Otimização do Modelo

Explique qual técnica foi utilizada para otimizar o modelo no arquivo
`optimize_model.py`.


### 4️⃣ Resultados Obtidos

Informe o principal resultado obtido após o treinamento do modelo.


### 5️⃣ Comentários Adicionais (Opcional)

Utilize este espaço para comentar:
- Dificuldades encontradas
- Decisões técnicas importantes
- Limitações do modelo
- Aprendizados durante o desafio
