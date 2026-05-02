import argparse
import sys
from gemini_ats_scorer.lib.parser import parse_pdf
from gemini_ats_scorer.lib.evaluator import evaluate_resume
from gemini_ats_scorer.models import Resume, JobDescription
from gemini_ats_scorer.logger import logger
from gemini_ats_scorer.errors import GeminiAtsScorerError

def main(args=None):
    if args is None:
        args = sys.argv[1:]
        
    parser = argparse.ArgumentParser(description="Gemini ATS Scorer")
    parser.add_argument("--resume", required=True, help="Path to candidate's PDF resume")
    parser.add_argument("--job", required=True, help="Path to job description text file")
    parser.add_argument("--format", choices=["text", "json"], default="text", help="Output format")
    
    parsed_args = parser.parse_args(args)
    
    try:
        logger.info(f"Parsing resume: {parsed_args.resume}")
        resume_text = parse_pdf(parsed_args.resume)
        resume = Resume(file_path=parsed_args.resume, extracted_text=resume_text)
        
        logger.info(f"Reading job description: {parsed_args.job}")
        with open(parsed_args.job, 'r', encoding='utf-8') as f:
            job_text = f.read()
        job_description = JobDescription(source_text=job_text)
        
        logger.info("Evaluating resume against job description using Gemini...")
        result = evaluate_resume(resume, job_description)
        
        if parsed_args.format == "json":
            print(result.model_dump_json(indent=2))
        else:
            print(f"\nScore: {result.score}/100")
            print(f"\nSummary: {result.summary}")
            print("\nStrengths:")
            for s in result.strengths:
                print(f"- {s}")
            print("\nWeaknesses:")
            for w in result.weaknesses:
                print(f"- {w}")
                
    except GeminiAtsScorerError as e:
        logger.error(str(e))
        sys.exit(1)
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
