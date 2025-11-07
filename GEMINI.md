<!-- 🔄 SYNC NOTICE — DO NOT REMOVE OR MODIFY -->

# Synchronization Requirement

This file (`GEMINI.md`) is one of three **synchronized AI instruction files**:

- `.github/copilot-instructions.md`
- `GEMINI.md`
- `CODEX.md`

Any change made to **any** of these files **must be reflected identically** in the others to keep all AI assistants aligned on the same project intent and stack details.

⚠️ **Do not remove, rename, or alter this notice.** It safeguards cross-agent consistency.

**README Sync Rule:** The repository’s `README.md` is a canonical source of truth for goals, stack, and run instructions. Any change to this file **must also be reflected** in the AI instruction files (`.github/copilot-instructions.md`, `GEMINI.md`, `CODEX.md`) where applicable, so all assistants and contributors share the same context.

<!-- 🔄 END SYNC NOTICE -->

# Gemini — Repository Instructions

## Intent

Assist in implementing a **full-stack data platform** called **Data Domain Portal** — a self-service ingestion, validation, and analytics solution built around Snowflake, Dagster, and dbt. All implementations must remain explicit and reproducible (no hidden one-click automation).

## Stack (authoritative)

- **Frontend**: React + TypeScript, MUI, Zustand, React Router, Hooks + Context API
- **Backend**: FastAPI (async), Pydantic, SQLAlchemy (async), Alembic
- **Messaging**: Kafka (KRaft)
- **Cache**: Redis
- **Analytics**: Snowflake + dbt
- **Orchestration**: Dagster (assets, sensors, schedules)
- **Auth**: Keycloak (OIDC), JWT
- **Policy**: Casbin (RBAC + PBAC)
- **Testing**: Jest/RTL, Pytest/httpx, Playwright, dbt tests, Dagster asset tests
- **Observability**: OpenTelemetry → Jaeger/Grafana

## Principles

1. Strong typing and contracts (OpenAPI ↔ TS ↔ db).
2. Async-first for I/O-bound Python.
3. Generic domain architecture; “Orders” only as example.
4. PII-safe logging.
5. Unit → Integration → E2E test flow.
6. Explicit dev steps, no hidden scripts.

## Preferred Patterns

- **React**: hooks, context, Zustand stores.
- **FastAPI**: routers per feature, Pydantic models, dependency-injected auth/policy.
- **SQLAlchemy/Alembic**: explicit migrations.
- **Kafka**: produce/consume JSON.
- **Dagster**: asset graphs triggering dbt runs/tests.
- **dbt**: RAW → staging → marts with schema tests.

## What Gemini Should Do

- Suggest improvements within stack boundaries.
- Generate MUI components, Zustand stores, FastAPI routers, dbt models, Dagster assets.
- Preserve code clarity, comments, and structure.

## Orders Domain

- Fields: `order_id`, `customer_id`, `order_ts`, `currency`, `subtotal`, `tax`, `total`, `items`, `source_file_id`, `ingest_run_id`, `dq_status`.
- DQ rules: required, type, non-negativity, `total >= subtotal + tax - 0.01`.
- Allowlist: USD, EUR, GBP, JPY, AUD, CAD, CHF.
- dbt: `stg_orders`, `fct_orders_daily`.
