def generate_report(flakiness_result: dict) -> str:

    report = []

    report.append("MIGRATION REPORT")
    report.append("=" * 50)
    report.append("")

    report.append("Issues Detected:")

    if flakiness_result["issues"]:

        for issue in flakiness_result["issues"]:
            report.append(f"✓ {issue}")

    else:
        report.append("✓ No major issues detected")

    report.append("")

    report.append(
        f"Risk Score: {flakiness_result['risk_score']}/100"
    )

    report.append("")

    report.append("Expected Migration Improvements:")
    report.append("✓ Playwright auto-waiting")
    report.append("✓ Web-first assertions")
    report.append("✓ Improved locator strategy")

    return "\n".join(report)