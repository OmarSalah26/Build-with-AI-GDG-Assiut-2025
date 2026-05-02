# Phase 0: Research & Decisions

## Clarification 1: Feedback Detail
- **Decision**: The system will provide detailed reasoning and feedback alongside the numerical score.
- **Rationale**: A raw numerical score lacks actionable insights for the recruiter. Gemini can easily generate structured feedback (strengths, weaknesses, match analysis) along with the score.
- **Alternatives considered**: Raw score only. Rejected because it limits the value provided by the ATS.

## Clarification 2: Interface Type
- **Decision**: The project will be built as a standalone Python library exposed via a CLI tool.
- **Rationale**: Aligns with the Project Constitution (I. Library-First, II. CLI Interface).
- **Alternatives considered**: Web Application. Rejected because the constitution strictly requires starting as a CLI/library.

## Clarification 3: Scanned PDFs
- **Decision**: Reject scanned PDFs with a clear error message.
- **Rationale**: Keeps the initial scope manageable and avoids introducing heavy OCR dependencies for the MVP.
- **Alternatives considered**: Implement OCR. Rejected due to complexity for version 1.

## Technology Choices
- **Language**: Python 3.11+
- **Dependencies**: `google-generativeai` (Gemini API), `PyMuPDF` / `fitz` (fast PDF parsing), `pydantic` (structured output from Gemini), `pytest` (TDD).
