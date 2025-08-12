# EDA and Visualisation API

## Overview
The **EDA and Visualisation API** is a FastAPI-based microservice that performs **Exploratory Data Analysis (EDA)** and generates **visualisations** from dataset inputs.  
It contains two main endpoints:
1. `/eda-insights` → Generates key dataset statistics and summaries.
2. `/visualisation` → Produces charts from dataset columns.

This API is designed to be part of the **Dataset AI pipeline** (https://github.com/aerhedai/dataset-ai-integration-tests) and works in conjunction with other modular APIs.

---

## Features
- **EDA Insights**:
  - Dataset shape, column names, and types.
  - Basic statistical summary.
  - Missing values count.
  - Target column distribution (if provided).
- **Visualisations**:
  - Histograms for numeric columns.
  - Bar charts for categorical columns.
  - Scatter plots for relationships.
  - JSON-based chart data using Plotly for easy integration into web apps.

---

## Project Structure
```
eda-and-visualisation-api/
│
├── app/
│   ├── main.py             # API entry point
│   ├── routes.py           # API endpoints
│   ├── models.py           # Pydantic models for requests/responses
│   ├── eda.py               # EDA logic
│   ├── visualisation.py     # Visualisation logic
│   ├── logging_config.py    # Centralised logging configuration
│
├── tests/
│   ├── test_routes.py       # Unit tests for endpoints
│
├── requirements.txt         # Python dependencies
├── README.md
├── CHANGELOG.md
```

---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/aerhedai/eda-and-visualisation-api.git
cd eda-and-visualisation-api
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## Usage

### Run locally
```bash
uvicorn app.main:app --reload --port 8005
```

### Example request (EDA Insights)
```bash
curl -X POST "http://localhost:8005/eda-insights" \
-H "Content-Type: application/json" \
-d '{
    "rows": [
        {"col1": 1, "col2": "A"},
        {"col1": 2, "col2": "B"},
        {"col1": 3, "col2": "A"}
    ],
    "target_column": "col2"
}'
```

### Example request (Visualisation)
```bash
curl -X POST "http://localhost:8005/visualisation" \
-H "Content-Type: application/json" \
-d '{
    "rows": [
        {"col1": 1, "col2": "A"},
        {"col1": 2, "col2": "B"},
        {"col1": 3, "col2": "A"}
    ],
    "chart_type": "histogram",
    "x_column": "col1"
}'
```

---

## API Endpoints

### `POST /eda-insights`
**Request Body:**
```json
{
    "rows": [ { "column1": "value1", "column2": "value2" }, ... ],
    "target_column": "optional_target"
}
```

**Response:**
```json
{
    "shape": [3, 2],
    "columns": ["col1", "col2"],
    "missing_values": { "col1": 0, "col2": 0 },
    "statistics": { "col1": { "mean": 2.0, "min": 1, "max": 3 } }
}
```

---

### `POST /visualisation`
**Request Body:**
```json
{
    "rows": [ { "column1": "value1", "column2": "value2" }, ... ],
    "chart_type": "histogram",
    "x_column": "col1",
    "y_column": "optional"
}
```

**Response:**
```json
{
    "chart_type": "histogram",
    "figure": { "data": [...], "layout": {...} }
}
```

---

## Running Tests
```bash
pytest
```

---