import os


def detect_source_type(
    value: str
) -> str:
    """
    Detect whether input is:

    - GitHub File
    - GitHub Repository
    - Local File
    - Pasted Code
    """

    if value.startswith(
        "https://github.com/"
    ):

        if "/blob/" in value:

            return "github_file"

        if "/tree/" in value:

            return "github_repo"

    if os.path.isfile(
        value
    ):

        return "file"

    return "text"