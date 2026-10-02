def analyze_flakiness(
    code: str
) -> dict:

    issues = []

    hard_waits = code.count(
        "time.sleep"
    )

    xpaths = code.count(
        "By.XPATH"
    )

    implicit_waits = code.count(
        "implicitly_wait"
    )

    if hard_waits:

        issues.append(
            f"{hard_waits} hard wait(s)"
        )

    if xpaths:

        issues.append(
            f"{xpaths} XPath locator(s)"
        )

    if implicit_waits:

        issues.append(
            f"{implicit_waits} implicit wait(s)"
        )

    risk_score = (
        hard_waits * 20
        + xpaths * 15
        + implicit_waits * 15
    )

    return {
        "issues": issues,
        "risk_score": min(
            risk_score,
            100
        )
    }