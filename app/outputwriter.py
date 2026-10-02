import os
import zipfile


def save_playwright_code(
    code: str,
    file_name: str = "converted_test.py"
) -> str:
    """
    Save a single Playwright file.
    """

    os.makedirs(
        "outputs",
        exist_ok=True
    )

    output_path = (
        f"outputs/{file_name}"
    )

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(code)

    return output_path


def save_playwright_repo(
    converted_files: list,
    zip_name: str = "playwright_repo.zip"
) -> str:
    """
    Save repository conversion results
    into a ZIP archive.

    Example converted_files:

    [
        {
            "name": "login_test.py",
            "content": "Playwright code..."
        },
        {
            "name": "profile_test.py",
            "content": "Playwright code..."
        }
    ]
    """

    os.makedirs(
        "outputs",
        exist_ok=True
    )

    zip_path = (
        f"outputs/{zip_name}"
    )

    with zipfile.ZipFile(
        zip_path,
        "w",
        zipfile.ZIP_DEFLATED
    ) as zip_file:

        for file in converted_files:

            zip_file.writestr(
                file["name"],
                file["content"]
            )

    return zip_path