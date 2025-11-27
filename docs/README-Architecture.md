# Infinite Stock Trader - Architecture

## Table of Contents
1. [Overview](#1-overview)
2. [System Architecture](#2-system-architecture)
3. [Project Structure](#3-project-structure)
4. [Component Details](#4-component-details)
5. [Data Flow](#5-data-flow)
6. [Development Environment](#6-development-environment)

<br>

# 1. Overview

The Infinite Stock Trader is an automated trading system that uses a Dollar-Cost Averaging (DCA) algorithm to execute trades via the Alpaca Trading API. The system is containerized using Docker for consistent development and deployment environments.

**Key Technologies:**
- Python 3.11
- Alpaca Trading API (alpaca-py)
- Docker & Docker Compose
- Poetry for dependency management

<br>

# 2. System Architecture

```
┌─────────────────────────────────────────────────────┐
│                  Docker Container                   │
│  ┌───────────────────────────────────────────────┐  │
│  │           Infinite Stock Trader App           │  │
│  │                                               │  │
│  │  ┌──────────┐         ┌──────────────────┐    │  │
│  │  │  main.py │────────▶│  Trader Module   │    │  │
│  │  │   (App)  │         │  (src/trader.py) │    │  │
│  │  └──────────┘         └────────┬─────────┘    │  │
│  │                                 │             │  │
│  │                                 ▼             │  │
│  │                     ┌───────────────────────┐ │  │
│  │                     │   Alpaca Trading API  │ │  │
│  │                     │  - TradingClient      │ │  │
│  │                     │  - Account Info       │ │  │
│  │                     │  - Trading Operations │ │  │
│  │                     └───────────────────────┘ │  │
│  └───────────────────────────────────────────────┘  │
│                                                     │
│  Volumes:                                           │
│  - ./workspace → /home/user/workspace               │
│  - ./docker-volumes → /home/user/docker-volumes     │
└─────────────────────────────────────────────────────┘
                           │
                           ▼
                ┌────────────────────┐
                │  Alpaca Broker API │
                │   (Paper/Live)     │
                └────────────────────┘
```

<br>

# 3. Project Structure

```
infinite-stock-trader/
├── docker/
│   └── dev.dockerfile              # Development container configuration
├── docker-volumes/
│   ├── .env                        # Environment variables (API keys)
│   └── example.env                 # Template for environment setup
├── workspace/                      # Main application directory
│   ├── src/
│   │   ├── __init__.py
│   │   └── trader.py               # Core trading logic and API wrapper
│   ├── main.py                     # Application entry point
│   ├── pyproject.toml              # Poetry dependencies
│   └── poetry.lock                 # Locked dependencies
├── docs/
│   ├── README-Architecture.md      # This file
│   ├── README-EarlyResearch.md
│   └── README-ProjectSetup.md
├── docker-compose.yaml             # Container orchestration
└── README.md                       # Main documentation
```

<br>

# 4. Component Details

## 4.1 Main Application (`main.py`)

**Purpose:** Application entry point and lifecycle management

**Key Components:**
- `App` class: Initializes the trader and manages application flow
- Loads environment configuration from `docker-volumes/.env`
- Creates and connects the Trader instance

**Flow:**
```python
1. Create App instance
2. Initialize Trader with ENV_FILE_PATH
3. Connect to Alpaca API
4. Execute run() method
5. Exit
```

## 4.2 Trader Module (`src/trader.py`)

**Purpose:** Encapsulates all trading operations and API interactions

**Responsibilities:**
- Load API credentials from environment file
- Initialize TradingClient (paper or live mode)
- Connect to Alpaca and verify account status
- Display account information (buying power, status, etc.)
- Future: Execute DCA trading strategy

**Key Methods:**
- `__init__(env_path)`: Load configuration from .env file
- `connect()`: Establish connection to Alpaca API and display account info

**Environment Variables:**
- `ALPACA_API_KEY`: API key for authentication
- `ALPACA_API_SECRET`: Secret key for authentication
- `ALPACA_PAPER_MODE`: Toggle between paper trading (True) and live trading (False)

## 4.3 Dependencies (`pyproject.toml`)

**Core Dependencies:**
- `alpaca-py (>=0.43.2,<0.44.0)`: Official Alpaca Trading API Python client
- `python-dotenv (>=0.9.9,<0.10.0)`: Environment variable management

**Python Version:** 3.11

<br>

# 5. Data Flow

```
┌──────────────┐
│   main.py    │
│   starts     │
└──────┬───────┘
       │
       ▼
┌─────────────────────────────┐
│ App.__init__()              │
│ - Creates Trader instance   │
│ - Passes ENV_FILE_PATH      │
└──────┬──────────────────────┘
       │
       ▼
┌─────────────────────────────┐
│ Trader.__init__()           │
│ - load_dotenv()             │
│ - Load API credentials      │
│ - Set paper/live mode       │
└──────┬──────────────────────┘
       │
       ▼
┌─────────────────────────────┐
│ Trader.connect()            │
│ - Create TradingClient      │
│ - Get account info          │
│ - Display status            │
└──────┬──────────────────────┘
       │
       ▼
┌─────────────────────────────┐
│ App.run()                   │
│ - Execute trading logic     │
│ - (Currently placeholder)   │
└─────────────────────────────┘
```

<br>

# 6. Development Environment

## 6.1 Docker Setup

**Base Image:** Ubuntu 22.04  
**Python Version:** 3.11  
**Poetry Version:** 2.2.1

**Key Features:**
- Virtual environment created in-project (`.venv`)
- Non-root user (`user`) for security
- Volume mounts for live code editing
- Host network mode for simplified connectivity

## 6.2 Running the Application

**Start Development Container:**
```bash
docker compose run -e HOST_USER_ID=jyoo -e HOST_USER_PWD=jyoo123 --service-ports --rm dev bash
```

**Inside Container:**
```bash
cd /home/user/workspace
poetry install          # Install dependencies
python main.py          # Run application
```

## 6.3 Volume Mounts

| Host Path | Container Path | Purpose |
|-----------|----------------|---------|
| `./workspace` | `/home/user/workspace` | Source code and dependencies |
| `./docker-volumes` | `/home/user/docker-volumes` | Configuration files (.env) |
| `~/.bash_history` | `/home/user/.bash_history` | Persist shell history |
| `/tmp/.X11-unix` | `/tmp/.X11-unix` | X11 forwarding (future GUI support) |

## 6.4 VS Code Integration

The Python interpreter path is configured in `.vscode/settings.json`:
```json
{
    "python.defaultInterpreterPath": "workspace/.venv/bin/python"
}
```

**Note:** Since the `.venv` exists inside the Docker container, import resolution in VS Code requires either:
1. Using the Dev Containers extension to work inside the container
2. Installing dependencies locally for IntelliSense only
3. Configuring the Python extension to use the containerized interpreter

<br>

