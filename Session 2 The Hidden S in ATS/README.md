# Build with AI — GDG Assiut 2025

Welcome to the GDG Assiut **Build with AI 2025** repository!

## 📂 Repository Structure

```text
Build-with-AI-GDG-Assiut-2025/
│
├── 📂 Attendee-Projects/                 # Projects built by the community 🚀
│   └── The_Hidden_S_in_ATS/              # Gemini ATS Scorer
│       ├── src/gemini_ats_scorer/
│       │   ├── core/                     # Core evaluation logic & Gemini integration
│       │   ├── cli/                      # Command-Line Interface
│       │   └── ui/                       # Streamlit Web UI
│       ├── tests/                        # Unit & integration tests
│       ├── specs/                        # Spec Kit specifications & plans
│       └── pyproject.toml                # Project config & dependencies
│
└── 📜 README.md                          # You are here!
```

---

## 🚀 Attendee Projects

### The Hidden S in ATS (Gemini ATS Scorer)

An intelligent, privacy-first ATS (Applicant Tracking System) scoring application that evaluates candidate resumes against job descriptions using **Google Gemini**.

#### Features

- **AI-Driven Analysis** — Uses Google Gemini to score candidates based on their alignment with job descriptions.
- **Privacy-First (PII Redaction)** — Automatically redacts PII using Microsoft Presidio before sending data to the LLM.
- **Dual Interface** — Streamlit Web UI + Command-Line Interface.
- **Evaluation History** — Persists results in a local SQLite database for tracking and comparison.
- **PDF Parsing** — Robust text extraction from uploaded resume PDFs.

#### 🛠️ Built With

- **Antigravity** — Agentic AI coding assistant by Google DeepMind.
- **Spec Kit** — Specification management & Test-First development workflow.

#### 🏃‍♂️ How to Run

```bash
cd Attendee-Projects/The_Hidden_S_in_ATS
streamlit run src/gemini_ats_scorer/ui/app.py
```
