def validate_code(code: str):
    """
    Validate incoming legacy test code.
    """

    if not code.strip():
        raise ValueError(
            "Input code cannot be empty."
        )

    if len(code) < 20:
        raise ValueError(
            "Input code is too short."
        )

    selenium_indicators = [
        "driver.",
        "find_element",
        "webdriver"
    ]

    cypress_indicators = [
        "cy.",
        "cypress"
    ]

    if not any(
        indicator in code
        for indicator in (
            selenium_indicators
            + cypress_indicators
        )
    ):
        raise ValueError(
            "Unsupported framework detected. Only Selenium and Cypress are currently supported."
        )

    return True