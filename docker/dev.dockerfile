# Use Ubuntu as base image
FROM ubuntu:22.04

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3.11 \
    python3.11-venv \
    python3.11-dev \
    python3-pip \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set Python 3.11 as default python3
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# Configure Poetry
RUN poetry config virtualenvs.create false

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install project dependencies if pyproject.toml exists
RUN if [ -f pyproject.toml ]; then poetry install --no-interaction --no-ansi; fi

# Default command
CMD ["/bin/bash"]
