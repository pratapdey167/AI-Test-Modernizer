import os
import base64
import requests

from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

GITHUB_TOKEN = os.getenv(
    "GITHUB_TOKEN"
)

if not GITHUB_TOKEN:
    raise RuntimeError(
        "Missing GITHUB_TOKEN in .env"
    )


HEADERS = {
    "Authorization":
    f"Bearer {GITHUB_TOKEN}",

    "Accept":
    "application/vnd.github+json"
}


def validate_github_access():
    """
    Validate GitHub access token.
    """

    response = requests.get(
        "https://api.github.com/user",
        headers=HEADERS
    )

    response.raise_for_status()

    return response.json()


def get_branch_sha(
    owner: str,
    repo: str,
    branch: str = "main"
):
    """
    Fetch the SHA of a branch.
    """

    response = requests.get(
        f"https://api.github.com/repos/"
        f"{owner}/{repo}/git/ref/heads/{branch}",
        headers=HEADERS
    )

    response.raise_for_status()

    return response.json()["object"]["sha"]


def create_branch(
    owner: str,
    repo: str,
    new_branch: str,
    source_branch: str = "main"
):
    """
    Create a new branch from source branch.
    """

    source_sha = get_branch_sha(
        owner,
        repo,
        source_branch
    )

    payload = {
        "ref":
        f"refs/heads/{new_branch}",

        "sha":
        source_sha
    }

    response = requests.post(
        f"https://api.github.com/repos/"
        f"{owner}/{repo}/git/refs",
        headers=HEADERS,
        json=payload
    )

    response.raise_for_status()

    return response.json()


def get_file_sha(
    owner: str,
    repo: str,
    file_path: str,
    branch: str
):
    """
    Fetch existing file SHA.
    """

    response = requests.get(
        f"https://api.github.com/repos/"
        f"{owner}/{repo}/contents/{file_path}",
        headers=HEADERS,
        params={
            "ref": branch
        }
    )

    response.raise_for_status()

    return response.json()["sha"]


def update_file(
    owner: str,
    repo: str,
    branch: str,
    file_path: str,
    new_content: str,
    commit_message: str
):
    """
    Update existing file.
    """

    file_sha = get_file_sha(
        owner,
        repo,
        file_path,
        branch
    )

    encoded_content = (
        base64
        .b64encode(
            new_content.encode(
                "utf-8"
            )
        )
        .decode(
            "utf-8"
        )
    )

    payload = {
        "message":
        commit_message,

        "content":
        encoded_content,

        "branch":
        branch,

        "sha":
        file_sha
    }

    response = requests.put(
        f"https://api.github.com/repos/"
        f"{owner}/{repo}/contents/{file_path}",
        headers=HEADERS,
        json=payload
    )

    response.raise_for_status()

    return response.json()


def push_converted_files(
    owner: str,
    repo: str,
    branch: str,
    converted_files: list
):
    """
    Push all converted files.

    Expected format:

    [
        {
            "name": "tests/login_test.py",
            "content": "playwright code"
        }
    ]
    """

    results = []

    for file in converted_files:

        result = update_file(
            owner=owner,
            repo=repo,
            branch=branch,
            file_path=file["name"],
            new_content=file["content"],
            commit_message=(
                f"AI Test Modernizer: "
                f"Update {file['name']}"
            )
        )

        results.append(
            result
        )

    return results

def generate_branch_name():
    """
    Generate a unique branch name.
    """

    timestamp = datetime.now().strftime(
        "%Y%m%d-%H%M%S"
    )

    return (
        f"playwright-modernization-"
        f"{timestamp}"
    )