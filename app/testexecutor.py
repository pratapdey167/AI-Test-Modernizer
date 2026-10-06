import os
import re
import subprocess
import tempfile
from typing import Dict


def execute_playwright_test(
    playwright_code: str
) -> Dict:

    temp_file_path = None

    try:

        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix="_playwright_test.py",
            delete=False,
            encoding="utf-8"
        ) as temp_file:

            temp_file.write(
                playwright_code
            )

            temp_file_path = (
                temp_file.name
            )

        result = subprocess.run(
            [
                "pytest",
                temp_file_path,
                "-v",
                "--tb=short"
            ],
            capture_output=True,
            text=True,
            timeout=300
        )

        stdout = (
            result.stdout or ""
        )

        stderr = (
            result.stderr or ""
        )

        summary_text = (
            stdout + "\n" + stderr
        )

        passed = 0
        failed = 0
        skipped = 0

        passed_match = re.search(
            r"(\d+)\s+passed",
            summary_text
        )

        failed_match = re.search(
            r"(\d+)\s+failed",
            summary_text
        )

        skipped_match = re.search(
            r"(\d+)\s+skipped",
            summary_text
        )

        if passed_match:

            passed = int(
                passed_match.group(1)
            )

        if failed_match:

            failed = int(
                failed_match.group(1)
            )

        if skipped_match:

            skipped = int(
                skipped_match.group(1)
            )

        return {

            "success":
            result.returncode == 0,

            "return_code":
            result.returncode,

            "passed":
            passed,

            "failed":
            failed,

            "skipped":
            skipped,

            "stdout":
            stdout,

            "stderr":
            stderr,

            "execution_summary":
            (
                f"Passed: {passed}, "
                f"Failed: {failed}, "
                f"Skipped: {skipped}"
            )
        }

    except subprocess.TimeoutExpired:

        return {

            "success": False,

            "return_code": -1,

            "passed": 0,

            "failed": 0,

            "skipped": 0,

            "stdout": "",

            "stderr":
            "Execution timed out after 300 seconds.",

            "execution_summary":
            "Execution timed out."
        }

    except Exception as e:

        return {

            "success": False,

            "return_code": -1,

            "passed": 0,

            "failed": 0,

            "skipped": 0,

            "stdout": "",

            "stderr": str(e),

            "execution_summary":
            "Execution failed."
        }

    finally:

        if (
            temp_file_path
            and
            os.path.exists(
                temp_file_path
            )
        ):

            try:

                os.remove(
                    temp_file_path
                )

            except Exception:
                pass