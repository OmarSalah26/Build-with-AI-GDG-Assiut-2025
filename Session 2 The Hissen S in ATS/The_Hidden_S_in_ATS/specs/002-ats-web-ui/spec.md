# Feature Specification: ATS Web UI

**Feature Branch**: `002-ats-web-ui`  
**Created**: 2026-05-01  
**Status**: Draft  
**Input**: User description: "I want to build a UI to run the application"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Evaluate Candidate via Web Interface (Priority: P1)

As a recruiter or hiring manager, I want to upload a candidate's resume and job description through a web browser so that I can easily obtain an AI-generated match score without using a command-line interface.

**Why this priority**: A graphical user interface is essential for non-technical users to access the core value of the ATS Scorer tool.

**Independent Test**: Can be fully tested by opening the web application in a browser, submitting a sample PDF and job description text, and visually verifying the evaluation results on the screen.

**Acceptance Scenarios**:

1. **Given** the user is on the main application page, **When** they upload a valid PDF resume and enter a job description, and click "Evaluate", **Then** the application displays a loading indicator, processes the request, and renders the score, strengths, weaknesses, and summary.
2. **Given** the user attempts to evaluate without providing a resume, **When** they click "Evaluate", **Then** the UI prevents submission and displays a clear validation error.
3. **Given** the backend encounters an error (e.g., unreadable PDF), **When** the evaluation completes, **Then** the UI displays the error message clearly to the user.

---

### Edge Cases

- What happens if the user uploads a very large PDF or non-PDF file? (The UI should validate file type and size before submission).
- How does the UI handle long evaluation times from the AI service? (Must ensure the browser does not timeout and clearly shows progress).
- How does the UI display extremely long job descriptions or extremely detailed feedback? (Should use scrollable containers or expandable sections).

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST provide a graphical web interface accessible via a standard web browser.
- **FR-002**: System MUST provide a file upload mechanism restricted to PDF files for the resume.
- **FR-003**: System MUST provide a text input area (and optionally a file upload) for the job description.
- **FR-004**: System MUST clearly indicate processing state (e.g., loading spinner) while the evaluation is running.
- **FR-005**: System MUST display the final score prominently, along with structured lists for strengths and weaknesses, and the summary text.
- **FR-006**: System MUST handle validation errors and processing errors by displaying user-friendly error messages on the screen.
- **FR-007**: System MUST handle evaluation history by saving history to a database so users can view past scores.
- **FR-008**: System MUST secure access by remaining publicly/internally accessible without authentication.

### Key Entities

- **EvaluationSession**: Represents the current user's interaction session, containing the uploaded files and inputs.
- **UIState**: Represents the current state of the interface (e.g., Idle, Uploading, Evaluating, Error, Results).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can successfully upload a file, submit the form, and view results entirely within the web interface without using the terminal.
- **SC-002**: The UI responds to user input (e.g., clicking buttons, validations) in under 1 second.
- **SC-003**: 100% of API errors or processing failures are caught and displayed as readable messages in the UI, rather than crashing the application.

## Assumptions

- The existing underlying Python library (`gemini_ats_scorer.lib`) will be reused to perform the actual parsing and evaluation.
- Users will access the UI from modern desktop web browsers (mobile responsiveness is a nice-to-have but not strict for v1).
- The application will be hosted in an environment where the Google Gemini API key is securely configured on the server.
