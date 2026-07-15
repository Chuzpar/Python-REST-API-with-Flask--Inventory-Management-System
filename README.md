# Inventory Management System

## Overview

This project is a Flask REST API for managing inventory items. It includes CRUD operations, a command-line interface (CLI), and integration with the OpenFoodFacts API.

---

## Features

- View inventory
- Add products
- Update products
- Delete products
- Search OpenFoodFacts
- REST API
- CLI
- Unit testing with pytest

---

## Installation

Clone the repository.

```bash
git clone <your-github-url>
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Run the Flask server.

```bash
python app.py
```

Run the CLI.

```bash
python cli.py
```

Run tests.

```bash
pytest
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /inventory | Get all products |
| GET | /inventory/<id> | Get one product |
| POST | /inventory | Add product |
| PATCH | /inventory/<id> | Update product |
| DELETE | /inventory/<id> | Delete product |
| GET | /search/<barcode> | Search OpenFoodFacts |

---

## Technologies

- Python
- Flask
- Requests
- Pytest
- Git
- OpenFoodFacts API

---

## Author

Yasin