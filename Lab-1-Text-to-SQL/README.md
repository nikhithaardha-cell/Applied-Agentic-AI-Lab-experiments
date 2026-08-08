# Lab 1 – Text-to-SQL Workflow

## Aim

To build an end-to-end Text-to-SQL workflow that converts natural language questions into SQL queries and retrieves the required information from a database.

## Objective

To understand how natural language questions can be converted into SQL queries and executed on a database.

## Description

Text-to-SQL converts a user's natural language question into an SQL query. The generated query is executed on a database and the required results are displayed.

## Workflow

User Question
↓
Natural Language Understanding
↓
SQL Query Generation
↓
SQL Query Execution
↓
Database Result
↓
Display Answer

## Technologies Used

- Python
- SQLite
- SQL

## Example

### Input

Show all students

### SQL Query

```sql
SELECT * FROM students;
