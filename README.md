# data-domain-portal

Full-stack data platform demo using React + TypeScript, FastAPI + Python, Kafka, Redis, Snowflake, dbt, and Dagster. Showcases self-service data ingestion, validation, orchestration, and analytics with modern testing and observability.

## GitHub Actions

This project includes two GitHub Actions for automation:

1. **Release Please**: Automates the release process by generating release notes and versioning based on commit messages. This ensures that releases are consistent and follow semantic versioning.

2. **Continuous Integration (CI)**: This action runs linting and testing on every push to the repository. It helps maintain code quality and ensures that all changes are validated before merging into the main branch.

## Project Goal

Build a **Data Domain Portal**: a self-service data platform for mapping CSV → canonical models, validating data, triggering ingestion, orchestrating ELT into **Snowflake** (via **Dagster** + **dbt**), and visualizing analytics. Primary demo domain: **Orders**. Architecture must remain **generic** so new domains can be added with minimal changes.

## Tech Stack

- **Frontend**: React + TypeScript, MUI, Zustand, React Router, Hooks + Context API
- **Backend**: FastAPI (asyncio-first), Pydantic, SQLAlchemy (async), Alembic
- **Messaging**: Apache Kafka (KRaft)
- **Cache/Session**: Redis
- **Analytics**: Snowflake (stages, COPY INTO), dbt (staging+marts+tests)
- **Orchestration**: Dagster (assets, sensors, schedules)
