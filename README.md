# 🚀 Desafio Técnico  
## Processo Seletivo – Laboratório Maker | Edge AI

Bem-vindo(a) à **etapa prática do processo seletivo para o Laboratório Intensivo Maker**.

Esta atividade tem como objetivo avaliar competências técnicas relacionadas a **Visão Computacional**, **Machine Learning** e **implantação de modelos em dispositivos embarcados (Edge AI)**, a partir da aplicação prática dos conhecimentos adquiridos nos cursos EAD da etapa anterior.

---

## 📌 Navegação Rápida

- 🏁 Passo 0 – Antes de Tudo  
- 🛠️ Passo 1 – Preparação do Ambiente  
- 💻 Passo 2 – O Desafio Técnico  
- 📂 Estrutura do Projeto  
- 📚 Material de Apoio  
- ⚖️ Critérios de Avaliação  
- 📤 Passo 4 – Instruções de Entrega  
- 📝 Relatório do Candidato  

---

## 🏁 Passo 0: Antes de Tudo

Caso ainda não possua familiaridade com o GitHub, siga **obrigatoriamente** as etapas abaixo.

### 1️⃣ Criação de Conta no GitHub

1. Acesse: https://github.com  
2. Clique em **Sign up**  
3. Siga as instruções para criação de uma conta gratuita  

### 2️⃣ Instalação do Git

- **Windows**: https://git-scm.com/downloads  
- **Linux / macOS**:
```bash
git --version
```

---

## 🛠️ Passo 1: Preparação do Ambiente

### 1️⃣ Fork do Repositório

1. Clique em **Fork** no canto superior direito  
2. Uma cópia será criada no seu perfil  

### 2️⃣ Clone do Repositório

```bash
git clone https://github.com/SEU_USUARIO/nome-do-repositorio.git
cd nome-do-repositorio
```

### 3️⃣ Instalação das Dependências

```bash
pip install -r requirements.txt
```

---

## 💻 Passo 2: O Desafio Técnico

O desafio consiste na classificação de dígitos manuscritos utilizando o dataset **MNIST**, com posterior otimização do modelo para execução em **Edge AI**.

---

## ✅ Requisitos Obrigatórios

### 🧠 Treinamento (`train_model.py`)

- Carregar o MNIST com TensorFlow  
- Construir e treinar uma rede neural  
- Exibir acurácia  
- Salvar o modelo (`.h5` ou `.keras`)  

### ⚡ Otimização (`optimize_model.py`)

- Converter o modelo para **TensorFlow Lite (.tflite)**  
- Aplicar **Dynamic Range Quantization**  

---

## 📂 Estrutura do Projeto

```plaintext
seu-repositorio/
├── .github/workflows/
├── train_model.py
├── optimize_model.py
├── requirements.txt
├── model.h5
├── model.tflite
└── README.md
```

---

## 📚 Material de Apoio

- Fundamentos de IA para Sistemas Embarcados  
- Sistemas de Visão Computacional  
- Otimização de Modelos em Sistemas Embarcados  

---

## ⚖️ Critérios de Avaliação

- Funcionalidade  
- Arquitetura do Modelo  
- Otimização  
- Boas Práticas  
- Uso do Git  

---

## 📤 Passo 4: Instruções de Entrega

```bash
git add .
git commit -m "Entrega do desafio técnico - Seu Nome"
git push origin main
```

---

## 📝 Relatório do Candidato

**Nome Completo:**

### 1️⃣ Resumo da Arquitetura

### 2️⃣ Bibliotecas Utilizadas

### 3️⃣ Técnica de Otimização

### 4️⃣ Resultados Obtidos

### 5️⃣ Comentários Adicionais
