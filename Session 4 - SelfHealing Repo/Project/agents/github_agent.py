import os
from github import Github

class GithubAgent:
    def __init__(self):
        token = os.getenv("GITHUB_TOKEN")
        self.gh = Github(token) if token else None

    def fetch_repo_file(self, repo_name: str, file_path: str) -> str:
        """Fetches the content of a specific file from a GitHub repository."""
        if not self.gh:
            raise ValueError("GITHUB_TOKEN environment variable not set")
        
        repo = self.gh.get_repo(repo_name)
        file_content = repo.get_contents(file_path)
        return file_content.decoded_content.decode()

    def create_branch(self, repo_name: str, branch_name: str) -> None:
        """Creates a new branch from the default branch if it doesn't exist."""
        if not self.gh:
            raise ValueError("GITHUB_TOKEN environment variable not set")
        
        repo = self.gh.get_repo(repo_name)
        try:
            repo.get_branch(branch_name)
            # Branch already exists
            return
        except Exception:
            pass # We need to create it
            
        default_branch = repo.get_branch(repo.default_branch)
        repo.create_git_ref(ref=f"refs/heads/{branch_name}", sha=default_branch.commit.sha)

    def update_repo_file(self, repo_name: str, file_path: str, new_content: str, commit_message: str = "Refactored by Project Antigravity", branch: str = None):
        """Updates a file in the repository with new content."""
        if not self.gh:
            raise ValueError("GITHUB_TOKEN environment variable not set")
            
        repo = self.gh.get_repo(repo_name)
        
        # If no branch is provided, use the default branch
        if not branch:
            branch = repo.default_branch
            
        file_content = repo.get_contents(file_path, ref=branch)
        
        repo.update_file(file_path, commit_message, new_content, file_content.sha, branch=branch)

    def get_all_files(self, repo_name: str, path: str = "") -> list:
        """Recursively fetches all file paths in a repository."""
        if not self.gh:
            raise ValueError("GITHUB_TOKEN environment variable not set")
            
        repo = self.gh.get_repo(repo_name)
        try:
            contents = repo.get_contents(path)
        except Exception as e:
            return []
            
        file_paths = []
        while contents:
            file_content = contents.pop(0)
            if file_content.type == "dir":
                try:
                    contents.extend(repo.get_contents(file_content.path))
                except Exception:
                    pass # Skip directories we can't access
            else:
                file_paths.append(file_content.path)
                
        return file_paths


