#  FastAPI_and_Pydantic

This repository contains a Patient Management Project built using **FastAPI**. It includes **CRUD (Create, Retrieve, Update, Delete)** endpoints to manage patient data. The project also features a dedicated **Pydantic schema file**, which demonstrates in-depth concepts of data validation and type enforcement using Pydantic models.

---

#  FastAPI Project Setup Guide

This guide walks you through setting up a FastAPI project using a virtual environment and installing the necessary dependencies.

##  Step 1: Create a Virtual Environment

```bash
python -m venv myenv
```

##  Step 2: Activate the Virtual Environment

```bash
source myenv/bin/activate
```

##  Step 3: Install Required Packages

```bash
pip install fastapi uvicorn pydantic
```

These are the core dependencies for your FastAPI app:

- **FastAPI** – the web framework  
- **Uvicorn** – the ASGI server  
- **Pydantic** – for data validation and type enforcement

##  Step 4: Run the FastAPI App

```bash
uvicorn main:app --reload
```

- `main` is the name of your Python file (e.g., `main.py`)  
- `app` is the FastAPI instance inside `main.py`  
- `--reload` enables auto-reloading on code changes (useful for development)

##  Example Directory Structure

```
.
├── main.py
├── patient.json
├── pydantic
│   └── pydantic_01.py
|   |__ pydantic_02.py
├── myenv/
├── .gitignore
└── README.md
```

