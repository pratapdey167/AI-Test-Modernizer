from langchain_core.output_parsers import StrOutputParser

from app.llm import llm
from app.prompts import migration_prompt


migration_chain = (
    migration_prompt
    | llm
    | StrOutputParser()
)


def convert_to_playwright(
    legacy_code: str,
    dependency_context: str = ""
):
    """
    Convert Selenium/Cypress code
    into Playwright code.

    dependency_context:
        Optional related files
        (page objects, base classes,
        helpers, utilities, etc.)
    """

    full_context = f"""
DEPENDENCY CONTEXT

{dependency_context}

LEGACY CODE

{legacy_code}
"""

    return migration_chain.invoke(
        {
            "legacy_code": full_context
        }
    )