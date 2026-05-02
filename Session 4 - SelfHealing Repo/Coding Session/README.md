# Project Sentinel: The Autonomous Codebase Maintenance Agency

## Project Overview
Project Sentinel is a multi-agentic system designed to ingest remote GitHub repositories, analyze the architecture, refactor for modernization, and autonomously generate test suites. It treats code as a dynamic, self-healing organism.

This project merges the "Sentinel" concept (identifying and fixing technical debt) with a robust repository-wide autonomous workflow, presented through a modern Web Application.

## Key Features
- **Repository-Wide Scanning**: Connects to a GitHub repository, recursively scans all folders, and automatically filters for valid source code files (e.g., `.java`, `.py`, `.js`).
- **Full-Stack Web Interface**: A sleek, premium glassmorphism React (Vite) UI powered by a fast Python FastAPI backend.
- **Multi-Agent Architecture**: Employs distinct agents tailored for specific tasks, utilizing the Gemini 2.5 models (`gemini-2.5-flash` for speed, `gemini-2.5-pro` for deep reasoning).
- **Interactive Review**: Watch the AI refactor code in real-time, view side-by-side diffs, and inspect the generated unit tests directly in your browser.
- **Automated Branching & Pushing**: Once reviewed, specify a dynamic branch name (e.g., `enhac/AI-step-1`) and push all refactored files back to the GitHub repository safely with a single click.

## Agent Workforce
1. **GitHub Agent (IO Specialist)**: Uses `PyGithub` to fetch file contents, scan directories, create branches, and push commits.
2. **Linguist Agent**: Analyzes file extensions to determine the programming language and provide context.
3. **Archeologist Agent**: Uses **Gemini 2.5 Flash** to scan the original code and identify bugs, technical debt, and anti-patterns.
4. **Architect Agent**: Uses **Gemini 2.5 Pro** to refactor the code based on the Archeologist's findings.
5. **Test Agent**: Uses **Gemini 2.5 Pro** to generate a comprehensive unit test suite for the newly refactored code.

## Tech Stack & Dependencies
### Backend (Python)
- `fastapi` & `uvicorn`: High-performance API server.
- `google-genai`: The official modern Google Gen AI SDK.
- `PyGithub`: For interacting with the GitHub API.
- `pydantic`: For strictly typing the schemas (e.g., `CodeIssueList`, `RefactorProposal`).
- `python-dotenv`: For managing API keys.

### Frontend (JavaScript)
- `React` & `Vite`: Fast development environment and UI library.
- Vanilla CSS with modern aesthetics (Glassmorphism, dark mode, CSS Grid).

## Project Structure
```text
Sentinel/
├── agents/
│   ├── archeologist_agent.py  # Gemini 2.5 Flash bug scanner
│   ├── architect_agent.py     # Gemini 2.5 Pro refactorer
│   ├── github_agent.py        # PyGithub repository interactions
│   ├── linguist_agent.py      # Language detection
│   └── test_agent.py          # Gemini 2.5 Pro test generator
├── api/
│   └── server.py              # FastAPI endpoints (/api/scan, /api/refactor, /api/push)
├── core/
│   ├── orchestrator.py        # SentinelAgency: Manages the agentic loop
│   └── schemas.py             # Pydantic models for structured outputs
├── frontend/                  # React (Vite) Web Application
│   ├── src/App.jsx            # Main interactive dashboard UI
│   └── src/index.css          # Premium glassmorphism design system
├── .env                       # GITHUB_TOKEN and GEMINI_API_KEY
├── main.py                    # Legacy CLI Entry point (optional)
└── requirements.txt           # Python Dependencies
```

## How to Build & Run
*(Instructions for future agents or developers to recreate this environment)*

You will need two terminal windows to run the application.

1. **Environment Setup**:
   - Create a `.env` file in the root directory with `GEMINI_API_KEY` and `GITHUB_TOKEN`.

2. **Start Backend**:
   ```bash
   pip install -r requirements.txt
   uvicorn api.server:app --reload
   ```

3. **Start Frontend**:
   In a new terminal window:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

4. **Interaction Flow**:
   - Open the browser to `http://localhost:5173`.
   - Provide the target GitHub repository format exactly as `Username/RepoName`.
   - The system will count the source code files and present them.
   - Click "Start Autonomous Refactoring" to process each file.
   - Click any file to view the refactored code and tests.
   - Finally, provide a branch name and push all changes back to GitHub.

## Important Implementation Details for AI Agents Recreating This:
- **Pydantic Schemas**: When using `google-genai` structured outputs (`response_schema`), ensure the top-level schema is a standard Pydantic `BaseModel`. Do not use generic lists (like `List[CodeIssue]`) directly; wrap them in a parent class (like `CodeIssueList`).
- **Gemini Models**: Use `gemini-2.5-flash` for fast scanning and `gemini-2.5-pro` for reasoning/coding.
- **GitHub API**: The format must be `Owner/Repo`. When pushing files, check if the branch exists first. If not, branch off `repo.default_branch`.
- **CORS Setup**: Ensure `CORSMiddleware` is configured in `api/server.py` to allow the React frontend to communicate with the FastAPI backend.
