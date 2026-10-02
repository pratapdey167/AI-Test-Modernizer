# 🚀 AI Test Modernizer

An AI-powered test modernization platform that converts legacy Selenium and Cypress automation scripts into production-ready Playwright tests.

---

## 📌 Overview

AI Test Modernizer helps QA engineers and automation teams accelerate framework migration by:

- Detecting flaky test patterns
- Generating migration insights
- Converting Selenium/Cypress tests to Playwright
- Validating generated code
- Supporting multiple input sources

The tool provides both:

- Command Line Interface (CLI)
- Streamlit Web UI

---

## ✨ Features

### Supported Inputs

✅ Paste Selenium/Cypress Code

✅ Upload Python Test Files

✅ Import Tests from GitHub

---

### Flakiness Analysis

Detects common flaky patterns such as:

- Hard waits (`time.sleep`)
- Brittle XPath locators
- Maintainability concerns

Generates a Legacy Risk Score to help prioritize modernization efforts.

---

### AI-Powered Conversion

Automatically converts:

```text
Selenium
        ↓
Playwright

Cypress
        ↓
Playwright
```

Generated Playwright code follows modern best practices:

- Auto-waiting
- Semantic locators
- Web-first assertions
- Pytest-compatible structure

---

### Migration Report

Provides:

- Identified issues
- Risk score
- Modernization recommendations
- Expected migration benefits

---

### Syntax Validation

Automatically validates generated Playwright code to ensure:

- Python syntax correctness
- Playwright API validity
- Executable output

---

### Download Support

Download generated Playwright tests directly from the web interface.

---

## 🏗 Architecture

```text
User Input
     │
     ├── Paste Code
     ├── Upload File
     └── GitHub URL
             │
             ▼
      Source Handler
             │
             ▼
         Validation
             │
             ▼
   Flakiness Analyzer
             │
             ▼
    Migration Report
             │
             ▼
      AI Conversion
             │
             ▼
    Syntax Validation
             │
             ▼
    Playwright Output
             │
             ▼
   Download / Export
```

---

## 📂 Project Structure

```text
test-modernizer/

├── README.md
├── main.py
├── streamlitapp.py
│
├── outputs/
│   └── converted_test.py
│
└── app/
    ├── converter.py
    ├── flakiness_analyzer.py
    ├── inputloader.py
    ├── llm.py
    ├── migration_report.py
    ├── prompts.py
    ├── sourcedetector.py
    ├── sourcehandler.py
    ├── syntax_validator.py
    └── validator.py
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone <repository-url>
cd test-modernizer
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

### Streamlit UI

```bash
streamlit run streamlitapp.py
```

Open:

```text
http://localhost:8501
```

---

### Command Line Interface

```bash
python main.py
```

You can provide:

- A local file path
- A GitHub file URL
- Selenium/Cypress code

---

## 🧪 Example

### Legacy Selenium

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

### Generated Playwright

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

## 🛠 Supported Frameworks

| Framework | Support |
|------------|----------|
| Selenium | ✅ |
| Cypress | ✅ |
| Playwright Output | ✅ |

---

## 💻 Technology Stack

- Python
- Streamlit
- LangChain
- Google Gemini
- Playwright
- Pytest

---

## 🎯 Key Benefits

- Faster framework migration
- Reduced manual effort
- Playwright best practices
- Flakiness reduction
- Automated modernization workflow

---

## 🚀 Future Enhancements

- Batch test conversion
- Repository-wide migration
- Playwright execution validation
- Migration quality scoring
- CI/CD integration
- Exportable PDF reports

---

## 👨‍💻 Author

**Pratap Dey**

Senior Consultant

Capgemini

---

⭐ If you found this project useful, consider giving it a star.