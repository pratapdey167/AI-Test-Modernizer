from app.sourcehandler import load_input

from app.validator import validate_code

from app.flakinessanalyzer import (
    analyze_flakiness
)

from app.migrationreport import (
    generate_report
)

from app.converter import (
    convert_to_playwright
)

from app.syntaxvalidator import (
    validate_python_syntax
)


user_input = input(
    "\nEnter Selenium/Cypress code, file path, or GitHub URL:\n"
)


try:

    legacy_code = load_input(
        user_input
    )

    validate_code(
        legacy_code
    )

    print(
        "\n✅ Validation Successful"
    )

    flakiness_result = (
        analyze_flakiness(
            legacy_code
        )
    )

    report = generate_report(
        flakiness_result
    )

    print("\n")
    print(report)
    print("\n")

    playwright_code = (
        convert_to_playwright(
            legacy_code
        )
    )

    print("=" * 60)
    print("PLAYWRIGHT OUTPUT")
    print("=" * 60)
    print()

    print(playwright_code)

    syntax_valid = (
        validate_python_syntax(
            playwright_code
        )
    )

    print("\n" + "=" * 60)

    if syntax_valid:

        print(
            "✅ Generated code is syntactically valid."
        )

    else:

        print(
            "❌ Generated code contains syntax errors."
        )

    print("=" * 60)

except Exception as e:

    print(
        f"\n❌ Error: {str(e)}"
    )