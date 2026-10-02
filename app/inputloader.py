import ast
import requests


EXCLUDED_DIRS = {
    ".git",
    ".github",
    ".helm",
    "trident",
    "venv",
    "node_modules",
    "dist",
    "build",
    "__pycache__"
}


TEST_INDICATORS = [
    "webdriver",
    "find_element",
    "By.XPATH",
    "By.ID",
    "By.CSS_SELECTOR",
    "cy.",
    "describe(",
    "it(",
    "@Test"
]


def load_pasted_code(
    code: str
) -> str:
    return code


def load_local_file(
    file_path: str
) -> str:

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()


def validate_github_url(
    github_url: str,
    expect_repo: bool = False
) -> bool:

    if not github_url.startswith(
        "https://github.com/"
    ):
        raise ValueError(
            "Only GitHub URLs are supported."
        )

    if expect_repo:

        if "/tree/" not in github_url:
            raise ValueError(
                "Please provide a valid GitHub repository URL."
            )

    else:

        if "/blob/" not in github_url:
            raise ValueError(
                "Please provide a valid GitHub file URL."
            )

    return True


def github_to_raw_url(
    github_url: str
) -> str:

    return (
        github_url
        .replace(
            "github.com",
            "raw.githubusercontent.com"
        )
        .replace(
            "/blob/",
            "/"
        )
    )

def extract_repo_details(
    github_url: str
):
    """
    Extract owner, repository and
    branch information from a
    GitHub URL.
    """

    clean_url = (
        github_url.replace(
            "https://github.com/",
            ""
        )
    )

    parts = clean_url.split("/")

    owner = parts[0]
    repo = parts[1]

    branch = "main"

    if "tree" in parts:

        branch_index = (
            parts.index("tree") + 1
        )

        if branch_index < len(parts):

            branch = parts[
                branch_index
            ]

    elif "blob" in parts:

        branch_index = (
            parts.index("blob") + 1
        )

        if branch_index < len(parts):

            branch = parts[
                branch_index
            ]

    return {
        "owner": owner,
        "repo": repo,
        "branch": branch
    }


def extract_github_file_details(
    github_url: str
):
    """
    Extract owner, repo, branch
    and file path from a GitHub
    file URL.
    """

    details = extract_repo_details(
        github_url
    )

    clean_url = github_url.replace(
        "https://github.com/",
        ""
    )

    parts = clean_url.split("/")

    blob_index = parts.index(
        "blob"
    )

    file_path = "/".join(
        parts[
            blob_index + 2:
        ]
    )

    details[
        "file_path"
    ] = file_path

    return details

def load_github_file(
    github_url: str
) -> str:

    validate_github_url(
        github_url,
        expect_repo=False
    )

    raw_url = github_to_raw_url(
        github_url
    )

    response = requests.get(
        raw_url,
        timeout=120
    )

    response.raise_for_status()

    return response.text


def is_test_file(
    content: str
) -> bool:

    return any(
        indicator in content
        for indicator in TEST_INDICATORS
    )


def extract_imports(
    source_code: str
) -> set:

    imports = set()

    try:

        tree = ast.parse(
            source_code
        )

        for node in ast.walk(
            tree
        ):

            if isinstance(
                node,
                ast.Import
            ):

                for name in node.names:

                    imports.add(
                        name.name
                    )

            elif isinstance(
                node,
                ast.ImportFrom
            ):

                if node.module:

                    imports.add(
                        node.module
                    )

    except Exception:

        pass

    return imports


def load_github_repo(
    repo_url: str
) -> list:

    validate_github_url(
        repo_url,
        expect_repo=True
    )

    clean_url = repo_url.replace(
        "https://github.com/",
        ""
    )

    parts = clean_url.split("/")

    owner = parts[0]
    repo = parts[1]

    all_files = []

    def scan_directory(
        api_url: str
    ):

        response = requests.get(
            api_url,
            timeout=120
        )

        response.raise_for_status()

        items = response.json()

        for item in items:

            path = item["path"]

            if any(
                excluded in path.split("/")
                for excluded in EXCLUDED_DIRS
            ):
                continue

            if item["type"] == "dir":

                scan_directory(
                    item["url"]
                )

            elif (
                item["type"] == "file"
                and item["name"].endswith(
                    (
                        ".py",
                        ".js",
                        ".ts"
                    )
                )
            ):

                file_response = requests.get(
                    item["download_url"],
                    timeout=120
                )

                file_response.raise_for_status()

                all_files.append(
                    {
                        "name": path,
                        "content": file_response.text
                    }
                )

    root_api_url = (
        f"https://api.github.com/repos/"
        f"{owner}/{repo}/contents"
    )

    scan_directory(
        root_api_url
    )

    selected_files = []

    for file in all_files:

        if is_test_file(
            file["content"]
        ):

            selected_files.append(
                file
            )

    return selected_files


def get_input_code(
    source_type: str,
    value: str
):

    if source_type == "text":

        return load_pasted_code(
            value
        )

    elif source_type == "file":

        return load_local_file(
            value
        )

    elif source_type == "github_file":

        return load_github_file(
            value
        )

    elif source_type == "github_repo":

        return load_github_repo(
            value
        )

    else:

        raise ValueError(
            f"Unsupported source type: {source_type}"
        )