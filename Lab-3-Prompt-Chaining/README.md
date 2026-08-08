# Lab 3 – Prompt Chaining for Summarization

## Aim

To implement a multi-step prompt chaining workflow for summarizing input text using sequential processing steps.

## Objective

The objective of this experiment is to understand prompt chaining and how a complex task can be divided into multiple smaller steps.

## Description

Prompt chaining is a technique where the output of one prompt is passed as the input to the next prompt. Instead of completing the entire task using one prompt, the task is divided into multiple stages.

In this experiment, the input text is processed through multiple stages to generate a final summary.

## Workflow

Input Text
↓
Prompt 1: Extract Key Points
↓
Prompt 2: Organize Key Points
↓
Prompt 3: Generate Summary
↓
Final Summary

## Technologies Used

- Python
- Prompt Engineering
- Natural Language Processing
- Artificial Intelligence
- Agentic AI Concepts

## Process

### Step 1 – Input Text

The user provides a text document or paragraph.

### Step 2 – Extract Key Points

The first prompt identifies the important points from the input text.

### Step 3 – Organize Information

The extracted points are organized into a clear and structured format.

### Step 4 – Generate Summary

The final prompt uses the organized information to generate a concise summary.

## Example

### Input

```text
Artificial Intelligence is a field of computer science that focuses
on developing systems capable of performing tasks that normally
require human intelligence.
