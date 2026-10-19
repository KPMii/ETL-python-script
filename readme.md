# Basic ETL Pipeline

<p align="center">
  <b>Fake Store API → Python → PostgreSQL</b>
  <br />
  Learning the fundamentals of data engineering through a simple ETL pipeline.
  <br /><br />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white" />
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" />
</p>

---

## Overview

This project is my introduction to **ETL (Extract, Transform, Load)** using Python.

It retrieves product data from the [Fake Store API](https://fakestoreapi.com/products), processes it with Pandas, and loads the results into a PostgreSQL database using SQLAlchemy and Psycopg. I then verify the stored records using pgAdmin 4.

## ETL Workflow

| Stage | Process | Tool |
|---|---|---|
| **01 — Extract** | Fetch product data from the REST API | Requests |
| **02 — Transform** | Convert JSON into a DataFrame and clean the data | Pandas |
| **03 — Load** | Insert transformed records into PostgreSQL | SQLAlchemy + Psycopg |
| **04 — Verify** | Inspect the stored data | pgAdmin 4 |

## Tech Stack

- **Python** — Pipeline logic
- **Requests** — HTTP requests and API data retrieval
- **Pandas** — Data manipulation and transformation
- **SQLAlchemy** — Database engine and SQL interaction
- **Psycopg** — PostgreSQL driver
- **PostgreSQL** — Relational database
- **pgAdmin 4** — Database management and verification

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd basic-etl-fakestore
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install requests pandas sqlalchemy "psycopg[binary]" python-dotenv
```

### 4. Configure the database

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql+psycopg://username:password@localhost:5432/your_database
```

Replace the placeholders with your local PostgreSQL credentials and database name.

### 5. Run the pipeline

```bash
python main.py
```

## Project Structure

```text
basic-etl-fakestore/
├── main.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## What I Learned

- Understanding the Extract, Transform, Load process.
- Fetching data from REST APIs using HTTP requests.
- Working with JSON responses and Pandas DataFrames.
- Connecting Python applications to PostgreSQL.
- Using SQLAlchemy's `create_engine()` to configure database access.
- Loading structured data into a relational database.
- Managing Python dependencies and environment variables.

## Security

Never commit your `.env` file or expose database credentials.

Add the following to `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
```

## Notes

This is a beginner learning project using sample e-commerce data. The goal is to understand the fundamentals of building a Python ETL pipeline before exploring more advanced data engineering concepts.

---

<p align="center">
  <i>Small steps. Real skills. One pipeline at a time.</i>
</p>
