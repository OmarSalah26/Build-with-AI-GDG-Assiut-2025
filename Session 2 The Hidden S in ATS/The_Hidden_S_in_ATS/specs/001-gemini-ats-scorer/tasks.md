# Tasks: Gemini ATS Scorer

**Input**: Design documents from `/specs/001-gemini-ats-scorer/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: TDD approach is mandated by the project constitution. Tests must be implemented and fail before core logic.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure per implementation plan (src/, tests/ directories)
- [x] T002 Initialize Python project with `pyproject.toml` and dependencies (`google-generativeai`, `PyMuPDF`, `pydantic`, `pytest`)
- [x] T003 [P] Configure pytest in `pytest.ini`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 Setup custom exception classes in `src/gemini_ats_scorer/errors.py` (e.g., PDFParseError, EvaluatorError)
- [x] T005 [P] Setup base logging configuration in `src/gemini_ats_scorer/logger.py`

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Evaluate Resume against Job Description (Priority: P1) 🎯 MVP

**Goal**: Extract text from a PDF resume, evaluate it against a text job description via Gemini API, and return a structured score with feedback.

**Independent Test**: Provide a sample PDF and TXT file to the CLI tool and verify a numerical score and reasoning is returned.

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T006 [P] [US1] Contract test for CLI interface in `tests/integration/test_cli.py`
- [x] T007 [P] [US1] Unit test for PDF parsing in `tests/unit/test_parser.py`
- [x] T008 [P] [US1] Unit test for Gemini evaluation in `tests/unit/test_evaluator.py`
- [x] T009 [P] [US1] Unit test for Pydantic models in `tests/unit/test_models.py`

### Implementation for User Story 1

- [x] T010 [P] [US1] Create Resume, JobDescription, and EvaluationResult models in `src/gemini_ats_scorer/models.py`
- [x] T011 [P] [US1] Implement PDF parsing logic in `src/gemini_ats_scorer/lib/parser.py` (rejecting scanned images)
- [x] T012 [US1] Implement Gemini API evaluation logic in `src/gemini_ats_scorer/lib/evaluator.py` (depends on T010)
- [x] T013 [US1] Implement CLI interface in `src/gemini_ats_scorer/cli.py` handling `--resume`, `--job`, and `--format` (depends on T011, T012)
- [x] T014 [US1] Add package entry point in `src/gemini_ats_scorer/__main__.py`

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T015 Code cleanup, typing validation, and formatting (e.g., using `black` and `mypy`)
- [x] T016 Run quickstart.md validation locally to ensure tool works end-to-end as documented

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
- Models before services
- Services before endpoints (CLI)
- Core implementation before integration

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- All tests for a user story marked [P] can run in parallel
- Models and Parsing logic within a story marked [P] can run in parallel

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
Task: "Contract test for CLI interface in tests/integration/test_cli.py"
Task: "Unit test for PDF parsing in tests/unit/test_parser.py"
Task: "Unit test for Gemini evaluation in tests/unit/test_evaluator.py"

# Launch independent implementation layers:
Task: "Create models in src/gemini_ats_scorer/models.py"
Task: "Implement PDF parsing logic in src/gemini_ats_scorer/lib/parser.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Verify tests fail before implementing
- Commit after each task or logical group
