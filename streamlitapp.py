import streamlit as st

from app.sourcehandler import load_input
from app.validator import validate_code
from app.flakinessanalyzer import analyze_flakiness
from app.migrationreport import generate_report
from app.converter import convert_to_playwright
from app.syntaxvalidator import validate_python_syntax
from app.testexecutor import execute_playwright_test
from app.outputwriter import save_playwright_repo
from app.githubpublisher import (
    create_branch,
    push_converted_files,
    generate_branch_name
)
from app.inputloader import (
    extract_repo_details,
    extract_github_file_details
)


st.set_page_config(
    page_title="AI Test Modernizer",
    page_icon="🚀",
    layout="wide"
)

if "push_completed" not in st.session_state:
    st.session_state[
        "push_completed"
    ] = False

if "push_in_progress" not in st.session_state:
    st.session_state[
        "push_in_progress"
    ] = False

if "conversion_ready_for_push" not in st.session_state:

    st.session_state[
        "conversion_ready_for_push"
    ] = False

if "last_branch_url" not in st.session_state:

    st.session_state[
        "last_branch_url"
    ] = ""

if "last_branch_name" not in st.session_state:

    st.session_state[
        "last_branch_name"
    ] = ""

if "push_source_type" not in st.session_state:

    st.session_state[
        "push_source_type"
    ] = ""

if "execution_result" not in st.session_state:
    st.session_state[
        "execution_result"
    ] = None

if "playwright_code" not in st.session_state:
    st.session_state[
        "playwright_code"
    ] = ""

if "conversion_completed" not in st.session_state:
    st.session_state[
        "conversion_completed"
    ] = False

if "is_repo" not in st.session_state:
    st.session_state[
        "is_repo"
    ] = False

if "migration_report" not in st.session_state:
    st.session_state[
        "migration_report"
    ] = ""

if "flakiness_result" not in st.session_state:
    st.session_state[
        "flakiness_result"
    ] = None

if "syntax_valid" not in st.session_state:
    st.session_state[
        "syntax_valid"
    ] = False

if "repo_total_risk" not in st.session_state:
    st.session_state[
        "repo_total_risk"
    ] = 0

if "repo_total_issues" not in st.session_state:
    st.session_state[
        "repo_total_issues"
    ] = 0

if "repo_file_count" not in st.session_state:
    st.session_state[
        "repo_file_count"
    ] = 0

if "repo_syntax_valid" not in st.session_state:
    st.session_state[
        "repo_syntax_valid"
    ] = True

if "playwright_version" not in st.session_state:
    st.session_state[
        "playwright_version"
    ] = "Latest"

# -----------------------------
# STYLING
# -----------------------------

st.markdown(
    """
    <style>

    .main-title {
        text-align:center;
        color:#4CAF50;
        font-size:58px;
        font-weight:800;
    }

    .sub-title {
        text-align:center;
        color:#BDBDBD;
        font-size:22px;
        margin-top:-10px;
        margin-bottom:10px;
    }

    .stButton button {
        width:100%;
        background-color:#4CAF50;
        color:white;
        font-weight:bold;
        font-size:18px;
        border-radius:10px;
        height:55px;
    }

    .stButton button:hover {
        background-color:#43A047;
        color:white;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# SIDEBAR
# -----------------------------

with st.sidebar:

    st.markdown("# 🚀 AI Test Modernizer")

    st.markdown("---")

    st.markdown("### ✨ Capabilities")

    st.markdown("""
✅ Paste Selenium/Cypress Code

✅ Upload Test Files 

✅ Import Directly from GitHub

✅ Detect Flaky Test Patterns

✅ Generate Migration Reports

✅ Convert to Playwright

✅ Download Modernized Tests
""")

    st.markdown("---")

    st.markdown("### 🛠 Framework Support")

    st.markdown("""
⚡ Selenium

⚡ Cypress

🎯 Playwright Output
""")

    st.markdown("---")

    st.markdown("### 💡 What It Does")

    st.caption(
        "Analyze legacy automation tests, identify modernization opportunities, and generate production-ready Playwright tests using AI."
    )

# -----------------------------
# HEADER
# -----------------------------

st.markdown(
    """
    <div class="main-title">
        🚀 AI Test Modernizer
    </div>

    <div class="sub-title">
        AI-Powered Test Modernization Platform
    </div>
    """,
    unsafe_allow_html=True
)

st.caption(
    "Analyze legacy tests • Detect flakiness • Generate Playwright code • Download modernized tests"
)

st.divider()

# -----------------------------
# OVERVIEW
# -----------------------------

st.subheader("📈 Platform Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Input Sources",
        "4"
    )

with col2:
    st.metric(
        "Supported Frameworks",
        "2"
    )

with col3:
    st.metric(
        "Target Framework",
        "Playwright"
    )

st.divider()

# -----------------------------
# INPUT SECTION
# -----------------------------

input_type = st.radio(
    "Choose Input Method",
    [
        "Paste Code",
        "Upload File",
        "GitHub File URL",
        "GitHub Repository URL"
    ],
    horizontal=True
)

if "last_input_type" not in st.session_state:

    st.session_state[
        "last_input_type"
    ] = input_type

if (
    st.session_state[
        "last_input_type"
    ]
    !=
    input_type
):

    st.session_state[
        "conversion_completed"
    ] = False

    st.session_state[
        "execution_result"
    ] = None

    st.session_state[
        "playwright_code"
    ] = ""

    st.session_state[
        "migration_report"
    ] = ""

    st.session_state[
        "flakiness_result"
    ] = None

    st.session_state[
        "syntax_valid"
    ] = False

    st.session_state[
        "is_repo"
    ] = False

    st.session_state[
        "conversion_ready_for_push"
    ] = False

    st.session_state.pop(
        "converted_files",
        None
    )
    st.session_state[
        "repo_total_risk"
    ] = 0

    st.session_state[
        "repo_total_issues"
    ] = 0

    st.session_state[
        "repo_file_count"
    ] = 0

    st.session_state[
        "repo_syntax_valid"
    ] = True

    st.session_state[
        "last_input_type"
    ] = input_type


legacy_code = ""

github_source_url = None

if input_type == "Paste Code":

    legacy_code = st.text_area(
        "Paste Selenium/Cypress Code",
        height=350,
        placeholder="Paste your legacy automation code here..."
    )

elif input_type == "Upload File":

    uploaded_file = st.file_uploader(
        "Upload Test File",
        type=["py", "js", "ts"]
    )

    if uploaded_file:

        legacy_code = (
            uploaded_file
            .read()
            .decode("utf-8")
        )

elif input_type == "GitHub File URL":

    github_source_url = st.text_input(
        "Enter GitHub File URL",
        placeholder="https://github.com/user/repo/blob/main/test.py"
    )

    legacy_code = github_source_url

elif input_type == "GitHub Repository URL":

    github_source_url = st.text_input(
        "Enter GitHub Repository URL",
        placeholder="https://github.com/user/repo/tree/main"
    )

    legacy_code = github_source_url

st.divider()

st.subheader(
    "⚙️ Target Configuration"
)

playwright_version = st.selectbox(
    "Playwright Version",
    [
        "Latest",
        "1.50",
        "1.49",
        "1.48",
        "1.47"
    ]
)

st.session_state[
    "playwright_version"
] = playwright_version

convert_clicked = st.button(
    "🚀 Convert to Playwright"
)

# -----------------------------
# PIPELINE
# -----------------------------

if convert_clicked:

    st.session_state[
        "push_completed"
    ] = False

    st.session_state[
        "push_in_progress"
    ] = False

    st.session_state[
        "conversion_ready_for_push"
    ] = False

    st.session_state[
        "last_branch_url"
    ] = ""

    st.session_state[
        "last_branch_name"
    ] = ""

    st.session_state[
        "execution_result"
    ] = None

    st.session_state[
        "conversion_completed"
    ] = False

    st.session_state.pop(
        "converted_files",
        None
    )

    st.session_state.pop(
        "github_source_url",
        None
    )

    st.session_state.pop(
        "input_type",
        None
    )

    try:

        if not legacy_code:

            st.warning(
                "Please provide an input."
            )

        else:

            
            with st.spinner(
                "Running AI Modernization..."
            ):

                code = load_input(
                    legacy_code
                )

                is_repo = isinstance(
                    code,
                    list
                )

                if not is_repo:

                    validate_code(code)

                    flakiness_result = (
                        analyze_flakiness(code)
                    )

                    report = generate_report(
                        flakiness_result
                    )

                    playwright_code = (
                        convert_to_playwright(
                            code,
                            playwright_version
                        )
                    )

                    st.session_state[
                        "playwright_code"
                    ] = playwright_code

                    st.session_state[
                        "migration_report"
                    ] = report

                    st.session_state[
                        "flakiness_result"
                    ] = flakiness_result


                    if input_type == "GitHub File URL":
                        st.session_state[
                            "converted_files"
                        ] = [
                            {
                                "name":
                                extract_github_file_details(
                                    github_source_url
                                )["file_path"],

                                "content":
                                playwright_code
                            }
                        ]

                    st.session_state[
                        "github_source_url"
                    ] = github_source_url

                    st.session_state[
                        "input_type"
                    ] = input_type

                    st.session_state[
                        "is_repo"
                    ] = False

                    st.session_state[
                        "conversion_completed"
                    ] = True

                    
                    syntax_valid = (
                        validate_python_syntax(
                            playwright_code
                        )
                    )

                    st.session_state[
                        "syntax_valid"
                    ] = syntax_valid

                    st.session_state[
                        "conversion_ready_for_push"
                    ] = True


                
                else:

                    converted_files = []

                    total_risk = 0
                    total_issues = 0

                    syntax_valid = True

                    for repo_file in code:

                        file_code = (
                            repo_file["content"]
                        )

                        validate_code(
                            file_code
                        )

                        file_result = (
                            analyze_flakiness(
                                file_code
                            )
                        )

                        total_risk += (
                            file_result[
                                "risk_score"
                            ]
                        )

                        total_issues += len(
                            file_result[
                                "issues"
                            ]
                        )

                        converted_code = (
                            convert_to_playwright(
                                file_code,
                                playwright_version
                            )
                        )

                        if not validate_python_syntax(
                            converted_code
                        ):
                            syntax_valid = False

                        converted_files.append(
                            {
                                "name":
                                repo_file["name"],
                                "content":
                                converted_code
                            }
                        )

                    st.session_state[
                        "converted_files"
                    ] = converted_files

                    st.session_state[
                        "repo_total_risk"
                    ] = total_risk

                    st.session_state[
                        "repo_total_issues"
                    ] = total_issues

                    st.session_state[
                        "repo_file_count"
                    ] = len(code)

                    st.session_state[
                        "repo_syntax_valid"
                    ] = syntax_valid

                    st.session_state[
                        "github_source_url"
                    ] = github_source_url

                    st.session_state[
                        "input_type"
                    ] = input_type

                    st.session_state[
                        "is_repo"
                    ] = True

                    st.session_state[
                        "conversion_ready_for_push"
                    ] = True

                    st.session_state[
                        "conversion_completed"
                    ] = True

    except Exception as e:

        st.error(
            f"❌ Error: {str(e)}"
        )

# -----------------------------
# PERSISTENT SINGLE FILE RESULTS
# -----------------------------

if (
    st.session_state.get(
        "conversion_completed",
        False
    )
    and
    not st.session_state.get(
        "is_repo",
        False
    )
):

    playwright_code = (
        st.session_state[
            "playwright_code"
        ]
    )

    report = (
        st.session_state[
            "migration_report"
        ]
    )

    flakiness_result = (
        st.session_state[
            "flakiness_result"
        ]
    )

    syntax_valid = (
        st.session_state[
            "syntax_valid"
        ]
    )

    st.success(
        "✅ Migration Completed Successfully"
    )

    st.divider()

    st.subheader(
        "📊 Migration Summary"
    )

    stat1, stat2, stat3 = st.columns(3)

    with stat1:

        st.metric(
            "Legacy Risk Score",
            f"{flakiness_result['risk_score']}/100"
        )

    with stat2:

        st.metric(
            "Issues Found",
            len(
                flakiness_result[
                    "issues"
                ]
            )
        )

    with stat3:

        st.metric(
            "Syntax Validation",
            "PASS"
            if syntax_valid
            else "FAIL"
        )

    if syntax_valid:

        st.success(
            "✅ Generated Playwright code is syntactically valid."
        )

    else:

        st.error(
            "❌ Generated Playwright code contains syntax errors."
        )

    st.divider()

    left_col, right_col = st.columns(
        [1, 2]
    )

    with left_col:

        st.subheader(
            "📊 Migration Report"
        )

        st.text(
            report
        )

    with right_col:

        st.subheader(
            "📜 Generated Playwright Code"
        )

        st.code(
            playwright_code,
            language="python"
        )

    st.divider()

    st.download_button(
        label="⬇ Download Playwright Code",
        data=playwright_code,
        file_name="converted_test.py",
        mime="text/plain",
        use_container_width=True
    )

    st.divider()

    execute_clicked = st.button(
        "▶ Execute Converted Test",
        key="execute_test_button"
    )

    if execute_clicked:

        with st.spinner(
            "Executing Playwright Test..."
        ):

            st.session_state[
                "execution_result"
            ] = execute_playwright_test(
                playwright_code
            )

    execution_result = (
        st.session_state.get(
            "execution_result"
        )
    )

    if execution_result:

        st.divider()

        st.subheader(
            "✅ Execution Results"
        )

        metric1, metric2, metric3 = (
            st.columns(3)
        )

        with metric1:

            st.metric(
                "Passed",
                execution_result[
                    "passed"
                ]
            )

        with metric2:

            st.metric(
                "Failed",
                execution_result[
                    "failed"
                ]
            )

        with metric3:

            st.metric(
                "Skipped",
                execution_result[
                    "skipped"
                ]
            )

        st.text_area(
            "Execution Summary",
            execution_result[
                "execution_summary"
            ],
            height=100
        )

        st.text_area(
            "Execution Log",
            execution_result[
                "stdout"
            ],
            height=300
        )

        if (
            execution_result[
                "stderr"
            ]
        ):

            st.text_area(
                "Execution Errors",
                execution_result[
                    "stderr"
                ],
                height=200
            )

# -----------------------------
# PERSISTENT REPOSITORY RESULTS
# -----------------------------

if (
    st.session_state.get(
        "conversion_completed",
        False
    )
    and
    st.session_state.get(
        "is_repo",
        False
    )
):

    converted_files = (
        st.session_state.get(
            "converted_files",
            []
        )
    )

    if converted_files:

        file_count = (
            st.session_state[
                "repo_file_count"
            ]
        )

        total_issues = (
            st.session_state[
                "repo_total_issues"
            ]
        )

        total_risk = (
            st.session_state[
                "repo_total_risk"
            ]
        )

        repo_syntax_valid = (
            st.session_state[
                "repo_syntax_valid"
            ]
        )

        avg_risk = (
            round(
                total_risk /
                file_count
            )
            if file_count > 0
            else 0
        )

        st.success(
            "✅ Repository Conversion Completed Successfully"
        )

        st.divider()

        st.subheader(
            "📊 Repository Migration Summary"
        )

        stat1, stat2, stat3 = st.columns(3)

        with stat1:

            st.metric(
                "Files Processed",
                file_count
            )

        with stat2:

            st.metric(
                "Total Issues",
                total_issues
            )

        with stat3:

            st.metric(
                "Avg Risk Score",
                avg_risk
            )

        if repo_syntax_valid:

            st.success(
                "✅ All generated Playwright files passed syntax validation."
            )

        else:

            st.error(
                "❌ One or more generated Playwright files contain syntax errors."
            )

        st.divider()

        st.subheader(
            "📦 Repository Conversion Output"
        )

        for repo_file in converted_files:

            st.markdown(
                f"### {repo_file['name']}"
            )

            st.code(
                repo_file[
                    "content"
                ],
                language="python"
            )

        st.divider()

        zip_path = (
            save_playwright_repo(
                converted_files
            )
        )

        with open(
            zip_path,
            "rb"
        ) as f:

            st.download_button(
                label="⬇ Download Playwright Repository",
                data=f.read(),
                file_name="playwright_repo.zip",
                mime="application/zip",
                use_container_width=True
            )

if (
    input_type ==
    st.session_state.get(
        "push_source_type",
        ""
    )
    and
    st.session_state.get(
        "push_completed",
        False
    )
):

    st.success(
        "✅ Push Completed Successfully"
    )

    st.markdown(
        f"🔗 {st.session_state['last_branch_url']}"
    )

    st.code(
        st.session_state[
            "last_branch_name"
        ]
    )

if st.session_state.get(
    "push_in_progress",
    False
):

    st.info(
        "🔄 Push to GitHub is currently in progress..."
    )

if (
    input_type in [
        "GitHub File URL",
        "GitHub Repository URL"
    ]
    and
    st.session_state.get(
        "conversion_ready_for_push",
        False
    )
    and
    not st.session_state.get(
        "push_completed",
        False
    )
    and
    not st.session_state.get(
        "push_in_progress",
        False
    )
):

    

    if st.button(
        "📤 Push to GitHub",
        disabled=st.session_state[
            "push_in_progress"
        ]
    ):

        try:

            st.session_state[
                "push_in_progress"
            ] = True

            with st.spinner(
                "Pushing to GitHub..."
            ):

                branch_name = (
                    generate_branch_name()
                )

                input_type = (
                    st.session_state[
                        "input_type"
                    ]
                )

                github_source_url = (
                    st.session_state[
                        "github_source_url"
                    ]
                )

                if (
                    input_type ==
                    "GitHub File URL"
                ):

                    file_details = (
                        extract_github_file_details(
                            github_source_url
                        )
                    )

                    create_branch(
                        owner=file_details[
                            "owner"
                        ],
                        repo=file_details[
                            "repo"
                        ],
                        new_branch=branch_name,
                        source_branch=file_details[
                            "branch"
                        ]
                    )

                    push_converted_files(
                        owner=file_details[
                            "owner"
                        ],
                        repo=file_details[
                            "repo"
                        ],
                        branch=branch_name,
                        converted_files=
                        st.session_state[
                            "converted_files"
                        ]
                    )

                    github_branch_url = (
                        f"https://github.com/"
                        f"{file_details['owner']}/"
                        f"{file_details['repo']}/tree/"
                        f"{branch_name}"
                    )

                else:

                    repo_details = (
                        extract_repo_details(
                            github_source_url
                        )
                    )

                    create_branch(
                        owner=repo_details[
                            "owner"
                        ],
                        repo=repo_details[
                            "repo"
                        ],
                        new_branch=branch_name,
                        source_branch=repo_details[
                            "branch"
                        ]
                    )

                    push_converted_files(
                        owner=repo_details[
                            "owner"
                        ],
                        repo=repo_details[
                            "repo"
                        ],
                        branch=branch_name,
                        converted_files=
                        st.session_state[
                            "converted_files"
                        ]
                    )

                    github_branch_url = (
                        f"https://github.com/"
                        f"{repo_details['owner']}/"
                        f"{repo_details['repo']}/tree/"
                        f"{branch_name}"
                    )

                st.session_state[
                    "last_branch_url"
                ] = github_branch_url

                st.session_state[
                    "last_branch_name"
                ] = branch_name

                st.session_state[
                    "push_source_type"
                ] = input_type

                st.session_state[
                    "push_completed"
                ] = True

                st.session_state[
                    "push_in_progress"
                ] = False

                st.session_state[
                    "conversion_ready_for_push"
                ] = False

                st.session_state.pop(
                    "converted_files",
                    None
                )

                st.rerun()

        except Exception as e:

            st.session_state[
                "push_in_progress"
            ] = False

            st.error(
                f"GitHub push failed: "
                f"{e}"
            )