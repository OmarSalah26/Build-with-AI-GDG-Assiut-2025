# Implementation Plan: ATS Web UI

**Branch**: `002-ats-web-ui` | **Date**: 2026-05-01 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/002-ats-web-ui/spec.md`

## Summary

Build a graphical web interface for the Gemini ATS Scorer to allow users to upload resumes, enter job descriptions, and view AI-generated match scores. The UI will persist evaluation history to a local database.

## Technical Context

**Language/Version**: Python 3.11  
**Primary Dependencies**: Streamlit, SQLite3, `gemini_ats_scorer` (internal lib)  
**Storage**: SQLite  
**Testing**: pytest, Streamlit AppTest  
**Target Platform**: Web Browser (Desktop)
**Project Type**: Web Application (UI wrapper)  
**Performance Goals**: UI responds in <1s (excluding API latency)  
**Constraints**: Requires `GEMINI_API_KEY`  
**Scale/Scope**: Local usage, single/multi-user without auth  

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Library-First**: The UI acts as a consumer of the existing `gemini_ats_scorer` library. PASS.
- **Test-First**: Tests will be written for the UI and DB layer before implementation. PASS.

## Project Structure

### Documentation (this feature)

```text
specs/002-ats-web-ui/
├── plan.md              # This file (/speckit-plan command output)
├── research.md          # Phase 0 output (/speckit-plan command)
├── data-model.md        # Phase 1 output (/speckit-plan command)
├── quickstart.md        # Phase 1 output (/speckit-plan command)
└── tasks.md             # Phase 2 output (/speckit-tasks command - NOT created by /speckit-plan)
```

### Source Code (repository root)

```text
src/gemini_ats_scorer/
├── lib/
├── models.py
├── cli.py
└── ui/               # [NEW] Web UI module
    ├── app.py        # Streamlit entry point
    ├── views.py      # UI components and layout
    └── db.py         # SQLite persistence layer

tests/
├── integration/
├── unit/
└── ui/               # [NEW] UI tests
```

**Structure Decision**: A new `ui` module will be added to the existing package, maintaining the single-project structure while keeping the UI code isolated from the core library.
