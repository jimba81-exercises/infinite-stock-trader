# Arguments
ARG PYTHON_VERSION=3.11
ARG POETRY_VERSION=2.2.1

#========================
FROM ubuntu:22.04
ARG PYTHON_VERSION
ARG POETRY_VERSION
LABEL POETRY_VERSION="$POETRY_VERSION"

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python${PYTHON_VERSION} \
    python${PYTHON_VERSION}-venv \
    python${PYTHON_VERSION}-dev \
    python3-pip \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set Python version as default python3
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python${PYTHON_VERSION} 1

# Poetry: Install
RUN pip install "poetry==$POETRY_VERSION"

# Create venv inside the project (i.e. ./.venv)
RUN poetry config virtualenvs.in-project true

# Create a non-root user
RUN useradd -m -s /bin/bash user

# Set workspace directory
USER user
WORKDIR /home/user/workspace

# Configure Poetry for the user to create venv in project
RUN poetry config virtualenvs.in-project true

CMD ["sh", "-c", "echo 'This is DEV Container. Run /bin/bash to start the development environment'"]

