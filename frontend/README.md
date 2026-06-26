# There Is No Earth B (Tech Assessment-Frontend)

## Overview

This is a frontend application built with react+vite as part of the technical assessment for There Is No Earth B.

It is a single-page application (SPA) that allows users to search members by calling the backend `/search` API.

## Tech Stack

- React
- Vite
- JavaScript (JSX)
- Axios
- Docker

## Environment Variables

The application requires the following environment variable:

| Variable | Description |
|----------|-------------|
| `VITE_API_BASE_URL` | Base URL of the backend API |

Example:

```env
VITE_API_BASE_URL=http://localhost:8080
```

## Running the Application

Build the Docker image:

```bash
docker build -t tineb-frontend:latest .
```

Run the container:

```bash
docker run -d \
  -p 5173:5173 \
  --env-file .env \
  --name tineb-frontend \
  tineb-frontend:latest
```

Note: Pass the `VITE_API_BASE_URL` environment variable using the `--env-file` flag or any other preferred method.

The application will be available at:

```
http://localhost:5173
```