# Mechanic Service API

A RESTful API built with Django and Django REST Framework for managing mechanics and customer service requests.

## Features

- Create and manage mechanics
- Retrieve all mechanics
- Retrieve a mechanic by ID
- Update mechanic details
- Delete mechanics
- Create customer service requests
- Assign service requests to mechanics
- Validate phone numbers
- Validate mechanic ratings
- Validate vehicle numbers
- Validate available services
- Validate mechanic IDs
- Automatic `PENDING` status for new service requests
- Automatic request creation timestamps

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite

## Project Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd mechanic_service_api
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

#### macOS/Linux

```bash
source .venv/bin/activate
```

#### Windows

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install django djangorestframework
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

---

# API Endpoints

## Mechanics

### Get all mechanics

```http
GET /api/mechanics/
```

### Create a mechanic

```http
POST /api/mechanics/
```

Example request:

```json
{
  "name": "Ali Motors",
  "phone": "9876543210",
  "location": "Jammu",
  "rating": "4.50",
  "is_open": true,
  "services": ["Oil Change", "Engine Repair", "Brake Repair"]
}
```

### Get a mechanic by ID

```http
GET /api/mechanics/<id>/
```

Example:

```http
GET /api/mechanics/1/
```

### Update a mechanic

```http
PUT /api/mechanics/<id>/
```

or:

```http
PATCH /api/mechanics/<id>/
```

Example PATCH request:

```json
{
  "is_open": false
}
```

### Delete a mechanic

```http
DELETE /api/mechanics/<id>/
```

---

# Service Requests

### Create a service request

```http
POST /api/service-requests/
```

Example request:

```json
{
  "customer_name": "Arhan",
  "customer_phone": "9876543210",
  "vehicle_number": "JK01AB1234",
  "mechanic": 1,
  "service": "Oil Change",
  "problem_description": "The engine oil needs to be changed."
}
```

Example response:

```json
{
  "id": 1,
  "customer_name": "Arhan",
  "customer_phone": "9876543210",
  "vehicle_number": "JK01AB1234",
  "service": "Oil Change",
  "problem_description": "The engine oil needs to be changed.",
  "status": "PENDING",
  "created_at": "2026-09-01T15:16:03.529328Z",
  "mechanic": 1
}
```

New service requests automatically receive:

```text
status = PENDING
```

and `created_at` is generated automatically.

---

# Validation

The API validates the following:

## Phone Number

Phone numbers must contain exactly 10 digits.

Invalid example:

```text
12345
```

## Rating

Mechanic ratings must be between:

```text
0 and 5
```

## Services

Supported services are:

- Oil Change
- Engine Repair
- Brake Repair
- Tire Repair
- Battery Service

A mechanic must provide at least one service.

## Service Request Validation

A customer cannot request a service that is not provided by the selected mechanic.

For example, if a mechanic provides:

```text
Oil Change
Engine Repair
```

a request for:

```text
Battery Service
```

will be rejected.

## Vehicle Number

Vehicle numbers are normalized to uppercase and must contain at least 6 characters.

## Mechanic Validation

A service request must reference an existing mechanic.

Invalid mechanic IDs return a validation error.

---

# HTTP Status Codes

| Status Code       | Meaning                           |
| ----------------- | --------------------------------- |
| `200 OK`          | Successful GET or update request  |
| `201 Created`     | Resource created successfully     |
| `204 No Content`  | Resource deleted successfully     |
| `400 Bad Request` | Invalid request data              |
| `404 Not Found`   | Requested mechanic does not exist |

---

# Project Structure

```text
mechanic_service_api/
│
├── config/
│   ├── settings.py
│   └── urls.py
│
├── mechanics/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
└── README.md
```
