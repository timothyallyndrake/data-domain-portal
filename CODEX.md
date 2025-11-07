<!-- 🔄 SYNC NOTICE — DO NOT REMOVE OR MODIFY -->

# Synchronization Requirement

This file (`CODEX.md`) is one of three **synchronized AI instruction files**:

- `.github/copilot-instructions.md`
- `GEMINI.md`
- `CODEX.md`

Any change made to **any** of these files **must be reflected identically** in the others to keep all AI assistants aligned on the same project intent and stack details.

⚠️ **Do not remove, rename, or alter this notice.** It safeguards cross-agent consistency.

**README Sync Rule:** The repository’s `README.md` is a canonical source of truth for goals, stack, and run instructions. Any change to this file **must also be reflected** in the AI instruction files (`.github/copilot-instructions.md`, `GEMINI.md`, `CODEX.md`) where applicable, so all assistants and contributors share the same context.

<!-- 🔄 END SYNC NOTICE -->

# Codex — Repository Instructions

## Objective

Implement a **Data Domain Portal**: a self-service ingestion, validation, and analytics platform that demonstrates modern data engineering and full-stack design principles.  
The first demo domain is **Orders**, but the architecture must remain generic to support any domain.

## Technologies

- **Frontend:** React (TypeScript), MUI, Zustand, React Router
- **Backend:** FastAPI (async), Pydantic, SQLAlchemy (async), Alembic
- **Messaging:** Apache Kafka (KRaft)
- **Cache:** Redis
- **Analytics:** Snowflake + dbt
- **Orchestration:** Dagster (assets, sensors, schedules)
- **Auth:** Keycloak (OIDC, JWT)
- **Policy:** Casbin (RBAC + PBAC)
- **Testing:** Jest/RTL, Pytest/httpx, Playwright, dbt tests
- **Observability:** OpenTelemetry → Jaeger/Grafana
- **Infra (Local):** Docker Compose, Terraform (Docker provider later)

## Coding Rules

1. Use **async/await** everywhere in Python.
2. Use **native `fetch`** with OpenAPI TypeScript types — no Axios.
3. Maintain an accurate and versioned **OpenAPI spec**.
4. Store all timestamps in **UTC**; localize only in the UI.
5. Apply **PII redaction middleware** in FastAPI logs.
6. Use **Casbin** for RBAC + resource-level PBAC (policy-based access).
7. Keep domain logic generic; “Orders” is only the example domain.
8. Follow consistent naming and structure between backend and frontend.

## Project Structure

apps/
web/ → React app (MUI, Zustand, routing, Contexts)
api/ → FastAPI service (routers: auth, domains, mappings, ingestion, analytics)
worker/ → Kafka consumer (validates data, writes Postgres, emits completion)
ops/
dbt/ → dbt project (sources, staging, marts, schema tests)
dagster/ → Dagster project (assets, jobs, sensors)
infra/
compose/ → Docker Compose files for local dependencies

## Expected Contributions

Codex should assist with:

- Generating **React components** (MUI + Zustand state management).
- Implementing **FastAPI routes**, **Pydantic models**, and **dependency-injected services**.
- Creating **SQLAlchemy async models** and **Alembic migrations**.
- Building **Dagster assets/jobs/sensors** for ELT orchestration.
- Writing **dbt YAML + SQL** models for staging and marts.
- Producing **Playwright E2E** tests for ingestion → analytics flows.
- Ensuring consistent typing, docstrings, and OpenAPI coverage.

## Testing Expectations

- **Frontend:** Jest + React Testing Library for units/integration; Playwright for E2E.
- **Backend:** Pytest + httpx.AsyncClient integration; Schemathesis for OpenAPI contract tests.
- **Worker:** Integration tests for Kafka → Postgres → Kafka flow.
- **dbt:** `dbt test` for not-null, unique, and custom constraints.
- **Dagster:** asset materialization tests and job selection tests.

## Observability

- Use **OpenTelemetry** for distributed tracing (web → api → worker).
- Log with **structlog**, redacting sensitive fields (e.g., tokens, emails, customer IDs).
- Include correlation IDs and trace context propagation.

## Dev & Infra

- Use **Docker Compose** for local Postgres, Redis, Kafka (KRaft), Keycloak, Jaeger, Grafana, and Dagster.
- Keep all `.env` variables documented in `.env.example`.
- Infrastructure as code will later use **Terraform (Docker provider)** to define the same local stack declaratively.

## Domain Example — Orders

### Canonical Fields

| Field            | Type                   | Notes                               |
| ---------------- | ---------------------- | ----------------------------------- |
| `order_id`       | UUID                   | Primary key                         |
| `customer_id`    | UUID                   | Reference                           |
| `order_ts`       | timestamptz (UTC)      | Stored in UTC                       |
| `currency`       | TEXT                   | ISO 4217 allowlist                  |
| `subtotal`       | NUMERIC(18,2)          | ≥ 0                                 |
| `tax`            | NUMERIC(18,2)          | ≥ 0                                 |
| `total`          | NUMERIC(18,2)          | ≥ subtotal + tax - 0.01             |
| `items`          | JSONB                  | Array of `{ sku, qty, unit_price }` |
| `source_file_id` | UUID                   | Originating upload                  |
| `ingest_run_id`  | UUID                   | Ingestion batch ID                  |
| `dq_status`      | ENUM(pass, warn, fail) | Data quality result                 |

### Data Quality Rules

- Required fields: `order_id`, `customer_id`, `order_ts`, `currency`, `total`.
- Type validation: UUIDs, timestamps, numeric fields.
- Non-negativity: subtotal, tax, total ≥ 0.
- Relational: `total >= subtotal + tax - 0.01`.
- Currency allowlist: `{USD, EUR, GBP, JPY, AUD, CAD, CHF}`.

### dbt Models

- `stg_orders.sql`: cleans types, normalizes fields, ensures UTC timestamps.
- `fct_orders_daily.sql`: aggregates orders by day and currency.
- `schema.yml`: not_null, unique, accepted_values tests.

### Kafka Topics

- `ingestion.requests`: emitted from API when ingestion starts.
- `ingestion.completed`: emitted by worker when load is done.
- `dq.reports`: optional topic for summary DQ metrics.

### Dagster Flow

1. Sensor on `ingestion.completed`.
2. Export validated data as Parquet.
3. Stage in Snowflake (`@ingest_stage`).
4. Run `COPY INTO RAW.ORDERS`.
5. Trigger `dbt run` + `dbt test`.
6. Emit completion + metrics to Dagit UI.

## Security

- OIDC auth with **Keycloak**, SPA PKCE flow.
- Backend verifies JWT (via JWKS).
- Casbin enforces policies at route/service layer.
- PII masking on all logs.

## Code Quality Expectations

- Consistent naming and modularity.
- Comprehensive inline docstrings and JSDoc-style comments.
- Every feature accompanied by unit + integration tests.
- No reliance on hidden automation; all commands explicit in README.

## Summary

Codex must assist in producing **clear, async, typed, and testable code** aligned with this stack and architecture.  
All generated examples, explanations, or refactors must preserve consistency with the shared Copilot and Gemini instructions.
