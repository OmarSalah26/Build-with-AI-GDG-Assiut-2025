from google import genai
import json
import os
from gemini_ats_scorer.models import Resume, JobDescription, EvaluationResult
from gemini_ats_scorer.errors import EvaluatorError

def evaluate_resume(resume: Resume, job_description: JobDescription) -> EvaluationResult:
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise EvaluatorError("GEMINI_API_KEY environment variable is not set")
        
    client = genai.Client(api_key=api_key)

    
    prompt = f"""
    You are an expert HR recruiter. Evaluate the following resume against the job description.
    Provide a score from 0 to 100 based on how well the candidate matches the requirements.
    Also provide a list of strengths, a list of weaknesses, and a brief summary.
    
    You MUST output valid JSON strictly matching this schema:
    {{
        "score": 85,
        "strengths": ["string"],
        "weaknesses": ["string"],
        "summary": "string"
    }}
    
    Job Description:
    {job_description.source_text}
    
    Resume:
    {resume.extracted_text}
    """
    
    try:
        response = client.models.generate_content(
            model='gemini-3.1-flash-lite-preview',
            contents=prompt,
        )
        text = response.text
        # Clean markdown code block if present
        if text.startswith("```json"):
            text = text[7:]
        if text.startswith("```"):
            text = text[3:]
        if text.endswith("```"):
            text = text[:-3]
            
        data = json.loads(text.strip())
        return EvaluationResult(**data)
    except Exception as e:
        raise EvaluatorError(f"Failed to evaluate resume: {e}")
