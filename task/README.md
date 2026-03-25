# Customer Data Pipeline Assessment

A data pipeline with 3 Docker services: Flask API (Mock server), FastAPI (Data ingestion), and PostgreSQL (Data storage).

## Project Structure

- `mock-server/`: Flask REST API serving customer data from `data/customers.json`.
- `pipeline-service/`: FastAPI service that ingests data from Flask into PostgreSQL using the `dlt` library.
- `docker-compose.yml`: Orchestrates the services.

## Prerequisites

- Docker Desktop
- Python 3.10+
- Git

## How to Run

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd project-root
    ```

2.  **Start all services**:
    ```bash
    docker-compose up -d --build
    ```

3.  **Test Flask Mock Server**:
    ```bash
    curl "http://localhost:5000/api/customers?page=1&limit=5"
    ```

4.  **Ingest data into PostgreSQL**:
    ```bash
    curl -X POST "http://localhost:8000/api/ingest"
    ```

5.  **Get paginated customers from PostgreSQL**:
    ```bash
    curl "http://localhost:8000/api/customers?page=1&limit=5"
    ```

6.  **Get a single customer**:
    ```bash
    curl "http://localhost:8000/api/customers/CUST001"
    ```

## Technology Stack

- **Flask**: Mock API server.
- **FastAPI**: Ingestion pipeline and API.
- **SQLAlchemy**: ORM for database operations.
- **DLT (Data Load Tool)**: Used for data ingestion with upsert logic.
- **PostgreSQL**: Relational database storage.
- **Docker & Docker Compose**: Containerization and orchestration.
