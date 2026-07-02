# DecodeLabs Backend Development — Project 1

**REST API Fundamentals** | Batch 2026

---

## Overview

A stateless RESTful API built with **FastAPI** (Python) that demonstrates core backend fundamentals: HTTP methods, routing logic, JSON serialization, and proper status code handling. No database is used — data is stored in-memory to keep the focus on API structure and REST principles.

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3 | Language |
| FastAPI | Web framework |
| Uvicorn | ASGI server |
| Pydantic | Request body validation |

---

## Project Structure

```
decodelabs-p1/
├── venv/          # Virtual environment (not committed)
├── main.py        # All API routes and logic
└── README.md      # This file
```

---

## Setup & Installation

### Prerequisites

- Python 3.8+
- Fedora Linux (or any Linux distro)

### Steps

```bash
# 1. Clone or enter the project directory
cd decodelabs-p1

# 2. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install fastapi uvicorn

# 4. Run the development server
uvicorn main:app --reload
```

Server starts at: `http://127.0.0.1:8000`

---

## API Endpoints

### Base URL

```
http://127.0.0.1:8000
```

---

### `GET /`

Health check — confirms the server is running.

**Response `200 OK`**
```json
{
  "message": "DecodeLabs P1 API is live"
}
```

---

### `GET /products`

Returns all products in the store.

**Response `200 OK`**
```json
{
  "status": "ok",
  "count": 3,
  "data": [
    { "id": 1, "name": "Laptop",   "price": 75000 },
    { "id": 2, "name": "Mouse",    "price": 499   },
    { "id": 3, "name": "Keyboard", "price": 1200  }
  ]
}
```

---

### `GET /products/{id}`

Returns a single product by ID.

**Response `200 OK`**
```json
{
  "status": "ok",
  "data": { "id": 1, "name": "Laptop", "price": 75000 }
}
```

**Response `404 Not Found`** (if ID doesn't exist)
```json
{
  "detail": "Product not found"
}
```

---

### `POST /products`

Creates a new product. Requires a JSON request body.

**Request Body**
```json
{
  "name": "Monitor",
  "price": 15000
}
```

**Response `201 Created`**
```json
{
  "status": "created",
  "data": { "id": 4, "name": "Monitor", "price": 15000 }
}
```

**Response `400 Bad Request`** (if name is empty)
```json
{
  "detail": "Name cannot be empty"
}
```

**Response `422 Unprocessable Entity`** (if data types are wrong — handled automatically by Pydantic)
```json
{
  "detail": [...]
}
```

---

## Testing with curl

```bash
# Health check
curl http://127.0.0.1:8000/

# Get all products
curl http://127.0.0.1:8000/products

# Get single product
curl http://127.0.0.1:8000/products/1

# Get non-existent product (404)
curl http://127.0.0.1:8000/products/999

# Create a product
curl -X POST http://127.0.0.1:8000/products \
  -H "Content-Type: application/json" \
  -d '{"name": "Monitor", "price": 15000}'

# Create with empty name (400)
curl -X POST http://127.0.0.1:8000/products \
  -H "Content-Type: application/json" \
  -d '{"name": "", "price": 500}'

# Pretty-print JSON output
curl http://127.0.0.1:8000/products | python3 -m json.tool
```

---

## Interactive API Docs

FastAPI auto-generates Swagger UI — no setup needed.

```
http://127.0.0.1:8000/docs
```

Open in browser after starting the server to test all routes interactively.

---

## Key Concepts Demonstrated

**Statelessness** — The server holds no session data. Every request is fully self-contained. The in-memory list simulates a data store but no client state is preserved between requests.

**RESTful routing** — Routes use plural nouns (`/products`), not verbs (`/getProducts`). The HTTP method (GET, POST) communicates the action.

**Correct status codes** — `200` for successful reads, `201` for successful creation, `400` for invalid client input, `404` for missing resources.

**JSON as transport** — All request bodies and responses are structured JSON. Pydantic automatically validates incoming data types and structure.

**Idempotency** — GET requests are safe and idempotent (repeated calls return the same data). POST is non-idempotent — each call creates a new resource.

---

## HTTP Method Reference

| Method | Route | Action | Status Code |
|---|---|---|---|
| GET | `/products` | Fetch all products | 200 |
| GET | `/products/{id}` | Fetch one product | 200 / 404 |
| POST | `/products` | Create new product | 201 / 400 |

---

## Notes

- Data resets on every server restart (no persistent storage — intentional for P1)
- Pydantic validation handles type checking automatically
- The `--reload` flag in uvicorn auto-restarts the server when `main.py` is saved

---

## Author

**Tejas Kedarpawar**
B.Tech Computer Science — RCOEM (Ramdeobaba University), Nagpur
DecodeLabs Backend Batch 2026
