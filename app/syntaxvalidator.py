import ast


def validate_python_syntax(
    code: str
) -> bool:

    try:

        ast.parse(code)

        return True

    except SyntaxError:

        return False