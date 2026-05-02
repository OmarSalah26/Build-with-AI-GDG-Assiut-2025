from pydantic import BaseModel, Field

class Resume(BaseModel):
    file_path: str
    extracted_text: str

class JobDescription(BaseModel):
    source_text: str

class EvaluationResult(BaseModel):
    score: int = Field(ge=0, le=100)
    strengths: list[str]
    weaknesses: list[str]
    summary: str
