from app.sourcedetector import (
    detect_source_type
)

from app.inputloader import (
    get_input_code
)


def load_input(
    value: str
):
    """
    Automatically load input.

    Supports:
    - GitHub File URL
    - GitHub Repository URL
    - Local File
    - Pasted Code
    """

    source_type = detect_source_type(
        value
    )

    return get_input_code(
        source_type,
        value
    )