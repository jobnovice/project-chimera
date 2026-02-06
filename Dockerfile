FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app

# system deps (minimal)
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential curl \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app

# Create venv and install runtime/dev dependencies including `uv`
RUN python -m venv /opt/venv \
    && /opt/venv/bin/pip install --upgrade pip setuptools wheel \
    && /opt/venv/bin/pip install uv pytest jsonschema

ENV PATH="/opt/venv/bin:${PATH}"

CMD ["pytest", "-q"]
