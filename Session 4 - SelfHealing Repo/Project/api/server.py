import os
import sys

# Ensure the root directory is in the path to import core/agents
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv

from core.orchestrator import AntigravityAgency

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

agency = None

def get_agency():
    global agency
    if agency is None:
        agency = AntigravityAgency()
    return agency

class ScanRequest(BaseModel):
    repo_name: str

class RefactorRequest(BaseModel):
    repo_name: str
    file_path: str

class PushFile(BaseModel):
    file_path: str
    content: str

class PushRequest(BaseModel):
    repo_name: str
    branch_name: str
    files: List[PushFile]

@app.post("/api/scan")
async def scan_repo(req: ScanRequest):
    try:
        a = get_agency()
        # Clean up the repo name if they pasted a full URL
        repo_name = req.repo_name.strip()
        if "github.com/" in repo_name:
            repo_name = repo_name.split("github.com/")[-1].strip("/")
            
        print(f"API received request to scan repository: '{repo_name}'")
        
        if "/" not in repo_name:
            raise ValueError(f"Invalid format: '{repo_name}'. Please include the username/organization (e.g., 'TawadrosGamal/Hotel-reservation-system-java-').")
            
        all_files = a.github.get_all_files(repo_name)
        extensions = ('.py', '.java', '.js', '.ts', '.cpp', '.c', '.go', '.cs', '.php', '.rb', '.html', '.css')
        source_files = [f for f in all_files if f.lower().endswith(extensions)]
        
        print(f"Found {len(all_files)} total files, {len(source_files)} source files.")
        return {"repo_name": repo_name, "source_files": source_files, "total_files": len(all_files)}
    except Exception as e:
        print(f"Error scanning repository: {e}")
        # Make the error message more readable if it's a GitHub 404
        error_msg = str(e)
        if "404" in error_msg:
            error_msg = f"Repository '{req.repo_name}' not found. Please check the name or ensure your GITHUB_TOKEN has access to it."
        raise HTTPException(status_code=500, detail=error_msg)

@app.post("/api/refactor")
async def refactor_file(req: RefactorRequest):
    try:
        a = get_agency()
        report = await a.run_pipeline(repo_name=req.repo_name, file_path=req.file_path)
        return report.model_dump() # Pydantic v2
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/push")
async def push_changes(req: PushRequest):
    try:
        a = get_agency()
        a.github.create_branch(req.repo_name, req.branch_name)
        for f in req.files:
            a.github.update_repo_file(req.repo_name, f.file_path, f.content, branch=req.branch_name)
        return {"status": "success", "branch": req.branch_name}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
