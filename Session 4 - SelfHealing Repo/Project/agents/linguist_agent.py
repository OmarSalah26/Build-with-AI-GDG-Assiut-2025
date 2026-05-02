class LinguistAgent:
    def detect_language(self, code_snippet: str, file_path: str = "") -> str:
        """
        A simple linguist agent.
        In a real scenario, this could use Gemini or Pygments to detect language.
        For this demo, we'll try to infer from file extension or fallback.
        """
        if file_path.endswith(".py"):
            return "Python"
        elif file_path.endswith(".js"):
            return "JavaScript"
        elif file_path.endswith(".ts"):
            return "TypeScript"
        elif file_path.endswith(".go"):
            return "Go"
        elif file_path.endswith(".java"):
            return "Java"
        elif file_path.endswith(".cpp") or file_path.endswith(".cc"):
            return "C++"
        else:
            return "Unknown (Fallback to inference by Architect)"
