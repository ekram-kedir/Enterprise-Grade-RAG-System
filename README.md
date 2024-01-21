# Enterprise-Grade-RAG-System

Welcome to the Enterprise-Grade RAG (Ranking and Generation) System, an innovative solution for optimizing Language Models (LLMs) across various industries.


## RAG System - Overview

The RAG (Ranking and Generation) system is a key component of language model optimization services. It comprises the following services:

### 1. Automatic Prompt Generation Service

Streamlining the process of creating effective prompts, this service enables businesses to efficiently utilize LLMs for generating high-quality, relevant content. It significantly reduces the time and expertise required in crafting prompts manually.

### 2. Automatic Evaluation Data Generation Service

RAG's service automates the generation of diverse test cases, ensuring comprehensive coverage and identifying potential issues. This enhances the reliability and performance of LLM applications, saving significant time in the Quality Assurance (QA) process.

### 3. Prompt Testing and Ranking Service

RAG's service evaluates and ranks different prompts based on effectiveness, helping users achieve the desired outcome from LLM. It ensures that chatbots and virtual assistants provide accurate, contextually relevant responses, thereby improving user engagement and satisfaction.

## Getting Started

This repository serves as the root system for the Enterprise-Grade RAG System. It includes subfolders for the frontend, backend, and RAG (Prompt Engineering and Evaluation Metrics).

### Subfolders

- [Frontend] - Next.js project for the user interface.
- [Backend] - Flask application for backend services.


Refer to individual subfolders READMEs for specific setup and usage instructions.

## Learn More

For more detailed information and resources, refer to the Readme in each subfolder.

### Contents

- [Setup](#setup)
- [Installation](#installation)

# Setup

1. Clone this repository:

```sh
git clone git@github.com:abel-blue/prompt-evaluation.git
cd prompt-evaluation
```

2. Setup environment variables on `.env`:

(create .env file in the root directory)

```bash
#################
# Development env
#################

OPENAI_API_KEY=""
VECTORDB_MODEL="gpt-3.5-turbo"
```


# Installation

**Run**

```bash
# create virtual environment
python3 -m venv venv

# activate
source venv/bin/activate

# install requirements
pip install -r requirements.txt

# to generate test data
make data_generate

# to evaluate user input data (prob., accur., confid.)
make data_evaluate
```

## Deploy

Follow deployment instructions provided in each subfolder's README resources for both frontend and backend.

Thank you for choosing Enterprise-Grade RAG System!

