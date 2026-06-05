# Natural Language Database Interaction using LLMs and MCP

## 📌 Project Overview

This project implements a Natural Language Interface for databases using a Large Language Model (LLM). Users can interact with a relational database by typing queries in plain English, and the system automatically converts them into SQL queries, executes them on a MySQL database, and displays the results through a web-based dashboard.

The project demonstrates the integration of LLMs, Flask, MySQL, and Model Context Protocol (MCP) concepts to simplify database interaction.

---

## 🎯 Objective

To enable users to query a database using natural language instead of writing SQL commands manually by leveraging a Large Language Model (LLM) for SQL generation.

---

## 🛠 Technologies Used

* Python
* Flask
* MySQL
* Ollama
* Llama3 / Phi / Gemma Models
* HTML
* CSS
* Jinja2
* MCP (Model Context Protocol)

---

## 🏗 System Architecture

User Query (English)

↓

Flask Backend

↓

LLM (Ollama)

↓

SQL Query Generation

↓

MySQL Database

↓

Query Execution

↓

Results Displayed on Dashboard

---

## 📂 Database Schema

### Categories

| Column        | Type    |
| ------------- | ------- |
| category_id   | INT     |
| category_name | VARCHAR |

### Products

| Column       | Type    |
| ------------ | ------- |
| product_id   | INT     |
| product_name | VARCHAR |
| category_id  | INT     |
| price        | DECIMAL |
| stock        | INT     |

### Customers

| Column        | Type    |
| ------------- | ------- |
| customer_id   | INT     |
| customer_name | VARCHAR |
| city          | VARCHAR |

### Sales

| Column      | Type |
| ----------- | ---- |
| sale_id     | INT  |
| product_id  | INT  |
| customer_id | INT  |
| quantity    | INT  |
| sale_date   | DATE |

---

## ✨ Features

* Natural Language to SQL Conversion
* Local LLM Integration using Ollama
* Dynamic SQL Query Generation
* MySQL Database Connectivity
* Interactive Web Dashboard
* Query Result Visualization
* Safe Query Validation
* MCP-Based Context Injection

---

## 🚀 Installation & Setup

### Clone Repository

```bash
git clone https://github.com/kumar-arman/nl-database-interaction-llm.git
cd nl-database-interaction-llm
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Ollama

Download Ollama from:

https://ollama.com

### Pull Model

```bash
ollama pull llama3
```

or

```bash
ollama pull phi
```

### Start Ollama

```bash
ollama serve
```

### Configure MySQL

Create database:

```sql
CREATE DATABASE mall_db;
```

Import schema and sample data.

### Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## 🧪 Sample Queries

* Show all products
* Show all customers
* Show products with their category names
* Show sales with customer names and product names
* Show total revenue for each product
* Which product generated the highest revenue?
* Show city-wise total revenue
* Show top 3 best-selling products

---

## 🔐 Security Measures

* Allows only SELECT queries
* Blocks DELETE, DROP, UPDATE, INSERT operations
* Cleans markdown output from LLM responses
* Validates generated SQL before execution

---

## ⚠ Limitations

* Accuracy depends on LLM performance
* Ambiguous queries may generate incorrect SQL
* Requires schema context for accurate results
* Local model requires sufficient system resources

---

## 🔮 Future Enhancements

* Support for MongoDB
* Role-Based Access Control
* Query History
* Advanced Analytics Dashboard
* Fine-Tuned SQL Generation Model
* Voice-Based Query Input

---

## 📚 Academic Context

Developed as part of Advanced Development Lab – Experiment 5:

**Natural Language Database Interaction with LLMs and MCP**

---

## 👨‍💻 Author

**Arman Kumar Singh**

B.Tech – Electronics and Computer Science Engineering (ECS)

Kalinga Institute of Industrial Technology (KIIT)
