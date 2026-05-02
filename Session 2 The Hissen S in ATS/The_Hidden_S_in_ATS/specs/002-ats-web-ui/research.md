# Phase 0: Research & Decisions

## Decision 1: Web Framework
- **Decision**: Streamlit
- **Rationale**: The core logic is built in Python. Streamlit allows us to rapidly build an interactive, data-driven web application entirely in Python without maintaining a separate frontend (React/Vue) and backend (FastAPI/Flask) stack. This aligns perfectly with building a simple MVP wrapper.
- **Alternatives considered**: 
  - FastAPI + React (Too complex for the MVP scope)
  - Gradio (Slightly less flexible for building multi-page dashboard-like interfaces compared to Streamlit)

## Decision 2: Database Storage
- **Decision**: SQLite
- **Rationale**: The spec requires saving evaluation history, but the tool is designed for local/internal usage without authentication. SQLite provides zero-configuration, file-based persistence that requires no external server setup, keeping the application lightweight.
- **Alternatives considered**: 
  - PostgreSQL/MySQL (Overkill, requires external server infrastructure)
  - JSON flat files (Difficult to query or manage as history grows)
