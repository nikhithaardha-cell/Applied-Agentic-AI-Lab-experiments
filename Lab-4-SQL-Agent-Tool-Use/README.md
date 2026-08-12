# Lab 4 – SQL Agent with Tool Use

## Title

SQL Agent with Tool Use

## Aim

To develop a ReAct-based SQL Agent using database tools to understand user questions, execute SQL queries, and provide the required results.

## Objectives

- To understand the ReAct agent approach.
- To create tools for database operations.
- To execute SQL queries using database tools.
- To retrieve information from an SQLite database.
- To generate the required final answer.

## Description

A SQL Agent with Tool Use is an agent that interacts with a database using predefined tools. The agent analyzes the user's question, selects an appropriate tool, performs the database operation, observes the result, and provides the final answer.

The experiment follows the ReAct pattern:

**Thought → Action → Observation → Final Answer**

## ReAct Workflow

```text
User Question
      ↓
     Agent
      ↓
    Thought
      ↓
    Action
      ↓
 Database Tool
      ↓
  Observation
      ↓
    Thought
      ↓
    Action
      ↓
 Final Answer
