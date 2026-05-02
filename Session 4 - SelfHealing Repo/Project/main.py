import asyncio
import os
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax

from rich.prompt import Prompt, Confirm
from core.orchestrator import AntigravityAgency

load_dotenv() # Load environment variables from .env
console = Console()

async def main():
    console.print(Panel.fit("[bold magenta]🛸 Project Antigravity Demo[/bold magenta]", border_style="cyan"))
    
    # Ensure we have keys before running
    if not os.getenv("GEMINI_API_KEY"):
        console.print("[bold red]Error: GEMINI_API_KEY not found in .env file.[/bold red]")
        return
    if not os.getenv("GITHUB_TOKEN"):
        console.print("[bold red]Error: GITHUB_TOKEN not found in .env file.[/bold red]")
        return

    agency = AntigravityAgency()
    
    repo_name = Prompt.ask("\n[bold cyan]Enter GitHub Repository (e.g., TawadrosGamal/Hotel-reservation-system-java-)[/bold cyan]")
    
    # Clean up the repo name if they pasted a full URL
    if "github.com/" in repo_name:
        repo_name = repo_name.split("github.com/")[-1].strip("/")
        
    console.print(f"[cyan]Scanning {repo_name} for files...[/cyan]")
    all_files = agency.github.get_all_files(repo_name)
    
    # Filter for standard source code files to avoid binaries, images, etc.
    extensions = ('.py', '.java', '.js', '.ts', '.cpp', '.c', '.go', '.cs', '.php', '.rb', '.html', '.css')
    source_files = [f for f in all_files if f.lower().endswith(extensions)]
    
    if not source_files:
        console.print("[yellow]No source code files found in the repository.[/yellow]")
        return
        
    console.print(f"\n[bold yellow]Found {len(source_files)} source code files out of {len(all_files)} total files.[/bold yellow]")
    
    proceed = Confirm.ask(f"[bold yellow]Do you want to proceed with analyzing and refactoring all {len(source_files)} files?[/bold yellow]")
    if not proceed:
        console.print("[cyan]Operation cancelled by user.[/cyan]")
        return

    # Track successfully refactored files for pushing later
    refactored_files = {}
    local_out_dir = "refactored_output"
    
    if not os.path.exists(local_out_dir):
        os.makedirs(local_out_dir)
        
    for file_path in source_files:
        console.print(f"\n[bold magenta]{'='*40}[/bold magenta]")
        console.print(f"[bold magenta]🛸 Processing: {file_path}[/bold magenta]")
        console.print(f"[bold magenta]{'='*40}[/bold magenta]")
        try:
            # Run the pipeline
            report = await agency.run_pipeline(repo_name=repo_name, file_path=file_path)
            
            # Save the refactored code locally
            local_file_path = os.path.join(local_out_dir, os.path.basename(file_path))
            with open(local_file_path, "w", encoding="utf-8") as f:
                f.write(report.refactored_code)
                
            console.print(f"[bold green]Saved locally to: {local_file_path}[/bold green]")
            
            # Save tests too
            local_test_path = os.path.join(local_out_dir, f"test_{os.path.basename(file_path)}")
            with open(local_test_path, "w", encoding="utf-8") as f:
                f.write(report.unit_tests)
            
            refactored_files[file_path] = report.refactored_code
                
        except Exception as e:
            console.print(f"[bold red]An error occurred while processing {file_path}: {e}[/bold red]")
            continue
            
    if not refactored_files:
        console.print("[yellow]No files were successfully refactored.[/yellow]")
        return
        
    console.print("\n")
    should_push = Confirm.ask(f"[bold yellow]All refactored files are saved in '{local_out_dir}'. Do you want to push these {len(refactored_files)} files to GitHub?[/bold yellow]")
    
    if should_push:
        branch_name = Prompt.ask("[bold cyan]Enter the branch name to push to[/bold cyan]", default="enhac/AI-step-1")
        try:
            console.print(f"[cyan]Creating branch '{branch_name}'...[/cyan]")
            agency.github.create_branch(repo_name, branch_name)
            
            for file_path, new_content in refactored_files.items():
                console.print(f"[cyan]Pushing updates to {file_path}...[/cyan]")
                agency.github.update_repo_file(repo_name, file_path, new_content, branch=branch_name)
                
            console.print(f"[bold green]Successfully pushed changes to branch '{branch_name}'! 🎉[/bold green]")
        except Exception as e:
            console.print(f"[bold red]Error pushing to GitHub: {e}[/bold red]")
    else:
        console.print("[yellow]Changes were discarded. No push was made.[/yellow]")

if __name__ == "__main__":
    asyncio.run(main())


