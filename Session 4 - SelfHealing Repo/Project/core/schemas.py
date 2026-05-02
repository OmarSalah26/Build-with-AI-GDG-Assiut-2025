from typing import List
from pydantic import BaseModel, Field

class CodeIssue(BaseModel):
    issue: str = Field(description="Description of technical debt, bug, or anti-pattern")
    severity: str = Field(description="High/Medium/Low")

class CodeIssueList(BaseModel):
    issues: List[CodeIssue] = Field(description="List of issues found")


class RefactorProposal(BaseModel):
    explanation: str = Field(description="Explanation of the proposed changes")
    proposed_code: str = Field(description="The refactored source code")

class AntigravityReport(BaseModel):
    language: str = Field(description="Detected programming language")
    original_code: str = Field(description="Original source code")
    refactored_code: str = Field(description="Refactored source code")
    unit_tests: str = Field(description="Generated unit tests")
    issues_found: List[CodeIssue] = Field(description="List of issues identified before refactoring")
