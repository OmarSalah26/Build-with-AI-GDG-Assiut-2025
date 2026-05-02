# Tasks: ATS Web UI

**Input**: Design documents from `/specs/002-ats-web-ui/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, quickstart.md

**Tests**: TDD approach is mandated by the project constitution. Tests must be implemented and fail before core logic.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Update `pyproject.toml` to include Streamlit as a `ui` optional dependency
- [x] T002 Create UI directory structure (`src/gemini_ats_scorer/ui/` and `tests/ui/`)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T003 Setup SQLite database connection and table schema creation logic in `src/gemini_ats_scorer/ui/db.py`

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Evaluate Candidate via Web Interface (Priority: P1) 🎯 MVP

**Goal**: Upload candidate's resume and job description through a web browser to obtain an AI-generated match score, with the results saved to a database.

**Independent Test**: Run `streamlit run src/gemini_ats_scorer/ui/app.py`, upload a test PDF and enter text, verify the result appears on screen and is saved to the SQLite DB.

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T004 [P] [US1] Unit test for database operations in `tests/ui/test_db.py`
- [x] T005 [P] [US1] Streamlit AppTest for UI flow in `tests/ui/test_app.py`

### Implementation for User Story 1

- [x] T006 [P] [US1] Implement CRUD operations for `EvaluationRecord` in `src/gemini_ats_scorer/ui/db.py`
- [x] T007 [US1] Implement Streamlit UI components and layout in `src/gemini_ats_scorer/ui/views.py` (depends on T006)
- [x] T008 [US1] Implement main Streamlit application entry point in `src/gemini_ats_scorer/ui/app.py` integrating the core evaluator and DB (depends on T007)

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently via the browser.

---

## Phase 4: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T009 Code cleanup, typing validation, and formatting (e.g., using `black` and `mypy`)
- [x] T010 Run `quickstart.md` validation locally to ensure the web app starts and works end-to-end as documented.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Tests MUST be written and FAIL before implementation
- Database operations before UI views
- Views before main application wiring
- Core implementation before integration

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- All tests for a user story marked [P] can run in parallel
- Database logic and isolated view components can be developed in parallel

---

## Parallel Example: User Story 1

```bash
# Launch independent implementation layers:
Task: "Implement CRUD operations for EvaluationRecord in src/gemini_ats_scorer/ui/db.py"
Task: "Implement Streamlit UI components and layout in src/gemini_ats_scorer/ui/views.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently via browser
5. Deploy/demo if ready

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Verify tests fail before implementing
- Commit after each task or logical group
