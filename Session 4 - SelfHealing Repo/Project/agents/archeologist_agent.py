from typing import List
from google import genai
from google.genai import types
from core.schemas import CodeIssue, CodeIssueList

class ArcheologistAgent:
    def __init__(self, client: genai.Client):
        self.client = client

    async def scan(self, code_snippet: str) -> List[CodeIssue]:
        """Scans for problems using the fast Flash model."""
        response = await self.client.aio.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"Find bugs, technical debt, or bad practices in this code:\n\n{code_snippet}",
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=CodeIssueList,
                system_instruction="You are a strict SRE Auditor and Code Reviewer. Identify issues accurately."
            )
        )
        if not response.parsed or not hasattr(response.parsed, 'issues'):
            return []
        return response.parsed.issues

