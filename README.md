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

The API will be available at:
http://localhost:8080

API documentation:
http://localhost:8080/docs

or

http://localhost:8080/redoc