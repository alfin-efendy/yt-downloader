# Dockerfile
FROM python:3.11-slim AS builder-base

# Build stage environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.7.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Install system dependencies
RUN apt-get update && \
    apt-get install --no-install-recommends -y \
        curl \
        build-essential && \
    rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Set up poetry environment
WORKDIR $PYSETUP_PATH
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry install --no-dev && \
    poetry export -f requirements.txt --output requirements.txt

# Runtime stage
FROM python:3.11-slim AS runtime

# Runtime stage environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Install FFmpeg and required dependencies
RUN apt-get update && \
    apt-get install --no-install-recommends -y \
        ffmpeg \
        libavcodec-extra \
        libavformat-dev \
        libavcodec-dev \
        libavdevice-dev \
        libavfilter-dev \
        libavutil-dev \
        libswscale-dev \
        libswresample-dev \
        libpostproc-dev \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/*

# Create and set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY --from=builder-base /opt/pysetup/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create non-root user
RUN useradd --create-home appuser && \
    chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Copy application code
COPY --chown=appuser:appuser . .

# Run the application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]