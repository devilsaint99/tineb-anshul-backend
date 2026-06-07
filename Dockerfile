FROM python:3.13-slim-trixie
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY . /app

ENV UV_NO_DEV=1

WORKDIR /app
RUN ls 
RUN uv sync --locked

CMD ["/app/.venv/bin/uvicorn", "app.main:app", "--port", "8080", "--host", "0.0.0.0"]