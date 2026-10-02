from app.githubpublisher import update_file

result = update_file(
    owner="pratapdey167",
    repo="testrepo",
    branch="playwright-modernization",
    file_path="README.md",
    new_content="""
# Updated by AI Test Modernizer
""",
    commit_message=
    "Test commit from AI Test Modernizer"
)

print(
    result["commit"]["sha"]
)