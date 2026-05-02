import os
import asyncio
from typing import Optional
from google import genai
from rich.console import Console

from core.schemas import AntigravityReport, RefactorProposal
from agents.github_agent import GithubAgent
from agents.linguist_agent import LinguistAgent
from agents.archeologist_agent import ArcheologistAgent
from agents.architect_agent import ArchitectAgent
from agents.test_agent import TestAgent

console = Console()

class AntigravityAgency:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set")
            
        self.client = genai.Client(api_key=api_key)
        self.github = GithubAgent()
        self.linguist = LinguistAgent()
        self.archeologist = ArcheologistAgent(self.client)
        self.architect = ArchitectAgent(self.client)
        self.tester = TestAgent(self.client)

    async def run_pipeline(self, repo_name: Optional[str] = None, file_path: Optional[str] = None, local_code: Optional[str] = None) -> AntigravityReport:
        console.print("[bold blue]🚀 Project Antigravity Activated...[/bold blue]")

        # 1. Fetch
        raw_code = ""
        if repo_name and file_path:
            console.print(f"[cyan]Fetching {file_path} from {repo_name}...[/cyan]")
            raw_code = self.github.fetch_repo_file(repo_name, file_path)
        elif local_code:
            console.print("[cyan]Using provided local code snippet...[/cyan]")
            raw_code = local_code
            file_path = "local_snippet" # mock for linguist
        else:
            raise ValueError("Must provide either a repo/file path or local code.")

        # 2. Identify Language
        language = self.linguist.detect_language(raw_code, file_path or "")
        console.print(f"[green]Detected Language:[/green] {language}")

        # 3. Discovery Phase (Archeologist)
        console.print("[cyan]Archeologist Agent scanning for issues...[/cyan]")
        issues = await self.archeologist.scan(raw_code)
        
        console.print(f"[yellow]Found {len(issues)} potential issues.[/yellow]")
        for i, issue in enumerate(issues):
            console.print(f"  [bold]Issue {i+1}:[/bold] {issue.issue} (Severity: {issue.severity})")

        # 4. Action Phase (Architect)
        console.print("[cyan]Architect Agent refactoring code...[/cyan]")
        issues_text = "\n".join([f"- {i.issue} ({i.severity})" for i in issues])
        
        proposal = await self.architect.refactor(raw_code, issues_text, language)
        console.print("[green]Refactoring complete.[/green]")
        console.print(f"[dim]Explanation: {proposal.explanation}[/dim]")

        # 5. Validation Phase (Test Agent)
        console.print("[cyan]Test Agent generating unit tests...[/cyan]")
        tests = await self.tester.generate_tests(proposal.proposed_code, language)
        console.print("[green]Test suite generated.[/green]")

        return AntigravityReport(
            language=language,
            original_code=raw_code,
            refactored_code=proposal.proposed_code,
            unit_tests=tests,
            issues_found=issues
        )
