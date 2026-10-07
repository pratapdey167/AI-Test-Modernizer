# 🚀 AI Test Modernizer

AI Test Modernizer is an AI-powered test modernization platform that helps teams migrate legacy Selenium and Cypress automation tests to Playwright with minimal manual effort.

The platform analyzes existing automation code, identifies flaky patterns, generates migration insights, converts tests to Playwright, validates generated code, executes converted tests, and publishes modernized tests directly to GitHub.

---

# 📖 Overview

Modern test automation teams often face challenges such as:

- Large Selenium codebases
- Legacy Cypress repositories
- Flaky tests
- High maintenance costs
- Slow framework migration initiatives

Migrating manually to Playwright can take weeks or months.

AI Test Modernizer accelerates the migration process using AI-assisted conversion and automated analysis.

---

# 🎯 What This Tool Does

The platform provides an end-to-end modernization workflow.

```
Legacy Test
     │
     ▼
Code Validation
     │
     ▼
Flakiness Analysis
     │
     ▼
Migration Report
     │
     ▼
AI Conversion
     │
     ▼
Playwright Validation
     │
     ▼
Optional Execution
     │
     ▼
Download / GitHub Push
```

---

# ✨ Features

## ✅ Flakiness Detection

Identifies common anti-patterns such as:

- Hard waits (`time.sleep`)
- Brittle locators
- Synchronization issues
- Maintainability concerns
- Legacy automation patterns

Generates a risk score to help prioritize modernization.

---

## ✅ Migration Report

Automatically generates insights including:

- Risk score
- Identified issues
- Improvement recommendations
- Modernization benefits

---

## ✅ AI-Powered Conversion

Automatically converts:

```
Selenium
      ↓
Playwright

Cypress
      ↓
Playwright
```

Generated Playwright code follows modern best practices:

- Auto waiting
- Better locator strategies
- Web-first assertions
- Pytest-compatible structure

---

## ✅ Syntax Validation

Validates generated Playwright code before download:

- Python syntax validation
- Code generation sanity checks
- Execution readiness checks

---

## ✅ Playwright Test Execution

Execute generated Playwright code directly from the UI.

Execution results include:

- Passed count
- Failed count
- Skipped count
- Execution summary
- Execution logs
- Error logs

---

## ✅ GitHub Integration

Supports:

### GitHub File Conversion

Convert a single test file directly from GitHub.

### GitHub Repository Conversion

Convert all supported test files in a repository.

### GitHub Publishing

Automatically:

```
Create Branch
      ↓
Push Converted Files
      ↓
Generate Branch URL
      ↓
Ready For Pull Request
```

---

# 🌐 Supported Input Methods

## 1. Paste Code

Paste Selenium or Cypress code directly into the application.

### Use Case

Quick proof-of-concept conversions.

---

## 2. Upload File

Upload supported test files.

### Supported Types

```
.py
.js
.ts
```

---

## 3. GitHub File URL

Convert a single GitHub-hosted test file.

Example:

```
https://github.com/user/repository/blob/main/tests/login.py
```

---

## 4. GitHub Repository URL

Convert an entire repository.

Example:

```
https://github.com/user/repository/tree/main
```

---

# 🔄 End-to-End Workflow

## Single File Workflow

```
Paste Code / Upload File / GitHub File
            │
            ▼
      Load Source
            │
            ▼
     Code Validation
            │
            ▼
   Flakiness Analysis
            │
            ▼
   Migration Report
            │
            ▼
 Convert To Playwright
            │
            ▼
   Syntax Validation
            │
            ▼
   Playwright Output
            │
      ┌─────┼─────┐
      ▼     ▼     ▼
 Download Execute Push
```

---

## Repository Workflow

```
GitHub Repository
         │
         ▼
 Load Repository Files
         │
         ▼
 Analyze Every File
         │
         ▼
 Convert Every File
         │
         ▼
 Repository Summary
         │
         ▼
 Download ZIP
         │
         ▼
 Push To GitHub
```

---

# 📊 Migration Metrics

The application generates migration statistics.

## Single File Metrics

- Legacy Risk Score
- Issues Found
- Syntax Validation Status

---

## Repository Metrics

- Files Processed
- Total Issues
- Average Risk Score
- Syntax Validation Status

---

# 🧪 Playwright Execution Workflow

Execution is supported only for single-file conversions.

```
Convert
   │
   ▼
Validate
   │
   ▼
Execute
   │
   ▼
Pytest Execution
   │
   ▼
Execution Summary
```

Execution results include:

```
Passed: X
Failed: Y
Skipped: Z
```

With:

- Full logs
- Error details
- Execution summary

---

# 🧱 Solution Architecture

```
streamlitapp.py
       │
       ▼
sourcehandler.py
       │
       ▼
validator.py
       │
       ▼
flakinessanalyzer.py
       │
       ▼
migrationreport.py
       │
       ▼
converter.py
       │
       ▼
syntaxvalidator.py
       │
       ▼
testexecutor.py
       │
       ▼
githubpublisher.py
```

---

# 📁 Project Structure

```
test-modernizer/
│
├── README.md
├── streamlitapp.py
├── main.py
│
├── app/
│   ├── converter.py
│   ├── validator.py
│   ├── sourcehandler.py
│   ├── sourcedetector.py
│   ├── flakinessanalyzer.py
│   ├── migrationreport.py
│   ├── syntaxvalidator.py
│   ├── testexecutor.py
│   ├── githubpublisher.py
│   ├── inputloader.py
│   ├── prompts.py
│   └── llm.py
│
├── outputs/
│
└── requirements.txt
```

---

# ⚙️ Configuration

## Required Python Version

Recommended:

```
Python 3.10+
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

Example:

```env
GOOGLE_API_KEY=<your-gemini-api-key>

GITHUB_TOKEN=<github-personal-access-token>
```

---

## Google Gemini API Key

Required for:

- AI Conversion
- Migration Recommendations

---

## GitHub Personal Access Token

Required for:

- Create Branch
- Push Converted Files

Recommended permissions:

```
repo
contents:write
pull_requests:write
```

---

# ▶ Running The Application

Launch Streamlit UI:

```bash
streamlit run streamlitapp.py
```

Default URL:

```
http://localhost:8501
```

---

# 🔍 Example Conversion

## Selenium

```python
driver.find_element(
    By.NAME,
    "username"
).send_keys("Admin")

driver.find_element(
    By.NAME,
    "password"
).send_keys("admin123")

driver.find_element(
    By.XPATH,
    "//button[@type='submit']"
).click()
```

---

## Playwright

```python
page.get_by_placeholder(
    "Username"
).fill("Admin")

page.get_by_placeholder(
    "Password"
).fill("admin123")

page.get_by_role(
    "button",
    name="Login"
).click()
```

---

# 🛠 Supported Frameworks

| Framework | Supported |
|------------|------------|
| Selenium | ✅ |
| Cypress | ✅ |
| Playwright Output | ✅ |

---

# 💻 Technology Stack

- Python
- Streamlit
- LangChain
- Google Gemini
- Playwright
- Pytest
- GitHub API

---

# 🎯 Benefits

- Faster framework migration
- Reduced manual effort
- Lower modernization risk
- Improved test reliability
- Flakiness reduction
- GitHub-ready output
- Execution validation before commit

---

# 📋 Demo Walkthrough

Use this sequence during demonstrations.

## Scenario 1 – Paste Code

1. Open application
2. Select "Paste Code"
3. Paste Selenium script
4. Click "Convert to Playwright"
5. Review Migration Summary
6. Review Migration Report
7. Review Generated Playwright Code
8. Execute Converted Test
9. Review Execution Results
10. Download Code

---

## Scenario 2 – Upload File
 
1. Select **Upload File**
2. Upload a Selenium/Cypress test file
3. Click **Convert to Playwright**
4. Review:
- Risk Score
- Migration Report
- Syntax Validation
5. Execute generated Playwright test
6. Download converted file

---

## Scenario 3 – GitHub File

1. Select "GitHub File URL"
2. Enter test file URL
3. Convert
4. Review migration details
5. Push to GitHub
6. Open generated branch

---

## Scenario 4 – GitHub Repository

1. Select "GitHub Repository URL"
2. Enter repository URL
3. Convert repository
4. Review:
   - Files Processed
   - Total Issues
   - Average Risk Score
5. Download ZIP
6. Push converted repository to GitHub

---

# 🚀 Future Enhancements

Potential roadmap items:

- CI/CD integration
- Pull request automation
- Playwright test generation
- Conversion quality scoring
- Dashboard analytics
- PDF reporting
- Conversion history
- Enterprise reporting

---

# 👨‍💻 Author

**Pratap Dey**  
Senior Consultant  
Capgemini

---

# ⭐ Support

If you find this project useful, consider starring the repository and contributing improvements.