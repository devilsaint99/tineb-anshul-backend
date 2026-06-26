# There Is No Earth B (Tech Assessment-Backend)

## Overview

This is a backend API for an assessment for backend for the tech team of NGO: There is No Earth B.
- This is just a simple api with pagination only, there is no filter feature as of now.

## Tech Stack
- Python 3.13
- PostgresSQL(supabase)
- FastAPI
- Alembic+SQLALchemy

## Application Usage

### Pre-requisite

- Docker installed on your machine
- Data on postgres DB
- DB credentials

### Commands to Run

Build the Docker image:

```bash
docker build -t tineb:latest .
```

Run the container:
```bash
docker run -d -p 8080:8080 --name tineb-api tineb:latest
```

Note: Pass the required environment variables using the `--env-file` flag or any other preferred method.

Following are the env variables for backend:
- DB_USER
- DB_PASSWORD
- DB_HOST
- DB_PORT
- DB_NAME

Example:

```env
DB_USER=user_xyz
DB_PASSWORD=password
DB_HOST=xyz_host.com
DB_PORT=5432
DB_NAME=eagle
```


The API will be available at:
http://localhost:8080

API documentation:
http://localhost:8080/docs

or

http://localhost:8080/redoc

# API Endpoints

## GET /members

Returns all members.

### Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| page | integer | Page number (default: 1) |
| limit | integer | Number of records per page. If omitted, all records are returned. |

### Example

```
GET /members?page=2&limit=20
```

---

## GET /search

Searches members by:

- Name
- Party
- State
- Constituency

### Query Parameters

| Parameter | Type | Required |
|-----------|------|----------|
| q | string | Yes |

### Example

```
GET /search?q=Kerala
```

### Response

```json
{
  "query": "Kerala",
  "length": 7,
  "timestamp": "2026-06-26T10:32:14.172Z",
  "results": [
    {
      "id": 240,
      "name": "...",
      "party": "...",
      "state": "...",
      "constituency": "..."
    }
  ]
}
```

---