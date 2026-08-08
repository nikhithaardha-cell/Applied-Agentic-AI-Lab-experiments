# Lab 2 – RAG-Based Question Answering System

## Aim

To implement a Retrieval-Augmented Generation (RAG) based Question Answering System that retrieves relevant information from a knowledge base and generates an appropriate answer.

## Objective

The objective of this experiment is to understand the basic RAG pipeline, including document preparation, indexing, retrieval, and answer generation.

## Description

Retrieval-Augmented Generation (RAG) combines information retrieval with language generation. Instead of generating an answer only from the model's existing knowledge, the system first retrieves relevant information from a collection of documents and uses that information to generate the answer.

## RAG Workflow

Documents
↓
Document Processing
↓
Indexing
↓
User Question
↓
Information Retrieval
↓
Relevant Documents
↓
Answer Generation
↓
Final Answer

## Technologies Used

- Python
- Scikit-learn
- TF-IDF
- Natural Language Processing
- Information Retrieval
- RAG Concepts

## Knowledge Base

The system uses a collection of text documents containing information related to topics such as:

- Artificial Intelligence
- Prompt Engineering
- Cybersecurity
- Agentic AI
- Large Language Models

## Example

### Input

```text
What is cyber security?
