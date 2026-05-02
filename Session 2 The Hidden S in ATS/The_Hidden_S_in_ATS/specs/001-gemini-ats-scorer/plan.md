# Implementation Plan: Gemini ATS Scorer

**Branch**: `001-gemini-ats-scorer` | **Date**: 2026-05-01 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-gemini-ats-scorer/spec.md`

**Note**: This template is filled in by the `/speckit-plan` command. See `.specify/templates/plan-template.md` for the execution workflow.

## Summary

Build a CLI tool and underlying Python library that takes a candidate's PDF resume and a job description (text) and uses the Google Gemini API to evaluate the match, providing a numerical score and detailed feedback.

## Technical Context

**Language/Version**: Python 3.11+
**Primary Dependencies**: `google-generativeai`, `PyMuPDF`, `pydantic`
**Storage**: N/A
**Testing**: `pytest`
**Target Platform**: CLI / Cross-platform
**Project Type**: Library and CLI tool
**Performance Goals**: Evaluation results in under 15 seconds.
**Constraints**: Requires internet connection for Gemini API. Fails fast on scanned (image-only) PDFs.
**Scale/Scope**: Small CLI application, processes one resume at a time.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Library-First**: Yes, the core logic will be in `gemini_ats_scorer/lib/`.
- **CLI Interface**: Yes, exposed via a CLI module.
- **Test-First**: Will follow TDD.
- **Integration Testing**: Tests will verify the CLI input/output and mock the Gemini API.

## Project Structure

### Documentation (this feature)

```text
specs/001-gemini-ats-scorer/
├── plan.md              # This file (/speckit-plan command output)
├── research.md          # Phase 0 output (/speckit-plan command)
├── data-model.md        # Phase 1 output (/speckit-plan command)
├── quickstart.md        # Phase 1 output (/speckit-plan command)
├── contracts/           # Phase 1 output (/speckit-plan command)
└── tasks.md             # Phase 2 output (/speckit-tasks command - NOT created by /speckit-plan)
```

### Source Code (repository root)

```text
src/
├── gemini_ats_scorer/
│   ├── __init__.py
│   ├── cli.py            # CLI interface
│   ├── lib/              # Core library
│   │   ├── parser.py     # PDF parsing logic
│   │   └── evaluator.py  # Gemini API integration
│   └── models.py         # Pydantic data models
tests/
├── integration/          # CLI and mock API tests
└── unit/                 # Parsing and data model tests
```

**Structure Decision**: Option 1: Single project structure (Library + CLI).

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| N/A | N/A | N/A |
