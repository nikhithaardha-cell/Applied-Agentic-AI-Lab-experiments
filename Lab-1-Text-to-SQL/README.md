# Lab 1 – Text-to-SQL Workflow

## Aim

To build an end-to-end Text-to-SQL workflow that converts natural language questions into SQL queries and retrieves the required information from a database.

## Objective

The main objective of this experiment is to understand how natural language questions can be converted into SQL queries and executed on a database.

## Description

Text-to-SQL is a technique that converts a user's natural language question into a structured SQL query. The generated SQL query is executed on a database, and the retrieved results are displayed to the user.

## Workflow

User Question
↓
Understand Natural Language
↓
Generate SQL Query
↓
Execute SQL Query
↓
Retrieve Database Results
↓
Display Answer

## Technologies Used

- Python
- SQLite
- SQL

## Database

The experiment uses an SQLite database named:

`college.db`

A `students` table is created to store student information.

## Example

### Input

```text
Show all students
