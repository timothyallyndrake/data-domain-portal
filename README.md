# Data Domain Portal

<a alt="Nx logo" href="https://nx.dev" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/nrwl/nx/master/images/nx-logo.png" width="45"></a>

Full-stack data platform demo using React + TypeScript, FastAPI + Python, Kafka, Redis, Snowflake, dbt, and Dagster. This project showcases self-service data ingestion, validation, orchestration, and analytics with modern testing and observability, all managed within a high-performance Nx monorepo.

## Project Goal

Build a **Data Domain Portal**: a self-service data platform for mapping CSV data to canonical models, validating that data, triggering ingestion pipelines, orchestrating ELT processes into **Snowflake** (via **Dagster** + **dbt**), and visualizing the resulting analytics. The primary demonstration domain is **Orders**, but the architecture is designed to be generic so new domains can be added with minimal changes.

## Technology Stack

- **Monorepo:** [Nx](https://nx.dev)
- **Frontend:** React, TypeScript, MUI, Zustand
- **Backend:** FastAPI (Python), SQLAlchemy, Pydantic, Redis
- **Data Platform:** Snowflake, dbt
- **Testing:** Pytest, Jest/RTL, Playwright
- **DevOps & CI/CD:** Docker, GitHub Actions

## Getting Started

### Prerequisites

- **Node.js (v24+ LTS):** Recommended to use a version manager like `nvm`.
- **pnpm (v10+):** [pnpm installation guide](https://pnpm.io/installation).
- **Python (v3.11+):** Recommended to use a version manager like `pyenv`.
- **Docker Desktop:** For running local services like Redis.
- **`uv`:** The Python package installer. [uv installation guide](https://astral.sh/uv/install).

### 1. First-Time Setup

1.  **Clone the repository:**

    ```sh
    git clone <repository_url>
    cd data-domain-portal
    ```

2.  **Install JavaScript dependencies:**

    ```sh
    pnpm install
    ```

3.  **Set up Backend Environment:**
    The Python backend requires credentials for external services.

    - First, create your local environment file by copying the template:
      ```sh
      cp apps/server/.env.example apps/server/.env
      ```
    - Fill in the required credentials in `apps/server/.env`.

4.  **Set up the Database Schema:**
    This project uses Snowflake as its data warehouse. The following command will connect to your Snowflake instance and create the necessary tables. This command is idempotent and is safe to run multiple times.
    ```sh
    pnpm nx run server:setup-db
    ```

### 2. Running the Application

This monorepo contains multiple applications. You will need to run each in a separate terminal.

- **Run the Backend API Server:**

  ```sh
  pnpm nx serve server
  ```

- **Run the Frontend Web Application:**
  _(Once the `client` app is generated)_
  ```sh
  pnpm nx serve client
  ```
- **Run a local Redis instance:**
  ```sh
  docker run -d --name ddp-redis -p 6379:6379 redis
  ```

## Development Workflow

This workspace uses [Nx](https://nx.dev) to manage tasks and automate the development lifecycle.

- **Run tests for a specific project:**

  ```sh
  pnpm nx test server
  pnpm nx test client
  ```

- **Run end-to-end tests:**

  ```sh
  pnpm nx e2e client-e2e
  ```

- **Visually explore the project graph:**
  ```sh
  pnpm nx graph
  ```

## CI/CD and Automation

This project includes two primary GitHub Actions for automation:

1.  **Release Please**: Automates the release process by generating release notes and versioning based on commit messages, ensuring that releases are consistent and follow semantic versioning.

2.  **Continuous Integration (CI)**: This action runs linting and testing on every push to the repository. It helps maintain code quality and ensures that all changes are validated before merging into the main branch.

## Future Work & TODOs

This project is a demonstration and has several areas for future improvement:

- [ ] **Formalize Database Migrations:** The initial schema is created via a script for stability. The next step is to re-integrate a tool like **Alembic** in "manual mode" to provide version-controlled schema migrations, which is a more robust pattern for production environments.
- [ ] **Containerize All Services:** Create `Dockerfile`s for all applications and a `docker-compose.yml` file to orchestrate the entire stack locally.
- [ ] **Full Data Orchestration:** Replace the synchronous data upload with an event-driven flow using **Kafka** and an orchestrator like **Dagster**.
