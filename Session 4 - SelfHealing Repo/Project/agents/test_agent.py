from google import genai

class TestAgent:
    def __init__(self, client: genai.Client):
        self.client = client

    async def generate_tests(self, refactored_code: str, language: str) -> str:
        """Generates unit tests for the refactored code."""
        prompt = f"""
        Write a comprehensive unit test suite for the following {language} code.
        Use industry-standard testing frameworks (e.g., pytest for Python, Jest for JS).
        
        CODE:
        {refactored_code}
        """
        response = await self.client.aio.models.generate_content(
            model="gemini-2.5-pro",
            contents=prompt,
            config=dict(
                system_instruction="You are an expert QA Automation Engineer. Output ONLY the test code without markdown block formatting if possible, or keep it clean."
            )
        )
        
        # Remove markdown formatting if present
        text = response.text
        if text.startswith("```"):
            lines = text.split("\n")
            if len(lines) > 2:
                return "\n".join(lines[1:-1])
        return text
