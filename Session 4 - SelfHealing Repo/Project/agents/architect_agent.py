from google import genai
from google.genai import types
from core.schemas import RefactorProposal

class ArchitectAgent:
    def __init__(self, client: genai.Client):
        self.client = client

    async def refactor(self, context_code: str, issues: str, language: str) -> RefactorProposal:
        """Fixes problems using the reasoning-heavy Pro model."""
        prompt = f"""
        Language: {language}
        
        Issues identified:
        {issues}
        
        Original Code context:
        {context_code}
        
        Please refactor the original code to fix the issues mentioned, while maintaining the intended functionality.
        """
        response = await self.client.aio.models.generate_content(
            model="gemini-2.5-pro",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=RefactorProposal,
                system_instruction="You are a world-class Developer. Provide the explanation and the complete refactored source code."
            )
        )
        return response.parsed
