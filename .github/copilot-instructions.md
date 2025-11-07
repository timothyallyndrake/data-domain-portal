<!-- 🔄 SYNC NOTICE — DO NOT REMOVE OR MODIFY -->

# Synchronization Requirement

This file (`.github/copilot-instructions.md`) is one of three **synchronized AI instruction files**:

- `.github/copilot-instructions.md`
- `GEMINI.md`
- `CODEX.md`

Any change made to **any** of these files **must be reflected identically** in the others to keep all AI assistants aligned on the same project intent and stack details.

⚠️ **Do not remove, rename, or alter this notice.** It safeguards cross-agent consistency.

**README Sync Rule:** The repository’s `README.md` is a canonical source of truth for goals, stack, and run instructions. Any change to this file **must also be reflected** in the AI instruction files (`.github/copilot-instructions.md`, `GEMINI.md`, `CODEX.md`) where applicable, so all assistants and contributors share the same context.

<!-- 🔄 END SYNC NOTICE -->

# GitHub Copilot — Workspace Instructions

## Project Goal (North Star)

Build a **Data Domain Portal**: a self-service data platform for mapping CSV → canonical models, validating data, triggering ingestion, orchestrating ELT into **Snowflake** (via **Dagster** + **dbt**), and visualizing analytics. Primary demo domain: **Orders**. Architecture must remain **generic** so new domains can be added with minimal changes.

## Tech Stack (authoritative)

- **Frontend**: React + TypeScript, MUI, Zustand, React Router, Hooks + Context API
- **Backend**: FastAPI (asyncio-first), Pydantic, SQLAlchemy (async), Alembic
- **Messaging**: Apache Kafka (KRaft)
- **Cache/Session**: Redis
- **Analytics**: Snowflake (stages, COPY INTO), dbt (staging+marts+tests)
- **Orchestration**: Dagster (assets, sensors, schedules)
- **Auth**: Keycloak (OIDC, SPA PKCE); JWT
- **Policy**: Casbin (RBAC + PBAC/ABAC-lite)
- **Testing**: Jest/RTL, Pytest/httpx, Playwright E2E, dbt tests, Dagster asset tests
- **Observability**: OpenTelemetry → Jaeger/Grafana (local)
- **Infra (local)**: Docker Compose; Terraform (Docker provider later)

## Architectural Rules

1. **Separation of concerns** — web, api, worker, and dagster remain distinct.
2. **Async everywhere** in Python services.
3. **OpenAPI-first**: typed requests/responses; consistent `/v1` routes.
4. **Generic domains** — “Orders” is just the example.
5. **UTC in storage**, localize in UI.
6. **Currency allowlist** with ε = 0.01 tolerance.

## Coding Standards

### React

- Hooks + Context + Zustand.
- Minimize re-renders using selectors and memoization.
- Contexts: Auth, Policy, Theme.
- Perf: `memo`, `useCallback`, `useMemo`.
- MUI DataGrid for data-heavy lists.

### HTTP Client

- Use native `fetch` + lightweight wrapper (base URL, JSON, headers, retries).
- Types generated from OpenAPI with `openapi-typescript`.

### FastAPI

- `async def` routes, tagged, Pydantic v2 models.
- 401/403/422/5xx standardized.
- Strong OpenAPI examples.

### Persistence

- SQLAlchemy async + Alembic migrations.
- Tables: `domains`, `mappings`, `ingest_runs`, `orders`.

### Messaging

- Kafka topics: `ingestion.requests`, `ingestion.completed`, `dq.reports`.

### Security

- OIDC (Keycloak), JWT verification, Casbin for policy.
- PII masking middleware: redact sensitive fields in logs.

### Testing

- **Web:** Jest/RTL + MSW, Playwright E2E.
- **API:** Pytest + httpx.AsyncClient + Schemathesis.
- **Worker:** Kafka→Postgres integration tests.
- **dbt:** schema tests.
- **Dagster:** asset and job selection tests.

### Observability

- Trace propagation (OpenTelemetry) and structured logging.

## Guidance for Copilot

- ✅ Generate code following these patterns (React, FastAPI, dbt, Dagster).
- ✅ Keep code explicit and explain design choices in comments.
- ❌ Don’t introduce new frameworks (e.g., Axios, Redux).
- ❌ Don’t collapse services or hide commands behind scripts.

## Domain Example (Orders)

- Required fields: order_id, customer_id, order_ts, currency, total.
- `total >= subtotal + tax - 0.01`.
- Allowlist: USD, EUR, GBP, JPY, AUD, CAD, CHF.
- dbt models: `stg_orders`, `fct_orders_daily`.
